.. _organisational-hierarchy:

Organisational Hierarchy
========================

Surveys and data are stored in a hierarchical structure. The security groups possesed by a user determines how high in that structure they
can go. 

.. figure::  _images/concept1.jpg
   :align:   center
   :alt:     Organisational Hierarchy

   Organisational Hierarchy
   
Hence if a user has the **admin** security group then they can create and add themselves to projects.  However unless they have
the **organisation** privilege they cannot access projects in a different organisation.  The same applies to a user with the
**organisation** privilege.  They can create and access different organisations and all the projects within those organisations
however they cannot access organisations or projects in a different enterprise.
