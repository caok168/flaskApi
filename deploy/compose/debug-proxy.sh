#!/bin/bash

socat TCP4-LISTEN:5432,reuseaddr,fork TCP4:postgres_test:5432 &
socat TCP4-LISTEN:6380,reuseaddr,fork TCP4:redis:6379 &
socat TCP4-LISTEN:4222,reuseaddr,fork TCP4:nats:4222 &
socat TCP4-LISTEN:8222,reuseaddr,fork TCP4:nats:8222 &
socat TCP4-LISTEN:8086,reuseaddr,fork TCP4:influxdb:8086 &
socat TCP4-LISTEN:8888,reuseaddr,fork TCP4:chronograf:8888 &


tail -f /dev/null