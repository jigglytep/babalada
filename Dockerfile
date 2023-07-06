# create docker image from ubuntu base with bullseye slim node runtime dependencies
# SOURCE: https://github.com/BretFisher/nodejs-rocks-in-docker
FROM node:20.2.0-bullseye-slim AS node
FROM ubuntu:focal-20230412 AS base
RUN apt-get update && apt-get install -y python3-pip curl
# COPY . /app
COPY --from=node /usr/local/include/ /usr/local/include/
COPY --from=node /usr/local/lib/ /usr/local/lib/
COPY --from=node /usr/local/bin/ /usr/local/bin/
# refresh corepack to fix simlinks for npx, yarn, & pnpm
RUN corepack disable && corepack enable
# create server group & node user, then create app directory
RUN groupadd --gid 1000 server \
	&& useradd --uid 1000 --gid server --shell /bin/bash --create-home node \
	&& mkdir /app \
	&& chown -R node:server /app

# create prod environment
FROM base AS prod
# move to app directory as user node
WORKDIR /app
USER node
COPY pnpm-lock.yaml package.json ./

# install app dependencies
RUN pnpm i
# build UI
RUN pnpm run build

# install pnpm
RUN curl https://get.pnpm.io/install.sh | sh -
RUN pnpm install --prod
COPY requirements.txt ./
RUN pip3 install -r /app/requirements.txt
# copy app files
COPY build build
COPY package.json ./
COPY server server
COPY start_servers.sh ./

# start servers
ENV HOST 0.0.0.0
ENV PORT 8080
EXPOSE 8080
ENV FLASK_APP=server
EXPOSE 5000
CMD ["/app/start_servers.sh"]
