# Rutas web site for Accra, Ghana

This is an interactive map of the public transport in Accra, Ghana. See it live at http://junglebus.io/accra

This project has been developed by [Jungle Bus](http://junglebus.io/) as part of the [Accra Mobile 3](Thttps://wiki.openstreetmap.org/wiki/AccraMobile3) project.

It is a fork of the interactive map made by the Nicaraguan community in Managua : https://github.com/mapanica/rutas


## Generate geojson routes

Donwload first geojson export from http://overpass-turbo.eu/s/s5W
Or from this overpass code:

    [out:json];
    // fetch area “ghana” to search in
    {{geocodeArea:Greater Accra Region}}->.searchArea;
    (
      // query part for: “type=route and bus=unofficial”
      node["type"="route"]["bus"="unofficial"](area.searchArea);
      way["type"="route"]["bus"="unofficial"](area.searchArea);
      relation["type"="route"]["bus"="unofficial"](area.searchArea);
    
      node["public_transport"="platform"](area.searchArea);
      way["public_transport"="platform"](area.searchArea);
      relation["public_transport"="platform"](area.searchArea);
    );
    // print results
    out body;
    >;
    out skel qt;

Then convert the export to one geojson per line:

    cd extra
    ./generate-geojson.sh


## Generate HTML web site

### Prerequisites

Install `pelican`(https://blog.getpelican.com/).

### Generate

To generate and run a demo server with autoreload:

    develop_server.sh start

In `pelicanconf.py` and `publishconf.py` change `SITEURL` to test in local.

Then visit: http://localhost:8000
