import datetime

# This stactools package was created to interact with the ALOS DEM data hosted
# on OpenTopography. As of this writing, the data were last updated at this
# time. This information was taken from
# https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.112016.4326.2.
OPENTOPOGRAPHY_DATETIME = datetime.datetime(2016,
                                            12,
                                            7,
                                            tzinfo=datetime.timezone.utc)
