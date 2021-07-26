import os.path
from typing import Optional
from pystac.extensions.projection import ProjectionExtension

import rasterio
from rasterio.windows import transform
from shapely.geometry import mapping, box
from pystac import Item

from stactools.core.io import ReadHrefModifier
from stactools.alos_dem.constants import OPENTOPOGRAPHY_DATETIME


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

    projection = ProjectionExtension.ext(item, add_if_missing=True)
    projection.epsg = 4326
    projection.transform = transform[0:6]
    projection.shape = shape

    return item
