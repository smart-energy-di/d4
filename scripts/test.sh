#! /usr/bin/env bash

# Exit in case of error
set -e

# Run this from the root of the project

rm -rf ./testing-project

echo "ls -la ./ [in root]"
ls -la ./

cookiecutter --no-input -f ./ project_name="Testing Project"

echo "ls -la ./ [in testing-project]"
ls -la ./testing-project/

cd ./testing-project

echo "cookiecutter --version"
cookiecutter --version


echo "ls -la ./ [in testing-project]"
ls -la ./

pip install -r ./spot/requirements_dev.txt

pytest .

bash ./scripts/test.sh "$@"

cd ../
