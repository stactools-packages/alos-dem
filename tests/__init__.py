from stactools.testing import TestData

test_data = TestData(
    __file__, {
        "ALPSMLC30_N041W106_DSM.tif": {
            "url":
            "s3://raster/AW3D30/AW3D30_global/ALPSMLC30_N041W106_DSM.tif",
            "s3": {
                "anon": True,
                "client_kwargs": {
                    "endpoint_url": "https://opentopography.s3.sdsc.edu",
                }
            }
        }
    })
