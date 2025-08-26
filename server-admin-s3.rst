.. _s3:

Store Attachments on S3
=======================

.. contents::
 :local:

Create a file called **bucket** in **/smap/settings** containing the name of the bucket where you are going to store attachments

Add the following to smap-ssl.conf (Inside the virtual host after the Directory Index)::

  SSLProxyEngine on
  RequestHeader unset Authorization
  ProxyPass         /app/attachments https://{bucket}.s3-{region}.amazonaws.com/attachments
  ProxyPassReverse  /app/attachments https://{bucket}.s3-{region}.amazonaws.com/attachments


Add proxy_http to apache2::

  a2enmod proxy_http

Add a bucket policy restricting access to the bucket to the server that manages its data::

  {
    "Version": "2012-10-17",
    "Id": "Allow access from proxy server",
    "Statement": [
      {
        "Sid": "Allow get requests originating from {server domain name}",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::{bucket}/*",
        "Condition": {
          "IpAddress": {
            "aws:SourceIp": "{server ip}/32"
          }
        }
      }
    ]
  }

Important if may be necessary to specify access to the VPC of the EC2 server (was required in ap-southeast-2 region)::

 {
    "Version": "2012-10-17",
    "Id": "Allow access from proxy server",
    "Statement": [
      {
        "Sid": "Allow get requests originating from {server domain name}",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::{bucket}/*",
        "Condition": {
          "StringEquals": {
            "aws:SourceVpc": "{vpc of server}"
          }
        }
      }
    ]
  }

The access to attachments, in the apache config file "smap-volatile.conf", will need to be overridden.
The volatile-conf file contains the latest apache http server access rules, however it is a generic file that is used for all installations, it also will get replaced
every time you deploy an update to the server.

In this case we have to also allow access to attachments from the installed server.  This is required when embedding media into PDF files and when
media needs to be included in a report. If the media is stored locally this is not a problem as the local file is accessed, however when it is stored
in S3, permission needs to be provided to call the URL.  We don't want to provide a hardcoded password as this will be viewable in the source, instead we
want the Apache web server to forward the request if it comes from the local server without requiring a logon.  This change should be made to smap-ssl.conf in /etc/apache2-sites-available.  Add
the following Location directive directly after the line that includes smap-volatile, so it will look like the following::

  Include sites-available/smap-volatile.conf
  <Location /attachments>
    AuthType Basic
    AuthName "smap"
    AuthBasicUseDigestAlgorithm MD5
    AuthBasicProvider dbd
    AuthDBDUserRealmQuery "select password from users where ident = %s and realm = %s"
    Require valid-user
    Require ip {public permanent IP address of the server}
  </Location>
