import os.path
from typing import Optional
from pystac.extensions.projection import ProjectionExtension

import rasterio
from shapely.geometry import mapping, box
from pystac import Item

from stactools.core.io import ReadHrefModifier
from stactools.alos_dem.constants import (ALOS_DEM_LINKS, ALOS_DEM_PROVIDERS,
                                          OPENTOPOGRAPHY_DATETIME,
                                          ALOS_DEM_PLATFORM,
                                          ALOS_DEM_INSTRUMENTS, ALOS_DEM_GSD,
                                          ALOS_DEM_EPSG)


def create_item(href: str,
                read_href_modifer: Optional[ReadHrefModifier] = None) -> Item:
    """Creates a STAC Item from a single tile of ALOS DEM data."""
    if read_href_modifer:
        modified_href = read_href_modifer(href)
    else:
        modified_href = href
    with rasterio.open(modified_href) as dataset:
        if dataset.crs.to_epsg() != 4326:
            raise ValueError(
                f"Dataset {href} is not EPSG:4326, which is required for ALOS DEM data"
            )
        bbox = dataset.bounds
        geometry = mapping(box(*bbox))
        transform = dataset.transform
        shape = dataset.shape
    item = Item(id=os.path.splitext(os.path.basename(href))[0],
                geometry=geometry,
                bbox=bbox,
                datetime=OPENTOPOGRAPHY_DATETIME,
                properties={},
                stac_extensions={})

    item.add_links(ALOS_DEM_LINKS)
    item.common_metadata.platform = ALOS_DEM_PLATFORM
    item.common_metadata.instruments = ALOS_DEM_INSTRUMENTS
    item.common_metadata.gsd = ALOS_DEM_GSD
    item.common_metadata.providers = ALOS_DEM_PROVIDERS
    item.common_metadata.license = "proprietary"

    projection = ProjectionExtension.ext(item, add_if_missing=True)
    projection.epsg = ALOS_DEM_EPSG
    projection.transform = transform[0:6]
    projection.shape = shape

    return item
