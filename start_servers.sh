#!/bin/bash

# Start the first process
python3 -m flask run --host=0.0.0.0 --port=5000 &
# Start the second process
/usr/local/bin/node ./build &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?