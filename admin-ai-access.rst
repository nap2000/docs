AI Access
=========

.. contents::
 :local:

Smap can be used by an AI client such as Claude Code, which connects to the server and works on your
behalf: answering questions about your data, changing surveys, managing users and projects. This page
explains how to connect one and how to take that access away again.

What an AI client can and cannot do
-----------------------------------

**It acts as you.** Everything it does, it does with your permissions and under your name. It can
never reach anything your own account could not reach. If you cannot see a survey, neither can it.

**What it does is recorded.** Every change is written to the audit trail with both facts: that you
are accountable for it, and which application made it. On a record's changes page, a change made by
an AI client shows the application name underneath your name.

**It does not send anything.** No email, no SMS, no webhook, no mailout. It can set a notification up
and switch it on or off, and it can tell you what would be sent, but sending is something a person
does from the console.

**It asks before doing anything large or irreversible.** Changing many records at once, deleting a
role, removing somebody's account - these stop and ask first, and say what cannot be undone.

Before you can connect
----------------------

You need the **mcp access** security group. Only a server owner can grant it, so ask whoever
administers your server. They also have to switch the MCP server on, which is a server-wide setting.

If either is missing, the connection fails and the address behaves as though it does not exist.

Connecting Claude Code
----------------------

In a terminal::

  claude mcp add --transport http smap https://yourserver.smap.com.au/mcp

Then, inside Claude Code::

  /mcp

Choose **smap** and authenticate. A browser window opens on your Smap server, you sign in as normal,
and a consent screen lists what the application is asking to be allowed to do. Each permission has
its own checkbox, and you can clear any you do not want to grant.

The consent screen is shown every time an application is authorised. Nothing is remembered on your
behalf.

Check what you are connected as with::

  /mcp

or by asking the AI to run **whoami**, which reports the account it is acting as and what it has been
allowed to do.

The permissions you may be asked for
------------------------------------

============================= ==========================================================
Read                          Everything you can already see, read only
Write                         Surveys, data, tasks, cases, notifications
Administration                Users, projects and the organisation as objects
Access control                What people are allowed to do, including creating and
                              removing accounts. Only offered if your server allows it
Server settings               The server's operational limits. Server owners only
Privacy                       Finding what is held about one person. Data protection
                              officers only
============================= ==========================================================

Grant the narrowest set that covers what you are doing. You can always authorise again for more.

"Requires re-authorization" after a server upgrade
--------------------------------------------------

This is expected and is not a fault.

An application can only be given a permission it has asked for, and it only asks after being refused
for want of it. So the first time you use a capability that has just been added, the call fails, the
connection drops, and running ``/mcp`` again picks up the new permission. It happens once per new
permission.

Taking access away
------------------

Settings, then **AI access**. The page lists every application that can currently act as you, when
you first allowed it, and when it was last used.

**Self registered** beside an application means it registered itself with your server. Anyone can do
that, and the name was chosen by whoever did, so treat an unfamiliar one with suspicion.

Withdrawing an application stops every token it holds immediately - not at the end of the
conversation. If it comes back it has to be authorised by a person again.

If you think an application is doing something you did not intend, withdraw it first and work out
what happened afterwards. That is what the button is for.

Getting more out of it
----------------------

The server publishes a set of ready-made procedures for jobs that take several steps - analysing a
survey's data, checking data quality, triaging tasks, summarising a week, working out why data is not
arriving, reorganising projects, adding somebody new. In Claude Code they appear as slash commands.
They are worth using in preference to describing the job yourself, because they carry the order
things have to happen in and the mistakes that are expensive.
