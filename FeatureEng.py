# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to 
import pandas as pd

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1):

    # Execution logic goes here

    
    dataframe1['TotalSF'] = dataframe1['1stFlrSF'] + dataframe1['2ndFlrSF'] + dataframe1['TotalBsmtSF']
    dataframe1['TotalRoom'] = dataframe1['TotRmsAbvGrd'] + dataframe1['FullBath'] + dataframe1['HalfBath']
    dataframe1['TotalPorchAr'] = dataframe1['OpenPorchSF'] + dataframe1['EnclosedPorch'] + dataframe1['3SsnPorch'] + dataframe1['ScreenPorch']

    # If a zip file is connected to the third input port is connected,
    # it is unzipped under ".\Script Bundle". This directory is added
    # to sys.path. Therefore, if your zip file contains a Python file
    # mymodule.py you can import it using:
    # import mymodule
    
    # Return value must be of a sequence of pandas.DataFrame
    return dataframe1,
