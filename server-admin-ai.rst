.. _ai-server-admin:

Switch on AI Access
===================

.. contents::
 :local:

Smap can act as an MCP server, which lets an AI client such as Claude Code or ChatGPT work with your
server on somebody's behalf: reading data, changing surveys, administering users. It is off on every
server until a server owner switches it on.

This page is for somebody running their own Smap server. If you are on one of our hosted servers you
cannot change these settings - ask us to switch it on for you. Once it is on, everything else is on
the AI access page (:ref:`ai-access`).

The two things worth understanding first
----------------------------------------

**An AI client acts as a person, with that person's permissions.** It can never do more than the
account it is acting for. Giving somebody AI access does not widen what they can reach; it lets a
program reach it for them.

**The person is accountable, and the application is recorded.** Every change is written to the audit
trail with both: who it was done for, and which application did it. On the changes page of a record,
an entry made by an AI client shows the application name under the user name. An entry made by a
person in the console shows nothing extra, which is most of them.

Switching it on
---------------

Only a server owner can do this.

#.  Settings, then the **MCP Server** section.
#.  Tick **Enable the MCP server**. Until this is ticked every MCP address answers as though it does
    not exist, and no token works.
#.  Leave **How AI clients register** at *Client ID Metadata Documents, with dynamic registration for
    older clients* unless you have a reason to narrow it.

The other settings there:

**Max rows an MCP request may return**
  0 means the built-in default. There is no value that means unlimited - an AI asking for "all the
  data" always gets a bounded answer.

**MCP access token lifetime (seconds)**
  3600 is the default. A shorter life means more re-authorisation; it does not make a stolen token
  safe, because a token can be withdrawn at once from the AI access page.

**Allow AI clients to manage users and their permissions**
  Off, on every server, until somebody deliberately turns it on. See below.

Nothing works until a user is also given the **mcp access** security group, which only a server owner
can grant and only while the MCP server is on. See :ref:`ai-access`.

The permissions switch
----------------------

**Allow AI clients to manage users and their permissions** governs whether an AI client can create
users, change what they are allowed to do, change which projects they belong to, change roles, or
remove people.

With it off, those tools do not appear to any client and cannot be called. With it on, they still
require the person to be an administrator, and they enforce every rule user management enforces - a
plain administrator still cannot make somebody a security manager, and nobody can grant server owner
at all.

One rule holds whatever the switch says: **a session cannot change its own permissions.** An AI
client acting as you cannot alter your account, whatever your account is allowed to do. Ask another
administrator, or use the console.

Off is the right default. Turn it on when somebody has a reason, and turn it off again afterwards.

What the server will not let an AI client do
--------------------------------------------

Whatever is switched on:

- **It never sends anything.** No email, no SMS, no webhook, no mailout. A notification can be
  prepared and switched off or on; sending is done by a person from the console.
- **It cannot read or change the mail settings, the keys or the stylesheet.** Server settings that
  are credentials are not readable or writable through MCP at all.
- **It cannot switch itself on, or widen its own permissions.** The settings on this page are console
  only, so a client cannot enable the permissions switch and then ask for it.
- **It cannot export a file.** The interface is interactive. Data subject access exports and report
  downloads are done from the console.

Rate limiting
-------------

One token is limited to 120 calls a minute, or the server's API rate if that is lower. The limit is
generous for a conversation and is there to catch an AI client that has got into a loop, which is a
thing that happens by accident and at machine speed. A client that reaches it is told to wait a
minute.

Problem Resolution
------------------

**Nothing works at all and the address is not found**
  The MCP server is switched off, or the user does not have the **mcp access** group. Both answer the
  same way deliberately, so that an unauthorised caller learns nothing about whether the feature
  exists.

**A tool the user expects is not listed**
  Tools are hidden when the person's security groups could never allow them, and when the permission
  they need is one this server does not issue - which is what the permissions switch controls.

**Everyone is asked to re-authorise after an upgrade**
  Expected, and not a fault. See :ref:`ai-access`.
