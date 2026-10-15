FROM alpine:3.20

VOLUME ["/volume-proof"]

CMD ["sh", "-c", "printf 'container=%s\n' \"$HOSTNAME\" > /volume-proof/container.txt; if [ \"${FAIL_ON_START:-0}\" = \"1\" ]; then echo 'intentional test failure' >&2; exit 42; fi; while :; do sleep 3600; done"]
