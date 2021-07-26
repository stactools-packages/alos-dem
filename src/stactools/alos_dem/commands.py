import click

from stactools.alos_dem import stac


def create_alos_dem_command(cli):
    """Creates the ALOS DEM stactools commands."""
    @cli.group("alos-dem", short_help="Work with ALOS DEM data.")
    def alos_dem():
        pass

    @alos_dem.command("create-item",
                      short_help="Creates a STAC item from an ALOS DEM tile.")
    @click.argument("source")
    @click.argument("destination")
    @click.option("--validate/--no-validate",
                  default=True,
                  help="Validate the item before saving")
    def create_item_command(source, destination, validate):
        item = stac.create_item(source)
        if validate:
            item.validate()
        item.save_object(dest_href=destination)

    return alos_dem
