#!/bin/sh
cd /etc/nginx/conf.d
if [ "${HOST+foo}" ]; then
  export HOST=$HOST
else
  export HOST=localhost
fi

envsubst '$$HOST'< default.conf.template > default.conf
nginx -g "daemon off;"