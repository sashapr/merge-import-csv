# -*- coding: utf-8 -*-
"""
Created on: August 2018

Created by: Sasha Prokosheva

Merge TXT, CSV files in a given folder and save as one CSV
"""
# usual stuff
import pandas as pd
import numpy as np
import re

# To operate with folders
import os

# To read several files
import glob


##############################################################################################
# Identify folder and the delimeter
##############################################################################################
path_folder = input("Type full path to the folder where the files are located: ")
my_delim = input("What is the delimeter for your data? ")
path_folder = path_folder.upper()

#############################################################
# Merge files
#############################################################
def CleanData(my_delim, path_folder):
    '''
    Function which imports CSV files from a given folder, merges them into one file (CSV) and creates additional column with datasets identifier as values.

    input: path_folder = location; delimiter = how the data is delimited
    output: DF
    '''
    df_merged = pd.DataFrame()

    try:
        if path_folder[-1] != "/":
            path_folder = path_folder + "/"
        # Read file names
        os.chdir(path_folder)
        files = [item.upper() for item in glob.glob("*.csv")]


        # Read data by row, join all cells
        for file in files:
            df = pd.read_csv(file, delimiter = my_delim)
            print("File to be merged: ", file)
            file_name = input("Please name it for the final dataset: ")
            df["file name"] = file_name
            df_merged = df_merged.append(df)

        df_merged = df_merged.reset_index(drop=True)

        # Save to CSV
        merged_file_name = input("How would you like to name the merged file? ")
        path = merged_file_name + '.csv'
        df_merged.to_csv(path, index=False, encoding='utf-8')

        print("Merged dataframe column types: ", df_merged.dtypes)

        return df_merged

    except:
        print("Some error...")
