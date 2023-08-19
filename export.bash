#!/usr/bin/env bash

function usage () {
    echo 'usage: '$(basename $0)' [-h] [-q] [-i {.png,md5sum}] [--] [PYPOE_ARGS]

options:
  -h, --help            show this help message and exit
  -q, --quiet           hide all non-error messages from pypoe
  -i, --image           process images and convert them to the specified format

export to the file system:
  '$(basename $0)' -q --write
to perform a dry run comparing changes against the wiki:
  '$(basename $0)' --write -w -w-dr -w-d -w-mt 8 -w-u $USERNAME -w-pw $PASSWORD
to perform a full export:
  '$(basename $0)' -i .png -- -w -w-mt 8 -w-u $USERNAME -w-pw $PASSWORD'
}


VALID_ARGS=$(getopt -o i:qh --long image:,quiet,help -- "$@")
if [[ $? -ne 0 ]]; then
    usage
    exit $?;
fi
SKIP_ICON_EXPORT=exit
eval set -- "$VALID_ARGS"
while [[ $# -gt 0 ]]; do
  case "$1" in
    -i | --image)
        if [[ $2 == .png ]]
        then
          IMG="--store-images --convert-images"
          SKIP_ICON_EXPORT=
        elif [[ $2 == md5sum ]]
        then
          IMG="--store-images --convert-images=md5sum"
        elif [[ $2 == .* ]]
        then
          IMG="--store-images --convert-images=$2"
        else
          echo "Error: $2 is not a file extension"
          echo
          usage
          exit 1
        fi
        shift 2
        ;;
    -q | --quiet)
        QUIET=--quiet
        shift
        ;;
    -h | --help)
        usage
        exit
        shift
        ;;
    --) shift;
        break
        ;;
  esac
done

set -x

pypoe_exporter setup perform

pypoe_exporter $QUIET wiki items item rowid $IMG "$@"
pypoe_exporter $QUIET wiki passive rowid $IMG "$@"
pypoe_exporter $QUIET wiki skill by_row $IMG "$@"
pypoe_exporter $QUIET wiki incursion rooms rowid "$@"
pypoe_exporter $QUIET wiki area rowid "$@"
pypoe_exporter $QUIET wiki lua bestiary "$@"
pypoe_exporter $QUIET wiki lua blight "$@"
pypoe_exporter $QUIET wiki lua crafting_bench "$@"
pypoe_exporter $QUIET wiki lua delve "$@"
pypoe_exporter $QUIET wiki lua harvest "$@"
pypoe_exporter $QUIET wiki lua heist "$@"
pypoe_exporter $QUIET wiki lua monster "$@"
pypoe_exporter $QUIET wiki lua pantheon "$@"
pypoe_exporter $QUIET wiki lua synthesis "$@"
pypoe_exporter $QUIET wiki lua ot "$@"
pypoe_exporter $QUIET wiki lua minimap "$@"
pypoe_exporter $QUIET wiki mastery effects rowid "$@"
pypoe_exporter $QUIET wiki mastery groups rowid "$@"
pypoe_exporter $QUIET wiki monster rowid "$@"
$SKIP_ICON_EXPORT
pypoe_exporter $QUIET wiki items maps --store-images --convert-images=.png "$@"
pypoe_exporter $QUIET wiki items atlas_icons --store-images --convert-images=.png "$@"
