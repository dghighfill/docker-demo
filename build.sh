#!/bin/bash

winpty docker build -t my_python_app .

winpty docker run --rm my_python_app

