import datetime

from pystac import Provider, Link

ALOS_DEM_PLATFORM = "alos"
ALOS_DEM_INSTRUMENTS = ["prism"]
ALOS_DEM_GSD = 30  # meters
ALOS_DEM_EPSG = 4326
ALOS_DEM_PROVIDERS = [
    Provider("Japan Aerospace Exploration Agency",
             roles=["producer", "processor", "licensor"],
             url="https://www.eorc.jaxa.jp/ALOS/en/aw3d30/index.htm"),
    Provider("OpenTopography",
             roles=["host"],
             url=("https://portal.opentopography.org/"
                  "raster?opentopoID=OTALOS.112016.4326.2")),
]
ALOS_DEM_LINKS = [
    Link("handbook",
         "https://www.eorc.jaxa.jp/ALOS/en/doc/alos_userhb_en.pdf",
         "application/pdf",
         "ALOS User handbook",
         extra_fields={"description": "Also includes data usage information"})
]

# This stactools package was created to interact with the ALOS DEM data hosted
# on OpenTopography. As of this writing, the data were last updated at this
# time. This information was taken from
# https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.112016.4326.2.
OPENTOPOGRAPHY_DATETIME = datetime.datetime(2016,
                                            12,
                                            7,
                                            tzinfo=datetime.timezone.utc)
