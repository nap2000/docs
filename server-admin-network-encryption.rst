
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
