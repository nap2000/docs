Submission
==========

.. contents::
 :local:

.. http:post:: /submission?device={device identifier}

  :synopsis: Submit data for a completed form to the server
  
Contents::

  Content Type: multipart/form-data
  Contains 1 form data part
  Contains 0 or more additional parts for attachments (images etc)

Form Data Part::

  Content Type: text/xml
  Name: xml_submission_file

Additional Parts:: 

  Content Type: Matches the type of attachment
  Name: Matches the value of an xml element in the xml_submission_file
  
xml_submission_file::

  Top level element: main
  Attribute id: The survey identifier
  Attribute project: The name of the project (optional)
  Attribute version: The version of the form that was used to create this submission file
  meta: Metadata
  data:  Elements with the names of questions containing the response to that question

metadata::

  instanceID:  A unique identifier for this submission (required)
  instanceName: The instance name (optional)

The following example response is for a form that has 3 questions: q1,q2 and q3.  q2 was not answered, q3 is an image type question.

Example xml_submission_file::

  <?xml version='1.0' ?>
  <main id="s10_16" project="A Project Name" version="2"
    xmlns:ev="http://www.w3.org/2001/xml-events"
    xmlns:orx="http://openrosa.org/xforms"
    xmlns:odk="http://www.opendatakit.org/xforms"
    xmlns:h="http://www.w3.org/1999/xhtml"
    xmlns:jr="http://openrosa.org/javarosa"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <meta>
      <instanceID>uuid:b75f5fdc-a6a3-4dc6-b186-0bbcef40abda</instanceID>
      <instanceName />
    </meta>
    <_start>2022-06-15T13:43:38.502+10:00</_start>
    <_end>2022-06-15T13:43:55.874+10:00</_end>
    <_device>PlanAssist:VcFYjONFwzqeSAc2</_device>
    <q1>Fff</q1>
    <q2 />
    <q3>ba76714c-13b0-4340-bf8a-4c0e51de93f1.jpg</q3>
  </main> 
