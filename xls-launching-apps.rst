Launching Apps from a Survey
============================

.. _contents:
  :local:

To Answer a single Question
---------------------------

Other Android applications can be launched from within FieldTask in order to answer a text, integer or decimal question. The information required to
start the other Android app is placed in the appearance column and consists of::

  ex:the_android_intent(parameters)

For example::

  ex:org.xxxx.myapp(param1='a', param2='b')

The external application should document the **intent** required to launch it and also the parameters.

To Answer Multiple Questions
----------------------------
