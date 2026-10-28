
.. _network-encryption:

Network Encryption
==================

.. contents::
 :local:

Generally I use certbot.

install Certbot as per https://certbot.eff.org
If there are any issues then install certbot-auto https://certbot.eff.org/docs/install.html

Then::

  sudo certbot --apache certonly

Update the apache ssl configuration file /etc/apache2/sites-available/smap-ssl.conf to identify the certbot certificate files::

  SSLCertificateFile    /etc/letsencrypt/live/{domain name}/fullchain.pem
  SSLCertificateKeyFile /etc/letsencrypt/live/{domain name}/privkey.pem

Create directory /var/log/certbot

Edit /etc/apache2/sites-available/smap.conf to uncomment the line that redirect all http requests to https

Setup Renewal
-------------

As root Crontab::

  44 19 * * * certbot renew >> /var/log/certbot/renew.log 2 >&1

Check for logs in /var/log/letsencrypt/letsencrypt.log

Custom Port / Reverse Proxy Configuration
------------------------------------------

By default Smap detects the port and host from the incoming HTTP request. This works for standard setups where
Apache proxies to Tomcat on the same machine. However, if your server is accessed on a non-standard port
(e.g., because a load balancer or reverse proxy sits in front and exposes a custom port), Smap may generate
incorrect URLs for form downloads and media manifests.

To override the detected values, set environment variables in Tomcat's ``context.xml``
(usually ``/etc/tomcat10/context.xml``).

**When to do this**

- Your server is accessed on a port other than 80 or 443.
- FieldTask or other clients are receiving form/manifest URLs with the wrong port.
- You are running behind a reverse proxy that terminates SSL on a non-standard port.

**How to configure**

Edit ``/etc/tomcat10/context.xml`` and add one or both of the following inside the ``<Context>`` element::

  <!-- Override the port Smap uses when building URLs -->
  <Environment name="server.port" value="8443" type="java.lang.Integer"/>

  <!-- Override the hostname (optional - only needed if the hostname is also wrong) -->
  <Environment name="server.host" value="example.com" type="java.lang.String"/>

Replace ``8443`` and ``example.com`` with your actual port and hostname. Restart Tomcat after making changes::

  sudo systemctl restart tomcat10

**Protocol detection**

Smap treats port 80 as HTTP and all other ports (including custom ports) as HTTPS. If you are running HTTP
on a non-standard port you will need to ensure your reverse proxy configuration forwards requests correctly.

.. _load-balancer:

Behind a Load Balancer
----------------------

When a load balancer, such as an AWS Application Load Balancer, sits in front of the server, every request reaches Apache
from the load balancer's address.  Unless Apache is told otherwise, Smap sees that address as the client's, so anything
that uses the client address treats everyone as the same client.  For example the limit of 3 registrations an hour from
one internet address becomes 3 an hour for the whole server, and the Turnstile check is given the wrong address.

Use mod_remoteip so that Apache takes the client's address from the X-Forwarded-For header the load balancer adds.  It
only does this for requests that come from the load balancer, so a client cannot set its own address by sending the header.

Enable the module.  On Debian and Ubuntu::

  sudo a2enmod remoteip

On RHEL, Amazon Linux and SUSE it is usually loaded already, check with ``apachectl -M | grep remoteip``.

Create ``remoteip.conf`` in ``/etc/apache2/conf-available`` on Debian and Ubuntu, ``/etc/httpd/conf.d`` on RHEL and Amazon
Linux, or ``/etc/apache2/conf.d`` on SUSE::

  RemoteIPHeader X-Forwarded-For
  # The addresses your load balancer connects from, for an AWS load balancer the CIDR range of its VPC subnets
  RemoteIPInternalProxy 10.0.0.0/16

Replace ``10.0.0.0/16`` with the range your load balancer uses.  Only list the load balancer's addresses, as any request from
a listed address can choose the client address it reports.  On Debian and Ubuntu enable the file with
``sudo a2enconf remoteip``, then on all systems::

  sudo apachectl configtest && sudo systemctl reload apache2      # httpd on RHEL and Amazon Linux

Tomcat receives the corrected address from Apache, so no change is needed in Smap.  To check it in the Apache access log,
the log format must use ``%a``, the client address, rather than ``%h``, which is still the address of the connection, that is
the load balancer.

Apache refuses requests for any host name other than the server's own, see the installation notes on setDomain.sh.  A load
balancer's health check is sent to the server's IP address and so is refused.  Remove the ``<If "req('Host') ...">`` block
from smap.conf and smap-ssl.conf and have the load balancer only forward requests for your domain instead, for example with
an AWS listener rule on the host header that forwards your domain and returns a fixed 404 for anything else.
