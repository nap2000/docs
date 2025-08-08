Mobile Administration
=====================

.. contents::
 :local:

Shared Devices
--------------

Commonly an evaluation will take place with Android devices that belong to the surveying organisation.  They will be taken out of a cupboard and
distributed to enumerators during the enumerator training.  This situation is the subject of this page of the documentation.

Tracking who has a device
-------------------------

It is good practice to to record who has received which device so that lost or damaged devices can be accounted for. It is also useful to know
which device submitted a completed survey.  This is particularly true if you are not giving enumerators individual logons and hence the only way
to identify the enumerator is by the device that has been given to them.

For example you may use a spreadsheet like the following:

.. csv-table:: Device Tracking
  :header: number, device identifier, enumerator name, date

  1, FieldTask:V1025HI67UikxlcB, Sally, 2021-03-16

The first column ``number`` can contain a simple unique identifier that you write on a sticker on the back of the device.  Possibly also with the
name of the organisation that the device belongs to.

The second column ``device identifier`` contains the globally unique identifier that is sent to the server with each record submitted.   You can get this
identifier by:

#.  Ensuring that the "Enable user and identify menu" option in :ref:`mobile-device-settings` is checked. If it wasn't set then set it and press ``refresh`` in FieldTask
#.  In FieldTask select ``menu`` then ``General Settings`` then ``User and device identity`` then ``Form metadata``
#.  The device identifier will be shown on the screen

