#!/usr/bin/env bash

function usage () {
    echo 'usage: '$(basename $0)' [-h] [-q] [-i {.png,md5sum}] [-t n] [-u <username>] [-p <password>] [{-w,-d,-e,-c}] [--] [PYPOE_ARGS]

options:
  -h, --help            show this help message and exit
  -q, --quiet           hide all non-error messages from pypoe
  -i, --image           process images and convert them to the specified format
  -t, --threads         number of threads that can read wiki pages simultaneously (equivalent to the -w-mt pypoe argument)
  -u, --username        wiki username (if not supplied pypoe will prompt several times during the export)
  -p, --password        wiki password (will be printed to console)

  -w, --write           export to the file system
                      - alias for '$(basename $0)' -- --write

  -d, --dry-run         perform a dry run, comparing changes against the wiki and saving diffs in the output directory
                      - alias for '$(basename $0)' -- --write -w -w-dr -w-d

  -e, --export          perform a full export to the wiki
                      - alias for '$(basename $0)' -i .png -- -w -w-pc

  -c, --cache           perform a null edit and cache purge of every page managed by the exporter
                      - alias for '$(basename $0)' -- -w -w-dr -w-pc all'
}


VALID_ARGS=$(getopt -o hqi:t:u:p:wdec --long help,quiet,image:,threads:,username:,password:,write,dry-run,export,cache -- "$@")
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
    -t | --threads)
        ARGS+=(-w-mt $2)
        shift 2
        ;;
    -u | --username)
        ARGS+=(-w-u $2)
        shift 2
        ;;
    -p | --password)
        ARGS+=(-w-pw $2)
        shift 2
        ;;
    -w | --write)
        ARGS+=(--write)
        shift
        ;;
    -d | --dry-run)
        ARGS+=(--write -w -w-dr -w-d)
        shift
        ;;
    -e | --export)
        ARGS+=(-w -w-pc)
        IMG=(--store-images --convert-images)
        SKIP_ICON_EXPORT=
        shift
        ;;
    -c | --cache)
        ARGS+=(-w -w-dr -w-pc all)
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
    --)
        shift
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
