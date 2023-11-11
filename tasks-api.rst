.. _tasks-api:

Tasks
=====

.. contents::
 :local:


Task Groups
-----------

.. http:get:: /api/v1/tasks/groups/(project id)

  :synposis: get a list of task groups in a project.  You can use the :ref:`tasks-api` request with a query parameter of `links=true` to get a list of available task groups URLs
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/tasks/groups/1554
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	[
	  {
		"tg_id": 199,
		"name": "xxxx",
		"address_params": "[]",
		"p_id": 1,
		"rule": {
		  "task_group_name": "xxxx",
		  "dl_dist": 0,
		  "show_dist": 100,
		  "source_survey_id": 17821,
		  "target_survey_id": 20282,
		  "project_name": "A project",
		  "source_survey_name": "3. School Personnel",
		  "survey_name": "accuracy",
		  "user_id": -2,
		  "role_id": 0,
		  "fixed_role_id": 0,
		  "assign_data": "${q1.1}",
		  "task_group_id": 0,
		  "blank": true,
		  "prepopulate": true,
		  "update_results": false,
		  "add_future": true,
		  "add_current": false,
		  "address_columns": [],
		  "filter": {
			"qId": 0,
			"oId": 0,
			"qInteger": 0,
			"qStartDate": 0,
			"qEndDate": 0,
			"advanced": "${q1.2} > 1000"
		  },
		  "taskStart": -1,
		  "taskAfter": 3,
		  "taskUnits": "days",
		  "taskDuration": 2,
		  "durationUnits": "hours",
		  "emailDetails": {
			"subject": "",
			"content": ""
		  },
		  "complete_all": true,
		  "assign_auto": false
		},
		"source_s_id": 17821,
		"target_s_id": 20282,
		"totalTasks": 1,
		"completeTasks": 1,
		"emaildetails": {
		  "subject": "",
		  "content": ""
		}
	  }
	 
	]
	
  In the task group details shown above:
  
  *  A task is created if the answer to question q1.2 in the submitted data was greater than 1000
  *  The task is assigned to the user identified in the answer to question q1.2
  *  Tasks are triggered by survey 17821 and require the completion of survey 20282
  
  :reqheader Authorization: basic
  :statuscode 200: no error

Task List
---------

.. http:get:: /api/v1/tasks

  :synposis: get a list of tasks.
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/tasks
  
  The format of the response is GeoJSON.
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	{
	  "type": "FeatureCollection",
	  "features": [
		{
		  "type": "Feature",
		  "geometry": {
			"type": "Point",
			"coordinates": [
			  0,
			  0
			]
		  },
		  "properties": {
			"tg_id": 234,
			"name": "cccc",
			"form_id": 17831,
			"survey_ident": "s1_17829",
			"assignee_ident": "neil",
			"generate_user": false,
			"from": "2019-11-09 01:44:34",
			"to": "2019-11-09 02:44:34",
			"location_trigger": "",
			"repeat": false,
			"repeat_count": 1,
			"guidance": "",
			"lon": 0,
			"lat": 0,
			"complete_all": true,
			"assign_auto": true,
			"show_dist": 0,
			"id": 2507,
			"tg_name": "Locate",
			"p_id": 0,
			"a_id": 2215,
			"survey_name": "2. Entèvyou paran oubyen gadyen (Parent Guardian) (1)",
			"blocked": false,
			"assignee": 3988,
			"assignee_name": "Neil Penman",
			"comment": "",
			"status": "late"
		  },
		  "links": {
			"detail": "https://sg.smap.com.au/api/v1/tasks/2507",
			"webform": "https://sg.smap.com.au/webForm/s1_17829?assignment_id=2215"
		  }
		},
		{
		  "type": "Feature",
		  "geometry": {
			"type": "Point",
			"coordinates": [
			  153.01260069944,
			  -27.446150149836
			]
		  },
		  "properties": {
			"tg_id": 235,
			"name": "Light 2",
			"form_id": 20361,
			"survey_ident": "s1554_20361",
			"assignee_ident": "neil",
			"generate_user": false,
			"from": "2019-11-09 04:21:16",
			"to": "2019-11-09 05:21:16",
			"location_trigger": "",
			"repeat": false,
			"repeat_count": 1,
			"guidance": "",
			"lon": 153.01260069943964,
			"lat": -27.446150149835972,
			"complete_all": true,
			"assign_auto": true,
			"show_dist": 0,
			"id": 2508,
			"tg_name": "Maintenance",
			"p_id": 0,
			"a_id": 2216,
			"survey_name": "street light",
			"blocked": false,
			"assignee": 3988,
			"assignee_name": "Neil Penman",
			"comment": "",
			"status": "late"
		  },
		  "links": {
			"detail": "https://sg.smap.com.au/api/v1/tasks/2508",
			"webform": "https://sg.smap.com.au/webForm/s1554_20361?assignment_id=2216"
		  }
		}
	  ]
	}
	
  :query user: The ident of the user who has been assigned the task.  Use `_unassigned` to return unassigned tasks.
  :query tg_id: The task group id.
  :query period: One of `all`, `week` or `month`.  The default is `week` which will return only the recent tasks created in the past week.  
                 Hence this is an option you will probably want to change to `all` in order to get all of the tasks.
  :query start: The `id` of the first task to get.
  :query limit: The number of tasks to return.
  :query sort: The property to sort on. This can be one of `id` (the default) or `scheduled` the scheduled start of the task.
  :query dirn: The direction of sort.  One of `asc` or `desc`
  :query tz: The timezone for example ``Australia/Brisbane``.  All date time and date answers will be returned in this time zone.
  :query status: A comma separated list of status values.  These can include `new`, `accepted`, `late`, `unsent`, `unsubscribed`, 
                 `submitted`, `rejected`, `cancelled`, `deleted`, `pending`, `error`, `blocked`. Refer to :ref:`task-lifecycle` for details
                 on how a task gets a status value.
  :reqheader Authorization: basic
  :statuscode 200: no error
  
.. _single-task:

Details of a Single Task
------------------------

.. http:get:: /api/v1/tasks/(task id)

  :synposis: Get the details for a single task.
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/tasks
  
  .. sourcecode:: http

    HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	{
	  "tg_id": 234,
	  "name": "cccc",
	  "form_id": 17831,
	  "survey_ident": "s1_17829",
	  "assignee_ident": "neil",
	  "generate_user": false,
	  "from": "2019-11-09 01:44:34",
	  "to": "2019-11-09 02:44:34",
	  "location_trigger": "",
	  "repeat": false,
	  "repeat_count": 1,
	  "guidance": "",
	  "lon": 0,
	  "lat": 0,
	  "complete_all": true,
	  "assign_auto": true,
	  "show_dist": 0,
	  "id": 2507,
	  "tg_name": "Locate",
	  "p_id": 0,
	  "a_id": 2215,
	  "survey_name": "2. Entèvyou paran oubyen gadyen (Parent Guardian) (1)",
	  "blocked": false,
	  "assignee": 3988,
	  "assignee_name": "Neil Penman",
	  "comment": "",
	  "status": "late"
	}
	
    :reqheader Authorization: basic
    :statuscode 200: no error

Create a Task
-------------
	
.. http:post:: /api/v1/tasks

  :synposis: Create a task. The payload is a JSON object and can use the same attributes as returned by :ref:`single-task`.  The payload is sent as x-www-form-urlencoded content with a key of "task".  Use :ref:`single-task` API call to get templates for the data that can be posted. 

  **Example request**:

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Vary: Accept
    Content-Type: application/x-www-form-urlencoded

    task = {
       "tg_id": 226,
       "name": "Assign to neil",
       "survey_ident": "s38_722",
       "assignee_ident": "neil",
       "initial_data_source": "none",
       "from": "2019-04-15 01:48:17",
       "to": "2019-04-15 02:48:17"
    }		   
  

  **Example request 2**:

Initial data is included in the task.   In this second example the task "id" is specified hence the existing task will be updated.

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Vary: Accept
    Content-Type: application/x-www-form-urlencoded

    {
      "tg_id": 4,
      "name": "xxxx : A project : geopoint",
      "form_id": 37,
      "survey_ident": "s1_37",
      "assignee_ident": "neil",
      "generate_user": false,
      "initial_data_source": "task",
      "from": "2020-02-06 01:37:42",
      "repeat": false,
      "repeat_count": 0,
      "lon": 153.013277,
      "lat": -27.445506,
      "complete_all": true,
      "assign_auto": false,
      "initial_data": {
        "values": {
          "q1": "hello 2"
        },
        "point_geometry": {
          "coordinates": [
            153.013277,
            -28.445506
          ],
          "altitude": 0,
          "accuracy": 0,
          "type": "Point"
        }
      },
      "show_dist": 0,
      "id": 9,
      "tg_name": "xxxx",
      "p_id": 0,
      "a_id": 9,
      "survey_name": "geopoint",
      "blocked": false,
      "assignee": 2,
      "assignee_name": "neil",
      "status": "accepted"
    }

  **Example Response:**

    Details on the task created as well as a link to a webform that can complete the task are returned

    .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "task": {
          "tg_id": 4,
          "name": "xxxx : A project : geopoint",
          "form_id": 37,
          "survey_ident": "s1_37",
          "generate_user": false,
          "initial_data_source": "task",
          "from": "2020-02-06 01:37:42",
          "repeat": false,
          "repeat_count": 0,
          "lon": 153.013277,
          "lat": -27.445506,
          "complete_all": true,
          "assign_auto": false,
          "initial_data": {
              "values": {
                  "q1": "hello 2"
              },
              "point_geometry": {
                  "coordinates": [
                      153.013277,
                      -28.445506
                  ],
                  "altitude": 0.0,
                  "accuracy": 0.0,
                  "type": "Point"
              }
          },
          "show_dist": 0,
          "id": 13,
          "tg_name": "xxxx",
          "p_id": 0,
          "a_id": 0,
          "survey_name": "geopoint",
          "blocked": false,
          "assignee": 0,
          "status": "new"
        },
          "links": {
            "webform": "https://ubuntu1804.smap.com.au/webForm/s1_37?taskkey=13&assignment_id=0"
        }
      }

 **Example request 3**:

Initial data is obtained from an existing record.  Hence the initial_data_source is set to "survey" and the
instanceId of the record to update is included as "update_id".

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Vary: Accept
    Content-Type: application/x-www-form-urlencoded

    {
      "tg_id": 4,
      "name": "xxxx : A project : geopoint",
      "form_id": 37,
      "survey_ident": "s1_37",
      "assignee_ident": "neil",
      "generate_user": false,
      "initial_data_source": "survey",
      "update_id": "uuid:7df6eb5f-c4b0-4837-9063-09653078782a",
      "from": "2020-02-06 01:37:42",
      "repeat": false,
      "repeat_count": 0,
      "lon": 153.013277,
      "lat": -27.445506,
      "complete_all": true,
      "assign_auto": false,
      "show_dist": 0,
      "id": 9,
      "tg_name": "xxxx",
      "p_id": 0,
      "a_id": 9,
      "survey_name": "geopoint",
      "blocked": false,
      "assignee": 2,
      "assignee_name": "neil",
      "status": "accepted"
    }

  :query preserveInitialData: When updating an existing task that already has initial data you can choose to not include initial_data
         and to set this parameter to either preserve the existing data or clear it.  One of `true` or `false`

