#!/bin/bash

# Donwload first geojson export from http://overpass-turbo.eu/s/s5W

rm data/*

jq -r '.features | map(select(.properties.ref)) | .[].properties.ref' export.geojson | sort -n | uniq | while read N; do

echo $N

jq ".features |
[
  (
    map(select(.properties.ref == \"$N\")) |
    map({type: .type, geometry: .geometry, properties: {name: .properties.name, attributes: {operator: .properties.operator, to: .properties.to, from: .properties.from, ref: .properties.ref, network: .properties.network}}})
  ),
  (
    map(select(select(.properties[\"@relations\"]) | .properties[\"@relations\"] | select(.[].reltags.ref == \"$N\") | any)) |
    map({type: .type, geometry: .geometry, properties: {name: .properties.name, attributes: {official_status: \"none\"}}})
  )
] |
[.[][]] |
{type: \"FeatureCollection\", features: .}
" export.geojson > data/$N.geojson

done
