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
	# remove quotes from flyctl env (until https://github.com/superfly/flyctl/issues/589 is resolved)
	flyctl_env_vars+=$(echo "$input_line " | tr -d '"')
done < .env
echo ${flyctl_env_vars[@]}

# set flyctl env secrets
flyctl secrets set --stage ${flyctl_env_vars[@]}

# deploy app with env secrets passed through flyctl to docker
flyctl deploy -a www-babalada-com ${docker_env_vars[@]}
