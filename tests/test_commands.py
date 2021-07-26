import os.path
from tempfile import TemporaryDirectory

import pystac
from stactools.testing import CliTestCase

from stactools.alos_dem import commands
from tests import test_data


class CreateItemTest(CliTestCase):
    def create_subcommand_functions(self):
        return [commands.create_alos_dem_command]

    def test_create_item(self):
        infile = test_data.get_external_data("ALPSMLC30_N041W106_DSM.tif")
        with TemporaryDirectory() as temporary_directory:
            outfile = os.path.join(temporary_directory, "item.json")
            args = ["alos-dem", "create-item", infile, outfile]
            result = self.run_command(args)
            self.assertEqual(result.exit_code, 0)
            item = pystac.read_file(outfile)
            item.validate()
