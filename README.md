# HDF2SQL

Export the data in a HDF5 (Hierarchial Data Format) file to a SQLServer database

## Usage

Create or edit the config.yaml for your situation:

```
HDF:
  # Specify nodes here individually
  nodes:
    - /df1
    - /sub/df2
    - /sub/df3
  # NOT_IMPLEMENTED_YET: Specify entire hierarchy folders here
  folders:
    - /sub2
    - /everything/under/here
  

Database:
  sqlalchemy_connection_string: 'mssql+pyodbc://localhost\SQLEXPRESS/Northwind?driver=ODBC+Driver+13+for+SQL+Server;Integrated Security=True'
  schema: dbo
```

Run the script:
```
python hdf2sql.py datastore.hdf myconfig.yaml
```


## Why HDF 

HDF has lighting fast reads and writes compared to a database or CSV files.  

## Why a Database

SQLServer is much more accesible to many users than a HDF file.  Pushing the data to a database
allows a wider audience of people to debug problems.  It also makes it easier to share data 
with a larger audience. 

