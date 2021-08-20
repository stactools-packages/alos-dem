# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). This project attempts to match the major and minor versions of [stactools](https://github.com/stac-utils/stactools) and increments the patch number as needed.

## [v0.1.2] - 2021-08-20

### Fixed

- Moved s3 to be a dev dependency only ([#6](https://github.com/stactools-packages/alos-dem/pull/6)).
  Includes a manual pin of the **aiobotocore** version to work around https://github.com/dask/s3fs/pull/510, which should be reverted once that PR is released.

## [v0.1.1] - 2021-08-02

### Added

- Nothing.

### Deprecated

- Nothing.

### Removed

- Nothing.

### Fixed

- Aligned platform and instruments fields with best practices.

## [v0.1.0] - 2021-07-29

The initial release of this package.
### Added

- Everything.

### Deprecated

- Nothing.

### Removed

- Nothing.

### Fixed

- Nothing.
