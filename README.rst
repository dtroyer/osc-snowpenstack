================
osc-snowpenstack
================

OpenStackClient reference transoprtation plugin module

The OSC plugin system is designed so that the plugin need only be
properly installed for OSC to find and use it.  It utilizes the
``setuptools`` entry points mechanism to advertise to OSC the
plugin module and supported commands.

**osc-snowpenstack** is an OpenStackClient (OSC) plugin implementation that
demonstrates the effect of snow during an OpenStack event on
developer productivity via OSC's extension mechanism.  It adds
two commands: ``flight list`` and ``flight show``.

Images taken from `ascii-art.de`_ and other sources.

.. _`ascii-art.de`: http://www.ascii-art.de/ascii/t/train.txt
