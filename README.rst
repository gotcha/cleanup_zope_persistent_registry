cleanup_zope_persistent_registry
================================

Before 3.5.2, ``zope.interface`` was broken :
it did not remove keys when unregistering adapters or unsubscribing
subscribers.

This implies that even when proper unregistration of adapters and subscribers
had been done, interfaces were left over, pickled in persistent registries.

This leads to nasty bugs when the code that defined those interfaces is removed
from the system.

This package defines a function that cleans up those leftover interfaces.
It must be called on a ``PersistentAdapterRegistry`` like the one
that is instantiated in the local site manager of a Plone site::

  from zope.component import getSiteManager
  from cleanup_zope_persistent_registry import cleanup_leftovers

  site_manager = getsitemanager(my_plone_site)
  cleanup_leftovers(site_manager)

 	
Tested
------

.. image:: https://secure.travis-ci.org/gotcha/cleanup_zope_persistent_registry.png?branch=master
   :target: http://travis-ci.org/#!/gotcha/cleanup_zope_persistent_registry
