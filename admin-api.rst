Admin API
=========

.. contents::
 :local:

This API provides access to administration functions.  To use these functions you will need **admin** privilege.

Usage
-----

.. http:get:: /surveyKPI/adminreport/usage/(int: year)/(int: month)

  :synposis: The usage API allows you to view the number of submissions made by each user in a `month`. These can be further broken down by `project`, `survey` and `device`.
  
  **Example request**:

  .. sourcecode:: http

    GET /surveyKPI/adminreport/usage/2018/1 HTTP/1.1
    Host: sg.smap.com.au
    Accept: xlsx


  :query boolean project: Show usage by project
  :query boolean survey: Show usage by survey
  :query boolean device: Show usage by device

  **Example response**:
  
  .. figure::  _images/api1.jpg
   :align:   center
   :width:   400px
   :alt:     Usage by User

   Usage by User
   
Resources
---------

.. http:get:: /surveyKPI/upload/media

  :synposis: Get a list of the media :ref:`shared-resources` available in the users current organisation.  Includes images, video, audio and csv files.
  
  **Example response**:
  
  https://sg.smap.com.au/surveyKPI/upload/media
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	{
	"files": [
	{
	"name": "a.jpg",
	"url": "/surveyKPI/file/a.jpg/organisation",
	"thumbnailUrl": "/surveyKPI/file/a.jpg/organisation?thumbs=true",
	"deleteUrl": "https://sg.smap.com.au/surveyKPI/upload/media/organisation/1/a.jpg",
	"type": "image",
	"size": 7946,
	"modified": "2019-04-21T22:32:42.000+0000"
	},
	{
	"name": "b.jpg",
	"url": "/surveyKPI/file/b.jpg/organisation",
	"thumbnailUrl": "/surveyKPI/file/b.jpg/organisation?thumbs=true",
	"deleteUrl": "https://sg.smap.com.au/surveyKPI/upload/media/organisation/1/b.jpg",
	"type": "image",
	"size": 7236,
	"modified": "2019-04-21T22:32:42.000+0000"
	},
	{
	"name": "c.jpg",
	"url": "/surveyKPI/file/c.jpg/organisation",
	"thumbnailUrl": "/surveyKPI/file/c.jpg/organisation?thumbs=true",
	"deleteUrl": "https://sg.smap.com.au/surveyKPI/upload/media/organisation/1/c.jpg",
	"type": "image",
	"size": 1075,
	"modified": "2019-04-21T22:32:42.000+0000"
	},
	{
	"name": "camps.csv",
	"url": "/surveyKPI/file/camps.csv/organisation",
	"thumbnailUrl": "/images/csv.png",
	"deleteUrl": "https://sg.smap.com.au/surveyKPI/upload/media/organisation/1/camps.csv",
	"type": "csv",
	"size": 103116,
	"modified": "2019-09-12T06:36:19.000+0000"
	}
	]
	}
	
  :query survey_id: The id of a survey to return the media. If specified the media associated with the survey will be returned rather than the shared media for the organisaiton. 
  :reqheader Authorization: basic
  :statuscode 200: no error

.. http:post:: /surveyKPI/upload/media

  :synposis: Upload a media file.
  
  **Example request**:
  
  curl -u xxxx -i -X POST -H "Content-Type: multipart/form-data" -F "data=@phone.jpg" https://sg.smap.com.au/surveyKPI/upload/media
  
 :query survey_id: The id of a survey if you want the media file to only be available to that survey.

.. _projects-api:
 
Projects
--------

.. http:get:: /api/v1/admin/projects

  :synposis: Get a list of projects.
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/admin/projects
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	[
	{
	"id": 1554,
	"name": "tasks",
	"desc": "",
	"tasks_only": false,
	"changed_by": "neil",
	"changed_ts": "2019-11-09 04:19:22.83124+00"
	}
	]
	
  :query boolean all:  If set to `true` all projects will be returned.  Otherwise only the project to which the user is currently assigned will be returned.
  :query boolean links: Return links to other project related data.
  :reqheader Authorization: basic
  :statuscode 200: no error
  
Submissions
-----------

.. http:get:: /api/v1/admin/submissions

  :synposis: A list of submissions in the calling user's organisation. The data is always returned as latest first
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/admin/aubmissions
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	[
	{
	"prikey": "856836",
	"Survey Name": "pp",
	"s_id": "14454",
	"survey_ident": "s1_14454",
	"instanceid": "uuid:7444b43e-dc6c-4037-9d84-06aaa4d181e2",
	"Device": "355306069766014",
	"Upload Time": "2019-11-09 01:35:59",
	"Project": "A project",
	"Instance Name": "",
	"Instance ID": "uuid:7444b43e-dc6c-4037-9d84-06aaa4d181e2",
	"Start Time": "2019-11-09 01:35:26",
	"End Time": "2019-11-09 01:35:55",
	"User": "neil"
	},
	{
	"prikey": "856835",
	"Survey Name": "v181203",
	"s_id": "14439",
	"survey_ident": "s1_14439",
	"instanceid": "uuid:fcbaf0a5-8ceb-413b-b180-58fc995447c4",
	"Device": "webform",
	"Upload Time": "2019-11-08 23:25:48",
	"Project": "A project",
	"Instance Name": "",
	"Instance ID": "uuid:fcbaf0a5-8ceb-413b-b180-58fc995447c4",
	"Start Time": "2019-11-08 23:25:26",
	"End Time": "2019-11-08 23:25:46",
	"User": "neil",
	"lon": 153.012455,
	"lat": -27.448157
	}
	]
	
  :query limit:  	Set to the number of records that you want to see. Since data is returned latest first then if you specify the limit as 10 you will see the last 10 submissions.
  :query start: The id to start from (upload id). If you specify a start of 1,000 and a limit of 2 then uploads 999 and 998 
                 will be returned. Note the id you specify in start will not be returned. You can use this parameter to page 
                 through the data setting the value of start to the oldest submission returned in the previous query.
  :query stopat: When set do not go past the specified upload id. The data for the specified upload id is not returned. 
                 You can use this when reading the data as a feed. For example if you call the service and the latest submission 
                 has an id of 1001, then if you call the service again with stopat=1001 you will only get the new submissions.
  :query user: Return the submissions for the specified user.
  :query tz: Set to a valid time zone. (Refer to timezones api call to get a list of valid time zones). The upload time will be 
                returned in this time zone.
  :query boolean links: Return links to other submission related data.
  :reqheader Authorization: basic
  :statuscode 200: no error
  
.. _timezone:

Timezone
--------

.. http:get:: /surveyKPI/utility/timezones

  :synposis: Many API calls include a timezone parameter so that dates can be returned in the specified time zone. This api returns the timezones that can be used.
  
  **Example response**:
  
  https://sg.smap.com.au/surveyKPI/utility/timezones
  
  A list of timezones. Each timezone consists of an "id" and a name. The "id" is what you should use to identifity the 
  time zone in a web service call. The name is just the "id" with the addition of the current hour offset from UTC. 
  The timezones are returned in order of increasing offset.
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	[
	{
	"id": "Pacific/Niue",
	"name": "Pacific/Niue (-11:00)"
	},
	{
	"id": "US/Samoa",
	"name": "US/Samoa (-11:00)"
	},
	{
	"id": "Pacific/Midway",
	"name": "Pacific/Midway (-11:00)"
	},
	{
	"id": "Pacific/Samoa",
	"name": "Pacific/Samoa (-11:00)"
	}
	]
	
  
  :reqheader Authorization: basic
  :statuscode 200: no error
 
Get a PDF of a submitted Record
-------------------------------

.. http:get:: /surveyKPI/pdf/(survey ident)

  :synposis: Returns a PDF of the data in the submission. You can use the data API passing a parameter of links=true to see the URLs that will return a PDF of data.
  
  :query instance:  (Required) The instance id of the record you want to retrieve.  
  :query tz: Set to a valid time zone.
  :reqheader Authorization: basic
  :statuscode 200: no error
  
Edit a submission in a Webform
------------------------------

.. http:get:: /webForm/(survey ident)

  :synposis: Opens the submission in a webform for editing. You can use the data API passing a parameter of links=true to see the URLs.
  
  :query datakey:  (Required) The column that holds the key of the record.  Usually you would use "instanceid"
  :query datakeyvalue: The value of the key that identified the record.
  :reqheader Authorization: basic
  :statuscode 200: no error


 