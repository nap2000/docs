.. _quotes:

Double and Single Quotes
========================

.. contents::
 :local:
 
You will often need to use quotation marks in your surveys and it is usually important that these not be left and right quotes.

.. note::

  This is not an issue when writing the label text for a question.

For example when specifying a pulldata function you may write::

  if(concat(${country}, ${city_code}) = '', '', pulldata('cities', 'city_label', "#{country} = ${country} and #{city} = ${city_code}"))

If you do this in a spreadsheet editor, the editor may convert the double quotes (") or the single quotes (') into left and right versions
of quotes.  These look nicer in a printable document but will confuse Smap.  If this happens you can change the settings in your editor to
not auto correct to left and right quotes.
