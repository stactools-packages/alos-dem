# stactools-alos-dem

- Name: alos-dem
- Package: `stactools.alos_dem`
- PyPI: https://pypi.org/project/stactools-alos-dem/
- Owner: @gadomski
- Dataset homepages:
  - https://www.eorc.jaxa.jp/ALOS/en/aw3d30/index.htm
  - https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.112016.4326.2
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
- Extra fields: none

This data set is a global digital surface model (DSM) with horizontal resolution of approximately 30 meters (basically 1 arcsecond) by the Panchromatic Remote-sensing Instrument for Stereo Mapping (PRISM), which was an optical sensor on board the Advanced Land Observing Satellite "ALOS".

(from https://www.eorc.jaxa.jp/ALOS/en/aw3d30/index.htm)

[![CI](https://github.com/stactools-packages/alos-dem/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/stactools-packages/alos-dem/actions/workflows/continuous-integration.yml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/stactools-packages/alos-gap/main?filepath=docs/installation_and_basic_usage.ipynb)
## Examples

### STAC objects

- [Item](examples/ALPSMLC30_N041W106_DSM.json)

### Command-line usage

Description of the command line functions

```bash
$ stac alos-dem create-item ALPSMLC30_N041W106_DSM.tif ALPSMLC30_N041W106_DSM.json
```

Use `stac package --help` to see all subcommands and options.
