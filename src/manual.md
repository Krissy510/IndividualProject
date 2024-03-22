# User manual
## Running the application
### Front-end 
```bash
yarn start
```
This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.


```bash
yarn serve
```
This command serves your built website locally, implying that the website will not be reflected to changes live.

> Seach bar is only support in the built version

### Back-end 
```bash
./run.sh dev
```
This command will runs the api andd will reload itself when the code is modified.

```bash
./run.sh start
```
This command also runs the api. However, this version will not reload itself when the code is modified.

## Deploy
### Back-end (Docker image)
The API docker image can be found on Docker hub: `kris310/pyterrier-api:V1.0`.

Requirements:
* Requires Docker
* Server memory
    * Minimum: 4GB
    * Recommend: 8GB
* CPU
    * Minimum: 1

### PyTerrier Base Image
The base docker image can be found on Docker hub: `kris310/base-pyterrier-py3.10:V1.0`.

Requirements:
* Requires Docker
* Memory >= 1GB
