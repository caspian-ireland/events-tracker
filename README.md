[![License](https://img.shields.io/badge/License-GPLv3-blue)](#license)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# Events Tracker

Events Tracker is a simple Flask app that helps users to search for events listed on event management and ticketing sites and then track changes to those events.

1. User registers search patterns using keywords.
2. Matching events are presented to user for approval/dismissal.
3. Event tracker will notify the user if approved events are updated/changed on the source website.

**Note:** This project is in the early stages of development.

## Project Status
Project is: _in progress_

## Roadmap

 * Establish a POC version that pulls events from eventbrite API
 * Refactor
 * Automated testing
 * Logging
 * User/Groups management
 * WSGI and app packaging
 * Additional event sources


## Guide

This project is still in development and is not ready for distribution. However to get a local development server running, you can try the following:

* I'm running Python 3.11.1, though earlier versions _may_ work
* Clone this repository
* Open a terminal and move to the root of the project directory.
* Install dependencies using `pip install -r requirements.txt`
* Configure environment variables. See file `example.env`
* Install `npm` and run `npm install --prefix ./eventstracker/static`
* Run the command `flask run`.

## Contributing

Not accepting code contributions until an initial working version has been released.
Please feel free to submit suggestions via an
https://github.com/caspian-ireland/events-tracker/labels/enhancement issue.


## Code Style

[Black](https://github.com/psf/black)

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) or later.
