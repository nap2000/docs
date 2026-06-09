
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
