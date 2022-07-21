#!/usr/bin/env python
# coding: utf-8

# %%
import numpy as np
import pandas as pd
import regex as re
pd.set_option('display.max_rows',5)
pd.set_option('display.max_colwidth', None)
from functools import *
from difflib import SequenceMatcher

import warnings
warnings.filterwarnings('ignore')
import math
import seaborn as sns
sns.set_theme(style="darkgrid")
import os


# ## Import original data

# %%
data = pd.read_pickle('/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/standardized_dfs.pickle')
data['2010']

years = range(2010, 2021, 1)
    
    
data2010 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2010.pickle")
data2011 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2011.pickle")
data2012 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2012.pickle")
data2013 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2013.pickle")
data2014 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2014.pickle")
data2015 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2015.pickle")
data2016 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2016.pickle")
data2017 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2017.pickle")
data2018 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2018.pickle")
data2019 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2019.pickle")
data2020 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2020.pickle")
data2021 = pd.read_pickle("/Users/samtan/Downloads/SERU Timeline Project/Sam&Tiffany/datasets_with_standardized_labels /standardized_df_2021.pickle")


# ## Import paired labels

# %%

os.chdir('/Users/samtan/Downloads/SERU Timeline Project/Jessamine&Matilda/SP22')
matched_dict = pd.read_excel("common_10to21.xlsx")
matched_dict = matched_dict .iloc[:, 1:]
matched_dict


# %%


# add a year column to each dataset
data2010["YEAR"] = 2010
data2011["YEAR"] = 2011
data2012["YEAR"] = 2012
data2013["YEAR"] = 2013
data2014["YEAR"] = 2014
data2015["YEAR"] = 2015
data2016["YEAR"] = 2016
data2017["YEAR"] = 2017
data2018["YEAR"] = 2018
data2019["YEAR"] = 2019
data2020["YEAR"] = 2020
data2021["YEAR"] = 2021


# %%


# discard matched questions; only need labels
matched_labels = matched_dict[["label10","label11",
                               "label12","label13", "label14",
                              "label15",
                              "label16", 
                              "label17",
                              "label18", 
                              "label19", 
                              "label20",
                              "label21"]]

# ## Create a latest label column for retrieval

# %%


# create a column with the LATEST LABEL
latest_label = []
for index, row in matched_labels.iterrows():
    for i in reversed(row):
        if not isinstance(i, float): # not nan
            latest_label.append(i)
            break
matched_labels['LABEL'] = latest_label
matched_labels


# %%


matched_labels_admin = pd.DataFrame({'label10': ["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                np.nan,"HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE",np.nan,"TOTAL_UNITS", "SEED"],
                                     'label11': ["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
               np.nan,"HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS", "SEED"],
                                   'label12': ["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS", "SEED"],
                                   'label13':["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS", "SEED"],
                                   "label14": ["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS", "SEED"],
                                   "label15":["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS", "SEED"],
                                   "label16":["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS", "SEED"],
                                   'label17':["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS", "SEED"],
                                   "label18":["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT",np.nan, "SEED"],
                                   "label19": ["NATIVE_UNITS",np.nan,"AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS", "SEED"],
                                   "label20": ["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL",np.nan,"CUMGPA_NATIVE",np.nan,
                "SATICR","SATIM","SATIW",np.nan,np.nan,np.nan,np.nan,np.nan,"RESIDENT",np.nan, "SEED"],
                                   "label21":["NATIVE_UNITS",np.nan,"AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE",np.nan,
                np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,"AGE","RESIDENT","TOTAL_UNITS", "SEED"],
                                     "LABEL": ["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1","HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS", "SEED"]})



# %%


matched_labels = pd.concat([matched_labels, matched_labels_admin])
matched_labels



# ## Create a lookup function
# Return merged df with all relevant data

# %%


def cur_label(label):
    # filter out matched_label rows
    cur_labels = matched_labels[matched_labels["LABEL"] == label]
    return cur_labels


# %%


def lookup(label, admin_group = None, cur_labels = None):
    '''
    input: label, a string, representing the latest label need to be looked up
            admin_group
    output: merged_df, a dataframe with two columns. 
        Column 1: <label>, with all data of the label across 10 years
        Column 2: year, representing the year from which data comes from
    '''
    merged_df = pd.DataFrame()
    merged_df[label] = []
    # merged_df["YEAR"] = []
    label_dict = {} # dict keep track of what labels have been appended for each year
    
    try:
        cur_labels == None
        cur_labels = cur_label(label)
    except:
        pass

    
    for index, row in cur_labels.iterrows():
        yr_counter = 2010
        for i in row: # i: specific label of this year
            if (not isinstance(i, float)) and ((yr_counter not in label_dict.keys()) or 
                                               (i not in label_dict[yr_counter])): # not nan and has not been appended
                try:
                    if admin_group:
                        data_this_year = eval("data" + str(yr_counter))[[i, admin_group, "YEAR"]]
                        
                        
                    else:
                        # data_this_year = eval("data" + str(yr_counter))[[i, "YEAR", "SEED"]]
                        data_this_year = eval("data" + str(yr_counter))[[i, "SEED"]]
                        
                        
                    merged_df = merged_df.append(data_this_year.rename(columns={i: label}))
                
                    if yr_counter not in label_dict.keys():
                        label_dict[yr_counter] = []
                    label_dict[yr_counter].append(i)
                    
                except:
                    print(yr_counter, i) # if label cannot be found in data, print year
                
            yr_counter += 1
            if yr_counter == 2022:
                break
    # merged_df["YEAR"] = merged_df["YEAR"].astype(int)
    return merged_df



# %%

# ## Get a merged df (Update 4/7)

# Add a unique seed to each row; later on join on the seed


data2010["SEED"] = np.nan
data2011["SEED"] = np.nan
data2012["SEED"] = np.nan
data2013["SEED"] = np.nan
data2014["SEED"] = np.nan
data2015["SEED"] = np.nan
data2016["SEED"] = np.nan
data2017["SEED"] = np.nan
data2018["SEED"] = np.nan
data2019["SEED"] = np.nan
data2020["SEED"] = np.nan
data2021["SEED"] = np.nan


# %%

data2010["SEED"] = ['2010' + i for i in data2010.index.values.astype(str)]
data2011["SEED"] = ['2011' + i for i in data2011.index.values.astype(str)]
data2012["SEED"] = ['2012' + i for i in data2012.index.values.astype(str)]
data2013["SEED"] = ['2013' + i for i in data2013.index.values.astype(str)]
data2014["SEED"] = ['2014' + i for i in data2014.index.values.astype(str)]
data2015["SEED"] = ['2015' + i for i in data2015.index.values.astype(str)]
data2016["SEED"] = ['2016' + i for i in data2016.index.values.astype(str)]
data2017["SEED"] = ['2017' + i for i in data2017.index.values.astype(str)]
data2018["SEED"] = ['2018' + i for i in data2018.index.values.astype(str)]
data2019["SEED"] = ['2019' + i for i in data2019.index.values.astype(str)]
data2020["SEED"] = ['2020' + i for i in data2020.index.values.astype(str)]
data2021["SEED"] = ['2011' + i for i in data2021.index.values.astype(str)]





admin_labels = ["NATIVE_UNITS","ETHNICITY","AFRICAN_AMERICAN","AMERICAN_INDIAN","ASIAN","WHITE",
                "PACIFIC_ISLANDER","HISPANIC","STATUS","GENDER","CIP_CODE1""HSGPA_CALC","HSGPA_UNW",
                "LEVEL","TERM1","UNIVERSITY","YEAR","INTERNATIONAL","CUMGPA","CUMGPA_NATIVE","HSRANK",
                "SATICR","SATIM","SATIW","ACTE","ACTM","ACTR","ACTS","AGE","RESIDENT","TOTAL_UNITS"]



index_col = pd.concat([data2010["SEED"], data2011["SEED"], data2012["SEED"],data2013["SEED"],data2014["SEED"],
                       data2015["SEED"],data2016["SEED"],data2017["SEED"],data2018["SEED"],data2019["SEED"],
                      data2020["SEED"],data2021["SEED"]])


final_df = pd.DataFrame(index_col)
for label in matched_labels["LABEL"]:
    cur_df = lookup(label)
    final_df = cur_df.merge(final_df, on = "SEED", how = "right")


# final_df_pickle = pd.read_pickle('final_df.pickle')

#final_df.to_csv("final_df.csv")
#final_df.to_pickle("final_df.pickle") 
# final_df.pickle is the same as final_df.csv. 
# pickle is a 80 Times faster to load but it's a python-specific object. 

# Reload:  final_df = pd.read_pickle('final_df.pickle') 



admin_labels = ["NATIVE_UNITS", "ETHNICITY", "AFRICAN_AMERICAN", "AMERIAN_INDIAN", "ASIAN", "WHITE", "HISPANIC", 
                "RESIDENT", "GENDER", "CIP_CODE1", "HSGPA_CALC", "HSGPA_UNW", "LEVEL", "TERM1", "UNIVERSITY", "YEAR", 
                "INTERNATIONAL","CUMGPA", "CUMGPA_NATIVE", "STATUS", "SEED"]





def lookup_admin(label_df):
    merged_df = pd.DataFrame(index_col)
    count = 0
    while count < 2:
        for index, row in label_df.iterrows():
            yr_counter = 2010
            for i in row: # i: specific label of this year
                if not isinstance(i, float):
                    try:
                        data_this_year = eval("data" + str(yr_counter))[[i, "SEED"]]


                        merged_df = merged_df.append(data_this_year.rename(columns={i: label}))

                    except:
                        print(yr_counter, i) # if label cannot be found in data, print year

                yr_counter += 1
                if yr_counter == 2022:
                    break
        count += 1
    return merged_df



# add admin to the common label df; editted/combined the replicated final labels

common_10to21 = pd.read_excel("common_10to21.xlsx")
common_10to21 = common_10to21.iloc[:, 1:]

# filter out the actual questions. Keep just the label names.  
common_labels = common_10to21[["label10","label11",
                               "label12","label13", "label14",
                              "label15",
                              "label16", 
                              "label17",
                              "label18", 
                              "label19", 
                              "label20",
                              "label21"]]

# create a column with the LATEST LABEL
latest_common_label = []
for index, row in common_labels.iterrows():
    for i in reversed(row):
        if not isinstance(i, float): # not nan
            latest_common_label.append(i)
            break
common_labels['LABEL'] = latest_label
common_labels = pd.concat([common_labels, matched_labels_admin])
# output: common_labels.to_csv("common_labels")



common_labels_filtered = common_labels.copy()
for index, row in common_labels_filtered.iterrows():
    row_last5 = row.iloc[7:12] # 
    na_num = sum(pd.isna(row_last5))
    if na_num > 3:
        common_labels_filtered = common_labels_filtered.drop([index])


# only include >=2 items in past 5 years 
final_df_filtered = pd.DataFrame(index_col)
count = 0
for label in common_labels_filtered["LABEL"]:
    cur_df_filtered = lookup(label)
    final_df_filtered = cur_df_filtered.merge(final_df_filtered, on = "SEED", how = "right")
    
    print(count)
    count += 1
    


final_df_filtered.to_csv('final_df_filtered.csv')


# # create a column with the LATEST LABEL
# latest_label = []
# for index, row in matched_labels.iterrows():
#     for i in reversed(row):
#         if not isinstance(i, float): # not nan
#             latest_label.append(i)
#             break

# matched_def = matched_dict.iloc[:, [1,3,5,7,9,11,13,15,17,19,21,23]]
# # create a column with the LATEST MEANING
# latest_meaning = []
# for index, row in matched_def.iterrows():
#     for i in reversed(row):
#         if not isinstance(i, float): # not nan
#             latest_meaning.append(i)
#             break


# latest = pd.DataFrame({'label': latest_label, 'meaning':latest_meaning})


# #common_labels_filtered.merge(latest, left_on = 'LABEL', right_on = 'label', how = 'left').drop_duplicates(subset = 'LABEL').drop(columns = 'label').to_excel("common_label_def.xlsx")



# common_labels_filtered.drop_duplicates(subset = "LABEL").shape


# final_df_filtered = final_df_filtered.rename(columns = {"SATIW_x": "SATIW", "SATIM_x": "SATIM", "SATICR_x": "SATICR"})

