import datetime

ALOS_DEM_PLATFORM = "Advanced Land Observing Satellite (ALOS)"
ALOS_DEM_INSTRUMENTS = [
    "Panchromatic Remote-sensing Instrument for Stereo Mapping (PRISM)"
]
ALOS_DEM_GSD = 30  # meters
ALOS_DEM_EPSG = 4326

# This stactools package was created to interact with the ALOS DEM data hosted
# on OpenTopography. As of this writing, the data were last updated at this
# time. This information was taken from
# https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.112016.4326.2.
OPENTOPOGRAPHY_DATETIME = datetime.datetime(2016,
                                            12,
                                            7,
                                            tzinfo=datetime.timezone.utc)
