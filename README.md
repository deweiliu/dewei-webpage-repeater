# [Dewei Webpage Repeater](http://repeater.deweiliu.com)

## Live Demo
A Live demo is available at [repeater.deweiliu.com](http://repeater.deweiliu.com)

## Check out the app
### Prerequisite
* Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/)
### Execution
Require root previleges

    sudo su
Build the application and run it in background

    docker-compose up -d

Wait for a couple minutes until the server fully starts up. Then open http://localhost/ with a browser

To stop the application

    docker-compose down

## Continous Deployment
Continous deployment is running for Docker Hub using [Git Action](.github/workflows/docker.yml). To enable this automatic process in your GitHub repository, add a [Docker Access Token](https://docs.docker.com/docker-hub/access-tokens/) to your [GitHub Secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) with the name *docker_access*
