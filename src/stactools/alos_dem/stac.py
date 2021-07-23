from typing import Optional

from pystac import Item

from stactools.core.io import ReadHrefModifier


def create_item(href: str,
                read_href_modifer: Optional[ReadHrefModifier] = None) -> Item:
    """Creates a STAC Item from a single tile of ALOS DEM data."""
