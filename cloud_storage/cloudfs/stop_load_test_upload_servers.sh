#!/bin/bash
for pid in $(ps -ef | awk '/load_test/ {print $2}'); do kill -9 $pid; done
