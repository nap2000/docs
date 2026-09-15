.. _ai-access:

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

What you can ask it to do
-------------------------

The AI is given around eighty tools, and picks the ones it needs from what you ask. You do not call
them yourself. Broadly they cover:

**Your data**
  Answering questions about records - how many, which ones, totals and averages by group - reading a
  single record with its repeats, listing its attachments, and reading the history of what changed on
  it and who changed it. It can also fill a form in, correct a record, change many records at once,
  and undo such a change as a set.

**Your surveys**
  Reading a survey's questions, choice lists, settings and change history. Creating a survey, and
  changing one: adding questions, adding groups and repeats, moving a question into or out of a
  group, making and editing choice lists, and changing which list a question offers. Before changing
  a question's type it can tell you what that would do to the answers already collected.

**Your processes**
  Tasks, cases and the rules that pass work from one person to the next, including drawing the whole
  workflow so you can see what a submission sets off and where it branches.

**Your organisation**
  Users, projects, roles and groups. Reading them needs the Administration permission, and an
  administrator account - these are not things an ordinary user can ask for. Changing who can reach
  what - adding and removing people, or changing somebody's groups, projects or roles - needs the
  Access control permission as well, which your server may withhold from every client whoever is
  asking.

**How things are going**
  Outstanding work across the organisation, what has happened recently, monthly usage, and finding
  everything held about one person for a subject access request.

There are some things it deliberately cannot do, listed above, and a few more: it cannot export a
file, read or change your mail settings or keys, or switch its own access on.

Before you can connect
----------------------

Two things have to be true, and both are somebody else's to arrange:

#.  **The MCP server has to be switched on.** It is off on every Smap server until a server owner
    turns it on. If you run your own server, see :ref:`ai-server-admin`. If you are on one of our
    hosted servers, or on a server somebody else administers, ask them to switch it on.
#.  **You need the mcp access security group.** Only a server owner can grant it, and only while the
    MCP server is on.

If either is missing the connection fails and the address behaves as though it does not exist. That
is deliberate - an unauthorised caller is not told whether the feature exists - so "not found" does
not tell you which of the two is missing. Ask whoever administers your server.

Your access is checked on every request, not only when you first signed in. If the group is taken
away your AI clients stop at once, including a conversation already running.

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

Connecting other AI clients
---------------------------

Smap is a standard MCP server, so anything that can connect to one can connect to Smap. What your
client needs to know:

=============================== ==============================================================
Address                         ``https://yourserver.smap.com.au/mcp``
Transport                       HTTP. The client sends each request as a POST and gets a reply.
                                There is no event stream, so a client that only supports the
                                older SSE transport cannot connect directly
Signing in                      Either sign in through the browser, which the client arranges
                                for you, or a token from the **AI access** page for anything
                                without a browser
=============================== ==============================================================

Claude Desktop and claude.ai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a custom connector and give it the same address. It will open a browser to sign in, show you the
same consent screen, and the tools become available in the conversation. The menu this lives under
has moved between releases, so look for connectors or integrations in settings.

ChatGPT
~~~~~~~

ChatGPT connects to servers like Smap as a custom connector. Give it the address above and sign in
when it asks. Which plans offer this, and where it is in the settings, has changed more than once, so
check OpenAI's own documentation.

One thing is worth knowing before you try. Some kinds of connector - the deep research one in
particular - will only accept a server that offers two tools named ``search`` and ``fetch``. Smap
offers neither, because its tools are named for what they actually do. Used that way, ChatGPT will
report the server as unsuitable, while the same server works normally as an ordinary connector. There
is no setting on either side that changes this.

Open source and self-hosted models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A model does not connect to anything - the application around it does. So Llama, Mistral, Qwen or
anything else you run yourself will work with Smap as long as the application you are running it in
speaks MCP.

The practical limit is not the connection, it is the model. Smap offers a lot of tools, and a small
model will choose the wrong one or make up its arguments. Use the largest instruction-tuned model you
can run, expect to be more explicit about what you want than you would be with a hosted model, and
check what it did.

If your application can sign in through a browser, give it the address and let it do so. If it
cannot, mint a token on the **AI access** page and give it the address together with this header::

  Authorization: Bearer <your token>

Most applications have somewhere to put extra headers in their server settings.

If your application can only start a local program and talk to it - rather than call a web address -
you need a bridge between the two. ``mcp-remote`` is the usual one, and is run as the program your
application starts::

  npx -y mcp-remote https://yourserver.smap.com.au/mcp

A script or a scheduled job
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Anything with no browser signs in with a token from the **AI access** page. The value is shown once
and never again, so save it when you create it.

A token acts as you, is not tied to any device, and anybody holding it has your access. Treat it as
you would a password, and withdraw it from the same page when the job is finished.

If a client will not connect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Worth checking in this order:

- **Nothing responds and the address appears not to exist.** Either the MCP server is switched off,
  or you do not have the **mcp access** group. Both look the same on purpose. Ask whoever
  administers your server.
- **Your client asks for an SSE or a WebSocket address.** It supports only the older transport. Use
  a bridge as described above, or a different client.
- **Your client asks for** ``search`` **and** ``fetch`` **tools.** See the note under ChatGPT.
- **You signed in but something you expected is missing.** Tools you could never use are not offered
  at all, and neither are tools needing a permission your server does not allow.
- **It worked yesterday and now wants you to sign in again.** Expected after an upgrade - see below.
- **It stops part way through and says to wait a minute.** One token may make 120 calls a minute.
  That is generous for a conversation, and usually means the AI has got into a loop. Wait, then say
  what you wanted more specifically.

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

If you administer other people's access
---------------------------------------

A security manager, an organisation administrator or a server owner sees everybody in the
organisation on the **AI access** page, not just themselves. Each row is an application that can act
as that person, with their permissions, until somebody withdraws it.

Granting somebody the **mcp access** group is done from user management, and only a server owner can
do it. Taking it away stops their AI clients immediately.

The page also mints a token for something that has no browser to sign in with - a script, a scheduled
job. The value is shown once and never again. A token acts as the person it was minted for and is not
tied to any device, so treat it as you would a password.

Whether an AI client can create users, change permissions, change project membership or remove people
is a server-wide setting that is off by default. If those tools are missing and you expected them,
that switch is why - see :ref:`ai-server-admin`.

Getting more out of it
----------------------

The server publishes a set of ready-made procedures for jobs that take several steps - analysing a
survey's data, checking data quality, triaging tasks, summarising a week, working out why data is not
arriving, reorganising projects, adding somebody new. In Claude Code they appear as slash commands.
They are worth using in preference to describing the job yourself, because they carry the order
things have to happen in and the mistakes that are expensive.
