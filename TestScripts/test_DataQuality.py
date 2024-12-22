
# Assignment for completing the file size check for all the other file/types

import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import logging
import pytest
import os

# Configure the logging
from CommonUtilities.utilities import file_to_db_verify, db_to_db_verify, check_file_exists, check_file_size

logging.basicConfig(
    filename='Logs/etlprocess.log',  # Name of the log file
    filemode='a',  # 'a' to append, 'w' to overwrite
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    level=logging.INFO  # Set the logging level
)
logger = logging.getLogger(__name__)

# create mysql database commection
from Config.config import *

#mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/retaildwh')
mysql_engine = create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}')

@pytest.mark.DQ_Check
def test_DQ_Sales_Data_File_Availability():
    try:
        logger.info("File availability check for Sales_data.csv has been initiated.. ")
        assert check_file_exists("TestData/sales_data.csv"),"Sales_data file is not available"
        logger.info("File availability check for Sales_data.csv has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file availability check{e}")
        pytest.fail(f"Test failed due to sales_data.csv file unavailability")

# Assignment for completing the file availability check for all the other file/types

@pytest.mark.DQ_Check
def test_DQ_Sales_Data_File_SizeCheck():
    try:
        logger.info("File size check for Sales_data.csv has been initiated.. ")
        assert check_file_size("TestData/sales_data.csv"),"Sales_data file is zero byte file"
        logger.info("File size check for Sales_data.csv has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file size check{e}")
        pytest.fail(f"Test failed due to sales_data.csv due to zero byte file")

@pytest.mark.DQ_Check
def test_DQ_product_Data_File_Availability():
    try:
        logger.info("File availability check for product_data.csv has been initiated.. ")
        assert check_file_exists("TestData/product_data.csv"),"product_data file is not available"
        logger.info("File availability check for product_data.csv has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file availability check{e}")
        pytest.fail(f"Test failed due to sales_data.csv file unavailability")

# Assignment for completing the file availability check for all the other file/types

@pytest.mark.DQ_Check
def test_DQ_product_Data_File_SizeCheck():
    try:
        logger.info("File size check for product_data.csv has been initiated.. ")
        assert check_file_size("TestData/product_data.csv"),"product_data file is zero byte file"
        logger.info("File size check for product_data.csv has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file size check{e}")
        pytest.fail(f"Test failed due to product_data.csv due to zero byte file")

@pytest.mark.DQ_Check
def test_DQ_inventory_Data_File_Availability():
    try:
        logger.info("File availability check for inventory_data.xml has been initiated.. ")
        assert check_file_exists("TestData/inventory_data.xml"),"product_data file is not available"
        logger.info("File availability check for inventory_data.xml has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file availability check{e}")
        pytest.fail(f"Test failed due to inventory_data.xml file unavailability")

# Assignment for completing the file availability check for all the other file/types

@pytest.mark.DQ_Check
def test_DQ_inventory_Data_File_SizeCheck():
    try:
        logger.info("File size check for inventory_data.xml has been initiated.. ")
        assert check_file_size("TestData/inventory_data.xml"),"product_data file is zero byte file"
        logger.info("File size check for inventory_data.xml has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file size check{e}")
        pytest.fail(f"Test failed due to inventory_data.xml due to zero byte file")

@pytest.mark.DQ_Check
def test_DQ_supplier_Data_File_Availability():
    try:
        logger.info("File availability check for supplier_data.json has been initiated.. ")
        assert check_file_exists("TestData/supplier_data.json"),"supplier_data file is not available"
        logger.info("File availability check for supplier_data.json has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file availability check{e}")
        pytest.fail(f"Test failed due to supplier_data.json file unavailability")

# Assignment for completing the file availability check for all the other file/types

@pytest.mark.DQ_Check
def test_DQ_supplier_Data_File_SizeCheck():
    try:
        logger.info("File size check for supplier_data.json has been initiated.. ")
        assert check_file_size("TestData/supplier_data.json"),"supplier_data file is zero byte file"
        logger.info("File size check for supplier_data.json has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file size check{e}")
        pytest.fail(f"Test failed due to supplier_data.json due to zero byte file")


@pytest.mark.DQ_Check
def test_DQ_sales_Data_linux_File_Availability():
    try:
        logger.info("File availability check for sales_Data_linux.csv has been initiated.. ")
        assert check_file_exists("TestData/sales_Data_linux.csv"),"supplier_data file is not available"
        logger.info("File availability check for sales_Data_linux.csv has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file availability check{e}")
        pytest.fail(f"Test failed due to sales_Data_linux.csv file unavailability")

# Assignment for completing the file availability check for all the other file/types

@pytest.mark.DQ_Check
def test_DQ_sales_Data_linux_File_SizeCheck():
    try:
        logger.info("File size check for sales_Data_linux.csv has been initiated.. ")
        assert check_file_size("TestData/sales_Data_linux.csv"),"supplier_data file is zero byte file"
        logger.info("File size check for sales_Data_linux.csv has been completed.. ")
    except Exception as e:
        logger.error(f"Error during file size check{e}")
        pytest.fail(f"Test failed due to sales_Data_linux.csv due to zero byte file")