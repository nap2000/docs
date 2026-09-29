.. _whatsapp-server-admin:

Set up WhatsApp
===============

.. contents::
 :local:

WhatsApp can be connected through Vonage, or from Smap Server version 26.10, directly to Meta using the WhatsApp Cloud API.
If both are set up, WhatsApp messages are sent through Meta.

Vonage
------

Requires Smap Server version 24.09+.

#.  Create an account on Vonage, https://www.vonage.com/
#.  Login to "Communication APIs"
#.  Select "External Accounts" and then select "Set up my WhatsApp business account"
#.  Logon to Facebook
#.  Enter your business information and press "Next"
#.  Leave the default options of creating a whatsapp business account and profile and press "Next"
#.  Fill in your profile and press "Next"
#.  Enter the whatsapp number for your business account (Note I had to use a new number for this account.  You can use a number with an
    existing whatsApp account associated to it but you will need to delete that account first)

#.  You can then continue to connect your whatsApp number to Vonage

    *  Select the phone number that has the whats app account
    *  Select your API key, this is probably the one you set up for SMS
    *  Select get my WhatsApp number live
    *  Follow the prompts

.. _whatsapp-meta:

Meta WhatsApp Cloud API
-----------------------

Requires Smap Server version 26.10+.  This connects your WhatsApp business number directly to Meta, without a middleware
provider.

#.  In Meta for Developers, https://developers.facebook.com, create an app of type "Business" and add the **WhatsApp** product
#.  Add your business phone number to the app.  Note the **Phone number ID** that Meta shows for it
#.  Create a permanent access token for a system user in Meta Business Settings, with the ``whatsapp_business_messaging``
    permission.  Temporary tokens expire after a day
#.  From the app's basic settings, copy the **App Secret**
#.  In Smap, as the server owner, open **Admin > Settings > Server** and under **WhatsApp - Meta Cloud API** enter:

    *  WhatsApp Access Token.  The permanent token
    *  WhatsApp App Secret
    *  WhatsApp Webhook Verify Token.  Make up a value, for example a long random string
    *  API Version.  Optional, the Graph API version to use.  Defaults to v21.0

#.  In the WhatsApp configuration in Meta, set up the webhook:

    *  Callback URL: https://{your server}/sms/whatsapp/inbound
    *  Verify token: the same value you entered in Smap

    Meta checks the URL straight away, so save the Smap settings first.  Then subscribe to the **messages** field

#.  Add the number in Smap, see :ref:`sms`.  Set the channel to WhatsApp and enter the **WhatsApp Phone Number Id** from
    step 2.  The number is not used to send messages through Meta without this id

Inbound messages are only accepted if Meta has signed them with the App Secret.

.. note::

  WhatsApp only lets a business send a free text message within 24 hours of the customer's last message to it.  Outside
  that window Meta rejects the message and the error is shown in the notification log.
