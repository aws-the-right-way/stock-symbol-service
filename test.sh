#!/bin/bash

COUNT=60 #number of 10 second timeouts in 10 minutes

while [[ $COUNT -ge "0" ]]; do
  #send the request, put response in variable
  DATA=$(wget -O - -q -t 1 http://127.0.0.1:8080/api/ping)

  if [ "$DATA" == "OK" ]; then
    echo "Pinged OK"
    exit 0
  else
    echo "ERROR: Couldn't retrieve PING response. Server responded -- $DATA"
    exit 1
  fi
done
