#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:27:42 2023

@author: nidhisharma
"""

import pandas as pd

def read_and_prepare_file(file_path, col_mapping, date_columns):
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
    except FileNotFoundError:
        raise FileNotFoundError(f"{file_path} not found")
    
    df = preprocess(df, col_mapping, date_columns)
    
    if 'cpid' not in df.columns or 'insid' not in df.columns:
        raise ValueError(f"{file_path} is missing either 'cpid' or 'insid'")
    
    df['unique_key'] = df['cpid'].astype(str) + '_' + df['insid'].astype(str)
    df.set_index('unique_key', inplace=True)
    return df

def preprocess(df, col_mapping, date_columns):
    for col in df.columns:
        if col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
        elif col in col_mapping and col_mapping[col] == 'float':
            df[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            df[col] = df[col].astype(str)
    return df

col_mapping_file1 = {'amount': 'float', 'date1': 'date', 'date2': 'date', 'date3': 'date', 'date4': 'date'}
col_mapping_file2 = {'amount': 'float', 'date1': 'date', 'date2': 'date', 'date3': 'date', 'date4': 'date'}
date_columns_file1 = ['date1', 'date2', 'date3', 'date4']
date_columns_file2 = ['date1', 'date2', 'date3', 'date4']

file1 = 'path_to_file1.xlsx'
file2 = 'path_to_file2.xlsx'

try:
    df1 = read_and_prepare_file(file1, col_mapping_file1, date_columns_file1)
    df2 = read_and_prepare_file(file2, col_mapping_file2, date_columns_file2)
except ValueError as ve:
    print(ve)
    exit()
except FileNotFoundError as fe:
    print(fe)
    exit()

common_keys = df1.index.intersection(df2.index)
unique_in_df1 = df1.index.difference(df2.index)
unique_in_df2 = df2.index.difference(df1.index)

common_df1 = df1.loc[common_keys].sort_index(axis=1)
common_df2 = df2.loc[common_keys].sort_index(axis=1)

comparison_results_df = pd.DataFrame(columns=['cpid', 'insid', 'comparison'])

if not common_df1.equals(common_df2):
    for idx in common_df1.index:
        cpid, insid = idx.split('_')
        row_df1, row_df2 = common_df1.loc[idx], common_df2.loc[idx]
        
        mismatched_cols = [col for col in common_df1.columns if row_df1[col] != row_df2[col]]
        
        if mismatched_cols:
            comparison_results_df = comparison_results_df.append({'cpid': cpid, 'insid': insid, 'comparison': f"{', '.join(mismatched_cols)}_mismatched"}, ignore_index=True)

for unique_key in unique_in_df1:
    cpid, insid = unique_key.split('_')
    comparison_results_df = comparison_results_df.append({'cpid': cpid, 'insid': insid, 'comparison': 'Missing_in_file2'}, ignore_index=True)

for unique_key in unique_in_df2:
    cpid, insid = unique_key.split('_')
    comparison_results_df = comparison_results_df.append({'cpid': cpid, 'insid': insid, 'comparison': 'Missing_in_file1'}, ignore_index=True)

comparison_results_df.to_excel('comparison_results.xlsx', index=False)