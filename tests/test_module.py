import unittest

import stactools.alos_dem


class TestModule(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(stactools.alos_dem.__version__)
