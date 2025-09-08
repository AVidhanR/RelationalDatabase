import sys
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# If running in Google Colab, install PostgreSQL and restore the database
if 'google.colab' in sys.modules:
    # Update package installer
    !sudo apt-get update -qq > /dev/null 2>&1

    # Install PostgreSQL
    !sudo apt-get install postgresql -qq > /dev/null 2>&1

    # Start PostgreSQL service (suppress output)
    !sudo service postgresql start > /dev/null 2>&1

    # Set password for the 'postgres' user to avoid authentication errors (suppress output)
    !sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'password';" > /dev/null 2>&1

    # Create the 'colab_db' database (suppress output)
    !sudo -u postgres psql -c "CREATE DATABASE contoso_100k;" > /dev/null 2>&1

    # Download the PostgreSQL .sql dump
    !wget -q -O contoso_100k.sql https://github.com/lukebarousse/Int_SQL_Data_Analytics_Course/releases/download/v.0.0.0/contoso_100k.sql

    # Restore the dump file into the PostgreSQL database (suppress output)
    !sudo -u postgres psql contoso_100k < contoso_100k.sql > /dev/null 2>&1

    # Shift libraries from ipython-sql to jupysql
    !pip uninstall -y ipython-sql > /dev/null 2>&1
    !pip install jupysql > /dev/null 2>&1

# Load the sql extension for SQL magic
%load_ext sql

# Connect to the PostgreSQL database
%sql postgresql://postgres:password@localhost:5432/contoso_100k

# Enable automatic conversion of SQL results to pandas DataFrames
%config SqlMagic.autopandas = True

# Disable named parameters for SQL magic
%config SqlMagic.named_parameters = "disabled"

# Display pandas number to two decimal places
pd.options.display.float_format = '{:.2f}'.format
