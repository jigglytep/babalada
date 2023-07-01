#!/bin/bash

# check dependencies are installed
pnpm i

# build UI
pnpm run build

# gather env secrets for fly
env_vars=("$@")
while IFS= read -r input_line || [[ -n "$input_line" ]]; do
	input_line=$(echo $input_line)
	env_vars+=" --build-secret $input_line"
done < .env
echo "${env_vars[@]}"

# deploy app with env secrets passed to Docker
flyctl deploy -a www-babalada-com ${env_vars[@]}
