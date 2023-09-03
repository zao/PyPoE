#!/usr/bin/env bash

function usage () {
    echo 'usage: '$(basename $0)' [-h] [-q] [-i {.png,md5sum}] [--] [PYPOE_ARGS]

options:
  -h, --help            show this help message and exit
  -q, --quiet           hide all non-error messages from pypoe
  -i, --image           process images and convert them to the specified format

  -w, --write           export to the file system
                      - alias for '$(basename $0)' -- --write

  -d, --dry-run         perform a dry run, comparing changes against the wiki
                      - alias for '$(basename $0)' -- --write -w -w-dr -w-d -w-mt 8 -w-u "$POEWIKI_USER" -w-pw "$POEWIKI_PASS"
                      - if $POEWIKI_USER and $POEWIKI_PASS are not set you will be prompted several times by the exporter

  -e, --export          perform a full export to the wiki
                      - alias for '$(basename $0)' -i .png -- -w -w-pc -w-mt 8 -w-u "$POEWIKI_USER" -w-pw "$POEWIKI_PASS"

  -p, --purge-cache     perform a null edit and cache purge of every page managed by the exporter
                      - alias for '$(basename $0)' -- -w -w-dr -w-pc all -w-mt 8 -w-u "$POEWIKI_USER" -w-pw "$POEWIKI_PASS"'
}


VALID_ARGS=$(getopt -o i:wdepqh --long image:,write,dry-run,export,purge-cache,quiet,help -- "$@")
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
          IMG=(--store-images --convert-images)
          SKIP_ICON_EXPORT=
        elif [[ $2 == md5sum ]]
        then
          IMG=(--store-images --convert-images=md5sum)
        elif [[ $2 == .* ]]
        then
          IMG=(--store-images --convert-images="$2")
        else
          echo "Error: $2 is not a file extension"
          echo
          usage
          exit 1
        fi
        shift 2
        ;;
    -w | --write)
        ARGS=(--write)
        shift
        ;;
    -d | --dry-run)
        ARGS=(--write -w -w-dr -w-d -w-mt 8)
        if [[ -n "$POEWIKI_USER" ]]; then
          ARGS+=(-w-u $POEWIKI_USER)
        fi
        if [[ -n "$POEWIKI_PASS" ]]; then
          ARGS+=(-w-pw "$POEWIKI_PASS")
        fi
        shift
        ;;
    -e | --export)
        ARGS=(-w -w-pc -w-mt 8)
        if [[ -n "$POEWIKI_USER" ]]; then
          ARGS+=(-w-u $POEWIKI_USER)
        fi
        if [[ -n "$POEWIKI_PASS" ]]; then
          ARGS+=(-w-pw "$POEWIKI_PASS")
        fi
        IMG=(--store-images --convert-images)
        SKIP_ICON_EXPORT=
        shift
        ;;
    -p | --purge-cache)
        ARGS=(-w -w-dr -w-pc all -w-mt 8)
        if [[ -n "$POEWIKI_USER" ]]; then
          ARGS+=(-w-u $POEWIKI_USER)
        fi
        if [[ -n "$POEWIKI_PASS" ]]; then
          ARGS+=(-w-pw "$POEWIKI_PASS")
        fi
        IMG=(--store-images --convert-images)
        SKIP_ICON_EXPORT=
        shift
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

pypoe_exporter $QUIET wiki items item rowid "${IMG[@]}" "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki passive rowid "${IMG[@]}" "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki mastery effects rowid "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki mastery groups rowid "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki mods mods rowid "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki monster rowid "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki area rowid "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki skill by_name "${IMG[@]}" "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki incursion rooms rowid "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua bestiary "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua blight "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua crafting_bench "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua delve "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua harvest "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua heist "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua monster "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua pantheon "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua synthesis "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua ot "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki lua minimap "${ARGS[@]}" "$@"
$SKIP_ICON_EXPORT
pypoe_exporter $QUIET wiki items maps --store-images --convert-images=.png "${ARGS[@]}" "$@"
pypoe_exporter $QUIET wiki items atlas_icons --store-images --convert-images=.png "${ARGS[@]}" "$@"
