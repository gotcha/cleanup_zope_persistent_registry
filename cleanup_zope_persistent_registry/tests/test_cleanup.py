import unittest2 as unittest
import pickle

from cleanup_zope_persistent_registry import cleanup_leftovers
from cleanup_zope_persistent_registry.testing import make_broken_registry


class TestCleanup(unittest.TestCase):

    def test_guts_after_cleanup(self):
        registry = make_broken_registry()
        self.assertTrue(registry.adapters._adapters[1])
        self.assertTrue(registry.adapters._subscribers[1])
        self.assertTrue(registry.utilities._adapters[0])
        cleanup_leftovers(registry)
        self.assertFalse(registry.adapters._adapters[1])
        self.assertFalse(registry.adapters._subscribers[1])
        self.assertFalse(registry.utilities._adapters[0])

    def test_pickle_after_cleanup(self):
        registry = make_broken_registry()
        pickled = pickle.dumps(registry)
        self.assertTrue('IBroken' in pickled)
        cleanup_leftovers(registry)
        pickled = pickle.dumps(registry)
        self.assertFalse('IBroken' in pickled)
