# Install

- create virtualenv
```bash
virtualenv -p python3.6 venv
```
- run virtualenv
```bash
source vemv/bin/activate
```
- install requirements
```bash
pip install -r requirements.txt
```
- run tests
```bash
py.test
```
- run application
```bash
python run.py
```

# How it works

I made a handler class and separate classes for entities, validators and data formatters for writing to a file. 
CSVHandler can read csv files to list of given entities (Hotels in the example. models.hotels.Hotels).
It is possible to register validators in current csv handler and set output format (without registering formatter for output it could not write to file).

In Solution there are two formatters: xml and json, but it is simple to add another.

The input files are in the "storage" folder. The output files save to the storage folder too.

Rating validation and uri validation are developed in separated validator classes as plug-in modules. Utf-8 validation is developed in CSVHandler as required validation.

Also there is the sort function for sort data.

