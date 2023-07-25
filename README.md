www.babalada.com
===
A stock investment simulator
---
Developed between June 7, 2023 and July 24, 2023.

Babalada uses data from the real stock market to provide a realistic trading environment with risk management tools, a social platform (forum), and performance evaluation metrics to help users assess and improve their stock trading skills.

This is a website built with [SvelteKit], [Typescript], & [Sass] to compile a html/css/js application delivered by a [Node] server. [Docker] is used to deploy the UI server within a minified [Ubuntu] environment. UI dependencies are managed by [PNPM]. The Docker container is to be hosted by [Fly] at https://www.babalada.com.

The website UI depends upon a [Python 3] server running on an [Ubuntu] machine to perform ORM for a [Postgres] database. Server dependencies are managed by [Pip]. The UI communicates with the server through REST endpoints. The server and database are to be hosted by [AWS].

### Install Dev Dependencies
* [Install PNPM] and ensure it's accessible by PATH.
* [Install Docker] and ensure it's accessible by PATH.
* Open a terminal in the root directory of this repository.
* Run `pnpm i` in the terminal to install UI dependencies.

From here, you can run, develop, and deploy the project.

### Run Scripts
To run a script, type `pnpm run <script-name>` in a terminal within the root folder.

| script-name | description |
|:----------- |:----------- |
| `ui` | create a local hot-reloading server at [localhost:5173](http://localhost:5173) for UI development |
| `api` | create a local server at [localhost:5000](http://localhost:5000) for API development |
| `build` | compile a production version of the UI server into the build folder |
| `preview` | create a local docker container to serve the UI server and API server - run `build` first |
| `deploy` | deploy the UI & API servers with flyctl |
| `check` | evaluate Svelte syntax |
| `check:watch` | re-evaluate Svelte syntax when files are updated |

### Deploy App
This app is set up to use [Fly.io] to deploy a Docker container. To deploy with Fly:
* [Install flyctl] and ensure it's accessible by PATH.
* Create or update `.env` file with necessary secrets variables.
* Run `pnpm run deploy` to deploy the UI & Server.

From here, you can access the server remotely via SSH by running `flyctl ssh console`.

### Run API Without Docker
* You must be operating on an Ubuntu machine or equivalent (like WSL).
* [Install Python 3] and ensure it's accessible by PATH.
* Open a terminal in the root directory of this repository.
* Run `python -m venv venv` to create the virtual environment.
* Run `source venv/bin/activate` to activate the virtual environment.
* Run `pip install -r requirements.txt` in the terminal to install server dependencies within your virtual environment.
* Add secrets to .env file.
* Use VS Code to run the Flask server with "Run and Debug".

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
[Install Docker]: https://docs.docker.com/engine/install/
[Pip]: https://pypi.org/project/pip/
[Postgres]: https://www.postgresql.org/about/
[Fly]: https://fly.io/docs/
[Install flyctl]: https://fly.io/docs/hands-on/install-flyctl/
[AWS]: https://aws.amazon.com/
