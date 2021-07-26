import datetime
from unittest import TestCase

from pystac.extensions.projection import ProjectionExtension
from pystac.provider import Provider

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

        common_metadata = item.common_metadata
        self.assertEqual(common_metadata.platform,
                         "Advanced Land Observing Satellite (ALOS)")
        self.assertEqual(common_metadata.instruments, [
            "Panchromatic Remote-sensing Instrument for Stereo Mapping (PRISM)"
        ])
        self.assertEqual(common_metadata.gsd, 30)
        self.assertEqual(common_metadata.providers, [
            Provider("Japan Aerospace Exploration Agency",
                     roles=["producer", "processor", "licensor"],
                     url="https://www.eorc.jaxa.jp/ALOS/en/aw3d30/index.htm"),
            Provider("OpenTopography",
                     roles=["host"],
                     url=("https://portal.opentopography.org/"
                          "raster?opentopoID=OTALOS.112016.4326.2")),
        ])

        projection = ProjectionExtension.ext(item)
        self.assertEqual(projection.epsg, 4326)
        self.assertEqual(projection.shape, (3600, 3600))
        self.assertEqual(list(projection.transform), [
            0.0002777777777777778, 0.0, -106.0, 0.0, -0.0002777777777777778,
            42.0
        ])

        item.validate()

    def test_create_item_with_read_href_modifier(self):
        done = False

        def do_it(href):
            nonlocal done
            done = True
            return href

        _ = stac.create_item(self.path, read_href_modifer=do_it)
        self.assertTrue(done, "Didn't do it")
