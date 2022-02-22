# Change Log

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v0.1.5] - 2022-02-22

### Added

- Added the [sentry](https://sentry.io) error tracking capability

### Changed

- Fixed [`requirements.txt`](requirements.txt) items versions

## [v0.1.4] - 2021-09-17

### Changed

- Multiple header fields to export instead of one
- Enhanced runtime performance

## [v0.1.3] - 2021-09-08

### Fixed

- Fixed delay between messages

## [v0.1.2] - 2021-09-08

### Added

- Added topic and service name to the metrics

### Fixed

- Added `PYTHONUNBUFFERED=1` to the `Dockerfile` to fix fetching logs in the
  Kubernetes

## [v0.1.1] - 2021-09-07

### Fixed

- Handled some exceptions

## [v0.1.0] - 2021-09-06

### Added

- Initial version
