#!/bin/sh
case $1 in
  start) cd /Users/cx/workspace/sophomore && celery -A sophomore worker -B
    --logfile="/Users/cx/workspace/sophomore/celery_scripts/celery_beat_logs.log"
    -l info > out.file 2>&1 & ;;
esac
#    --scheduler django_celery_beat.schedulers:DatabaseScheduler

# python -m celery -A sophomore worker -B -l info
