# Pyterrier API
## Requirement
Programming Language: **Python 3.10.x** (Any version that PyTorch works)
## Set up
### Local
For local machine use `local-test` branch instead since the main version contained [Pyterrier PISA](https://github.com/terrierteam/pyterrier_pisa) which does not work always local machine due to its requirement.

Make the script executable:
```bash
chmod +x cli.py
```
Then run the commmand below to start installing dependencies and dataset's index.
```bash
./run.sh init
```
### Server
For server, you can do the same but on the `main` branch if your server match the requirement of [Pyterrier PISA](https://github.com/terrierteam/pyterrier_pisa). If not then use the same version as local.

## Local Run
To run, simply use the following command:
```bash
./run.sh dev
```
> Make sure that the script is exectuable ([Read here](#local))

## Testing
Test suite in this project onyl test non-pyterrier functions. 

Run test using the following command:
```bash
./run.sh test
```

## Credits
- Sean MacAvaney, University of Glasgow
- Raviphas Sananpanichkul, University of Glasgow