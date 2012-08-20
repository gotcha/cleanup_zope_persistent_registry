from zope.interface import Interface
from zope.component.persistentregistry import PersistentComponents


class IBroken(Interface):
    pass


def factory(value):
    return value


def make_broken_registry():
    persistent = PersistentComponents('persistent')
    persistent.registerAdapter(factory, (Interface,), IBroken)
    persistent.unregisterAdapter(factory, (Interface,), IBroken)
    persistent.registerUtility(factory, IBroken)
    persistent.unregisterUtility(factory, IBroken)
    persistent.registerHandler(factory, (IBroken,))
    persistent.unregisterHandler(factory, (IBroken,))
    return persistent
