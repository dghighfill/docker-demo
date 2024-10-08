# Docker Demo

This demo just launches a very simple flyway container and migrates a database.

## Exercise 1

Clone the repository https://github.com/dghighfill/docker-demo.git 

Checkout exercise 1 with

```
$ git switch exercise-1
```

Run the following command from a terminal window

```
$ ./run_docker.sh clean migrate info
```

## Exercise 2

This exercise builds a Docker container with a very simple python script that runs when the container is ran.
Checkout exersie 2 with

```
$ git switch exercise-2
```

Run the following command from a terminal window

```
$ ./build.sh
```

## Exercise 3

Now we're going to introduce a docker-compose.yml file that allows you to run multiple services.  Eventually this will house our UI, python API and Database.

Checkout exersie 3 with

```
$ git switch exercise-3
```

Review the docker-compose.yml.  We've moved the startup of flyway and its configuration to this file.

Run the following command from a terminal window

```
$ ./run_docker_compose.sh
```

## Exercise 4

Now we're going to layer in all the components in our docker-compose.yml

Checkout exersie 4 with

```
$ git switch exercise-4
```

Review the docker-compose.yml.  We have now added the UI and API.

Run the following command from a terminal window.  This will build the Dockerfile which builds a docker image with our application and fast api requirements.  This image is then used in the docker-compose-yml file.

```
$ ./run_docker_compose.sh
```
