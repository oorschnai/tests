FROM alpine:3.20

RUN mkdir -p /srv/www \
    && printf '%s\n' 'anonymous volume cleanup probe' > /srv/www/index.html

VOLUME ["/volume-proof"]

EXPOSE 8080

CMD ["sh", "-c", "printf 'container=%s\n' \"$HOSTNAME\" > /volume-proof/container.txt; if [ \"${FAIL_ON_START:-0}\" = \"1\" ]; then echo 'intentional test failure' >&2; exit 42; fi; exec httpd -f -p 8080 -h /srv/www"]
