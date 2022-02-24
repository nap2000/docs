Admin
=====

.. contents::
 :local:

This API provides access to administration functions.  To use these functions you will need **admin** privilege.

Usage
-----

.. http:get:: /surveyKPI/adminreport/usage/(int: year)/(int: month)/(string: userIdent)

  :synposis: The usage API allows you to view the number of submissions made by each user in a `month`. These can be further broken down by `project`, `survey` and `device`. The API request stopped working in version 21.11 as this reporting usage for all users became too lengthy.  The reports generated from the user interface now run in the background and can later be downloaded from the reports page.  However this API call is back in version 21.12 with the addition of one more path parameter for the user ident. So it now downloads usage for only a single user.
  
  **Example request**:

  .. sourcecode:: http

    GET /surveyKPI/adminreport/usage/2018/1/sal HTTP/1.1
    Host: sg.smap.com.au
    Download: xlsx


  :query boolean project: Show usage by project
  :query boolean survey: Show usage by survey
  :query boolean device: Show usage by device
  :query boolean inc_temp: Include temporary and anonymous users
  :query int o_id: Organisation Id.  Can be used if the calling user has organisational administration privilege to get details on a user in a different organisation

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

.. _users-simple-api:
 
Users (Simple)
--------------

.. http:get:: /surveyKPI/userList/simple

  :synposis: Get a list of users in the current organisation of the user making the API call.
  
  **Example response**:
  

  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
        [
          {
            "id": 2,
            "ident": "neil",
            "name": "Neil Penman"
          },
          {
            "id": 3,
            "ident": "tom",
            "name": "Tom"
          }
        ]
	
  :statuscode 200: no error

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
  
.. _surveys-api:
 
Surveys
-------

Get
+++

.. http:get:: /api/v1/admin/surveys/(project id)

  :synposis: Get a list of surveys with details on each within the specified project. Projects can be found using :ref:`projects-api`.
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/admin/surveys/17
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
        [
          {
            "id": 116,
            "e_id": 0,
            "o_id": 0,
            "p_id": 17,
            "ident": "s17_115",
            "displayName": "csvtest",
            "task_file": false,
            "timing_data": false,
            "audit_location_data": false,
            "track_changes": false,
            "deleted": false,
            "blocked": false,
            "hasManifest": false,
            "forms": [],
            "optionLists": {},
            "styleLists": {},
            "serverCalculations": {},
            "sscList": [],
            "languages": [],
            "surveyManifest": [],
            "filters": {},
            "changes": [],
            "meta": [],
            "roles": {},
            "instance": {},
            "managed_id": 0,
            "version": 2,
            "loadedFromXLS": true,
            "exclude_empty": false,
            "projectName": "tx",
            "projectTasksOnly": false,
            "hideOnDevice": false,
            "dataSurvey": true,
            "oversightSurvey": true,
            "groupSurveyId": 0,
            "links": {
              "mailouts": "https://ubuntu1804.smap.com.au/api/v1/mailout/s17_115?links=true"
            }
          }
        ]
	
  :query boolean links: Return links to other survey related data.
  :reqheader Authorization: basic
  :statuscode 200: no error
  
Get Accessible
++++++++++++++

.. http:get:: /surveyKPI/surveys/idents

  :synposis: Get a list of survey names and their identifier and project name that are accessible by the calling user. (version 21.05+)
  
  **Example response**:
  
  https://sg.smap.com.au/surveyKPI/surveys/idents
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
            [
                {
                    "id": 296,
                    "project": "A project",
                    "name": "Audit this",
                    "ident": "s1_20363"
                },
                {
                    "id": 298,
                    "project": "A project",
                    "name": "Beneficiary List",
                    "ident": "s1_21255"
                },
                {
                    "id": 299,
                    "project": "A project",
                    "name": "Geotrace Line Form_ Draft (4)",
                    "ident": "s1_30057"
                },
                {
                    "id": 321,
                    "project": "A project",
                    "name": "Literacy_Assessment_test",
                    "ident": "s1_29888"
                }
            ]

  :reqheader Authorization: basic
  :statuscode 200: no error
  
Upload
++++++

.. http:post:: /surveyKPI/upload/surveytemplate

  :synposis: Upload a survey template in the spreadsheet format
  
  **Example request**:
  
  curl -u xxxx -i -X POST -H "Content-Type: multipart/form-data" -F "fileupload=@file.xlsx" -F templateName=name -F projectId=10 -F groupsurvey=0 https://sg.smap.com.au/surveyKPI/upload/surveytemplate

  :query fileupload: The name of the spreadsheet to upload
  :query templateName: The name to call the uploaded survey
  :query: projectId: The id of the project to store the survey in
  :query: groupsurvey: The id of the survey that you want to group this new survey with.  (optional). If you do include it set it to zero to specify no group


Submissions
-----------

.. http:get:: /api/v1/submissions

  :synposis: A list of submissions in the calling user's organisation. The data is always returned as latest first
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/submissions
  
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
	
  :query integer limit:  	Set to the number of records that you want to see. Since data is returned latest first then if you specify the limit as 10 you will see the last 10 submissions.
  :query integer start: The id to start from (upload id). If you specify a start of 1,000 and a limit of 2 then uploads 999 and 998 
                 will be returned. Note the id you specify in start will not be returned. You can use this parameter to page 
                 through the data setting the value of start to the oldest submission returned in the previous query.
  :query integer stopat: When set do not go past the specified upload id. The data for the specified upload id is not returned. 
                 You can use this when reading the data as a feed. For example if you call the service and the latest submission 
                 has an id of 1001, then if you call the service again with stopat=1001 you will only get the new submissions.
  :query text user: Return the submissions for the specified user.
  :query text tz: Set to a valid time zone. (Refer to timezones api call to get a list of valid time zones). The upload time will be 
                returned in this time zone.
  :query boolean links: Return links to other submission related data.
  :query text survey_ident: Only return data for the specified survey (version 21.01+)
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
  :query string tz: Set to a valid time zone.
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

Change current organisation
---------------------------

.. http:get:: /api/v1/users/organisation/(organisation name)

  :synposis: Set the users organisation to the value specified in "organisation name". Available in server version 21.03+.
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/users/organisation/head%20office
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	
  
  :reqheader Authorization: basic
  :statuscode 200: no error
 
