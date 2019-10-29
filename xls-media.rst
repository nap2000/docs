Questions with Media
====================

.. contents::
  :local:

As well as, or instead of, providing a standard text question such as "What is your name?", you can include an image, an audio file, and/or a
video file in the question.

.. note::

  Adding media to a question is different from asking a media question.  For example a question of type **image** where the label is "Take a picture".

Specifying Media
----------------

In the XLSForm template there are 3 columns for adding media:

*  media::image
*  media::audio
*  media::video

Add the names of your media files to those columns::

  intro.mp3

Do not include the path to the file only the name.

Loading the Media File
----------------------

The media file needs to be loaded onto the server so that it can be used by surveys.  The simplest approach is to load it into :ref:`shared-resources` where 
it can be used by any survey that references it.

Auto Play
---------

If you have an audio or video file in your question then you can set one of them to play automatically when the question is shown for the first time.  
In the **autoplay** column enter "audio" or "video" (no quotation marks) to specify which type to play.
