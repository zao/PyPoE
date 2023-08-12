#!/usr/bin/env bash

set -x

pypoe_exporter setup perform

pypoe_exporter --quiet wiki items item rowid --store-images --convert-images "$@"
pypoe_exporter --quiet wiki items maps --store-images --convert-images "$@"
pypoe_exporter --quiet wiki items atlas_icons --store-images --convert-images "$@"
pypoe_exporter --quiet wiki passive rowid --store-images --convert-images "$@"
pypoe_exporter --quiet wiki incursion rooms rowid "$@"
pypoe_exporter --quiet wiki area rowid "$@"
pypoe_exporter --quiet wiki lua atlas "$@"
pypoe_exporter --quiet wiki lua bestiary "$@"
pypoe_exporter --quiet wiki lua blight "$@"
pypoe_exporter --quiet wiki lua crafting_bench "$@"
pypoe_exporter --quiet wiki lua delve "$@"
pypoe_exporter --quiet wiki lua harvest "$@"
pypoe_exporter --quiet wiki lua heist "$@"
pypoe_exporter --quiet wiki lua monster "$@"
pypoe_exporter --quiet wiki lua pantheon "$@"
pypoe_exporter --quiet wiki lua synthesis "$@"
pypoe_exporter --quiet wiki lua ot "$@"
pypoe_exporter --quiet wiki lua minimap "$@"
pypoe_exporter --quiet wiki skill by_row --store-images --convert-images "$@"
pypoe_exporter --quiet wiki mastery effects rowid "$@"
pypoe_exporter --quiet wiki mastery groups rowid "$@"
pypoe_exporter --quiet wiki monster rowid "$@"
