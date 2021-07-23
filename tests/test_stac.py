import datetime
from unittest import TestCase

from stactools.alos_dem import stac

from tests import test_data


class StacTest(TestCase):
    def setUp(self):
        self.path = test_data.get_external_data("ALPSMLC30_N041W106_DSM.tif")

    def test_create_item(self):
        item = stac.create_item(self.path)
        self.assertEqual(item.id, "ALPSMLC30_N041W106_DSM")
        self.assertIsNotNone(item.geometry)
        self.assertEqual(list(item.bbox), [-106.0, 41.0, -105.0, 42.0])
        self.assertEqual(
            item.datetime,
            datetime.datetime(2016, 12, 7, tzinfo=datetime.timezone.utc))
        item.validate()

    def test_create_item_with_read_href_modifier(self):
        done = False

        def do_it(href):
            nonlocal done
            done = True
            return href

        _ = stac.create_item(self.path, read_href_modifer=do_it)
        self.assertTrue(done, "Didn't do it")
