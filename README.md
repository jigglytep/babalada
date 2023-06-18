Babalada
===
A stock investment simulator
---
Developed between June 7, 2023 and July 24, 2023.

Babalada uses data from the real stock market to provide a realistic trading environment with risk management tools, a social platform (forum), and performance evaluation metrics to help users assess and improve their stock trading skills.

This is a website built with [SvelteKit], [Typescript], & [Sass] to compile a html/css/js application delivered by a [Node] server. [Docker] is used to deploy the UI server within a minified [Ubuntu] environment. UI dependencies are managed by [PNPM]. The Docker container is to be hosted by [Fly] at https://www.babalada.com.

The website UI depends upon a [Python 3] server running on an [Ubuntu] machine to perform ORM for a [Postgres] database. Server dependencies are managed by [Pip]. The UI communicates with the server through REST endpoints. The server and database are to be hosted by [AWS].

### Install UI
* [Install PNPM].
* Open a terminal in the root directory of this repository.
* Run `pnpm i` in the terminal to install UI dependencies.

From here, you can run, develop, and deploy the UI side of the project.

### Run UI Scripts
To run a script, type `pnpm run <script-name>` in a terminal within the root folder.

| script-name | description |
|:----------- |:----------- |
| `dev` | create a local hot-reloading server at [localhost:5173](http://localhost:5173) for development purposes |
| `build` | compile a production version of the app into the build folder |
| `preview` | create a local server which serves the contents of the build folder at [localhost:4173](http://localhost:4173) |
| `check` | evaluate Svelte syntax |
| `check:watch` | re-evaluate Svelte syntax when files are updated |

### Deploy UI
This app is set up to use [Fly.io] to deploy a Docker container. To deploy with Fly:
* Install UI.
* [Install flyctl].
* Run `pnpm run build` to build the app files.
* Run `flyctl deploy` or `flyctl launch` to deploy the app files.

From here, you can access the server remotely via SSH by running `flyctl ssh console`.

### Install Server
* You must be running a Linux Ubuntu machine or equivalent to install the server locally.
* [Install Python 3].
* Open a terminal in the root directory of this repository.
* Run `python -m venv venv` to create the virtual environment.
* Run `source venv/bin/activate` to activate the virtual environment.
* Run `pip install -r python-packages.txt` in the terminal to install server dependencies within your virtual environment.
* Run the following to create environment variables:
```
export FLASK_APP=server
export PG_PASSWD=<PASSWORD>
export PG_USR=<USERNAME>
export PG_URL=<URL>
```

From here, you can run, develop, and deploy the server side of the project.

### Run Server Scripts
* Run `flask run` to run the app locally.
* TODO: Lev

### Deploy Server
* TODO: Lev

[SvelteKit]: https://kit.svelte.dev/docs/introduction
[Typescript]: https://www.typescriptlang.org/why-create-typescript
[Sass]: https://sass-lang.com/guide
[Node]: https://nodejs.org/en/docs/guides/
[Docker]: https://docs.docker.com/get-started/overview/
[Ubuntu]: https://ubuntu.com/about
[PNPM]: https://pnpm.io/motivation
[Install PNPM]: https://pnpm.io/installation
[Python 3]: https://www.python.org/
[Install Python 3]: https://www.python.org/downloads/
[Pip]: https://pypi.org/project/pip/
[Postgres]: https://www.postgresql.org/about/
[Fly]: https://fly.io/docs/
[Install flyctl]: https://fly.io/docs/hands-on/install-flyctl/
[AWS]: https://aws.amazon.com/

# TODO: remove the following notes

Login Tutorial for refrence: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login