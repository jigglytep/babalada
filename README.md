Babalada
===
A stock investment simulator
---
Developed between June 7, 2023 and July 24, 2023.

Babalada uses data from the real stock market to provide a realistic trading environment with risk management tools, a social platform (forum), and performance evaluation metrics to help users assess and improve their stock trading skills.

This is a website built with [SvelteKit], [Typescript], & [Sass] to compile a html/css/js application delivered by a [Python 3] server. [Docker] is used to deploy the server within a minified [Ubuntu] environment. SvelteKit dependencies are managed by [pnpm], while Python dependencies are managed by [pip]. The Docker container is to be hosted by [fly] at https://babalada.com.

### Install Dependencies
* [Install pnpm].
* [Install Python 3].
* Clone this repository to your computer.
* Run `pnpm i` to install UI dependencies.

### Development Scripts
To run a script, type `pnpm run <script-name>` in a terminal within the root folder.

| script-name | description |
|:----------- |:----------- |
| `dev` | create a local hot-reloading server at [localhost:5173](http://localhost:5173) for development purposes |
| `build` | compile a production version of the app into the build folder |
| `preview` | create a local server which serves the contents of the build folder at [localhost:5173](http://localhost:4173) |
| `check` | evaluate Svelte syntax |
| `check:watch` | re-evaluate Svelte syntax when files are updated |

### Build Server
* Install Dependencies.
* Run `python -m venv venv`
* Run `source venv/bin/activate`
* Run `pip install -r python-packages.txt` to install server dependencies.
* TODO

### Build App
* Install Dependencies.
* TODO

### Deploy App
* Build App.
* [Install flyctl]
* TODO

[SvelteKit]: https://kit.svelte.dev/docs/introduction
[Typescript]: https://www.typescriptlang.org/why-create-typescript
[Sass]: https://sass-lang.com/guide
[Python 3]: https://www.python.org/
[Install Python 3]: https://www.python.org/downloads/
[Docker]: https://docs.docker.com/get-started/overview/
[Ubuntu]: https://ubuntu.com/about
[pnpm]: https://pnpm.io/motivation
[pip]: https://pypi.org/project/pip/
[Install pnpm]: https://pnpm.io/installation
[fly]: https://fly.io/docs/
[install flyctl]: https://fly.io/docs/hands-on/install-flyctl/

# TODO: remove the following notes

Login Tutorial for refrence
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

## Steps to set up local environment

    FLASK_APP=auth

    PG_PASSWD=<PASSWORD>

    PG_USR=<USERNAME>

    PG_URL=<URL>

## Run app locally

    flask run