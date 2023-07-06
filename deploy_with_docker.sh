#!/bin/bash

# check dependencies are installed
pnpm i

# build UI
pnpm run build

# gather env secrets for flyctl and docker
docker_env_vars=("$@")
flyctl_env_vars=("$@")
while IFS= read -r input_line || [[ -n "$input_line" ]]; do
	input_line=$(echo $input_line)
	docker_env_vars+="--build-secret $input_line "
	flyctl_env_vars+="$input_line "
done < .env

# set flyctl env secrets
flyctl secrets set --stage ${flyctl_env_vars[@]}

# deploy app with env secrets passed through flyctl to docker
flyctl deploy -a www-babalada-com ${docker_env_vars[@]}
