# Interactive Documentation for PyTerrier
There are three folders for the source code.

1. `api` folder contains the back-end of the project, developd using Python and FastAPI.
2. `pyterrier-doc` folder contains the front-end of the project, developed using Docusaurs, which uses React(Typescript).
3. `PyTerrierBaseImage` foder contains the dockerfile that is used for building the base image that is used in the back-end.

## Requirements
### Front-end
* Node.js version 18.0 or above
### Back-end
* Python 3.10.x
* Packages: listed in `requirements.txt`
* Tested on MacOS and Windows 10

## Initialize
### Front-end 
```bash
yarn 
```
This command will install dependencies in the `package.json`.

### Back-end 
```bash
./run.sh init
```
Running the command below will install python dependencies and index folders that is required when using PyTerrier.

## Build steps
### Front-end 
```bash
yarn build
```
Run this command to build the front-end.

### Back-end
```bash
docker build -t "Image name" .
```
This command will build the docker image from `dockerfile` for API.

### PyTerrier Base Image
```bash
docker build -t "Image name" .
```
This command will build the docker image from `dockerfile` for pyterrier base docker image.


## Test steps
### Back-end
```bash
./run.sh test
```
This command is use for testing the back-end specifically the generated function in `generate.py`.



