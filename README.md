# Making Maps for the City of San Francisco and Code for America :heart: :us:

 ## How you can join:
* Test prototype: http://sfmta.xtreet.org/resolutions-map
* Get on [Slack](http://c4sf.me/slack)
  * Add prj-sf-trip4SF as a channel
* Get on [GitHub](http://c4sf.me/joingithub)
  * Find sfbrigade/sfmta-board-resolutions
* Visit Google Drive folder: https://drive.google.com/drive/folders/0B_zAxkoAf-U6NGY1Zlk4UDl2Z28
* Attend [Code for San Francisco](http://codeforsanfrancisco.org/events) hack nights on Wednesdays from 6-9

### Setup/Installation

Install requirements to run locally.

Clone repository:

```sh
$ git clone https://github.com/geosphere-io/resolution_alert_map.git
```
Move into folder.

```sh
$ cd resolution_alert_map
```
Create virtual environment:

```sh
$ virtualenv env
```
Activate virtual environment:

```sh
$ source env/bin/activate
```
Install dependencies:

```sh
$ pip install -r requirements.txt
```
Gather necessary secret keys from Mapbox and Flask. Save to your secrets file. Link to server.py.

Database

```sh
$ createdb resolutions
```
```sh
$ psql resolutions
```
```sh
$ >>> CREATE EXTENSION postgis;
```
Create the models and tables.
```sh
$ python -i model.py
```
