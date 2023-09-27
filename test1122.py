#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:44:50 2023

@author: nidhisharma
"""
import pandas as pd


file1_df = pd.read_excel("File1.xlsx")
file2_df = pd.read_excel("File2.xlsx")


def compare_values(val1, val2):
    if pd.isna(val1) and pd.isna(val2):
        return True
    elif (is_numeric(val1) or isinstance(val1, str)) and \
            (is_numeric(val2) or isinstance(val2, str)):
        val1 = float(val1) if is_numeric(val1) else val1
        val2 = float(val2) if is_numeric(val2) else val2
        return val1 == val2
    else:
       
        return str(val1).strip().lower() == str(val2).strip().lower()


def is_numeric(val):
    try:
        float(val)
        return True
    except (ValueError, TypeError):
        return False


result_df = pd.DataFrame(columns=['entityid', 'result_summary'])


for index, row1 in file1_df.iterrows():
    entityid = row1['entityid']
    empid = row1['empid']
    
    if (entityid, empid) in file2_df[['entityid', 'empid']].apply(tuple, axis=1).values:
        row2 = file2_df[(file2_df['entityid'] == entityid) & (file2_df['empid'] == empid)].iloc[0]
        
        result_details = []
        
        for col1 in file1_df.columns:
            if col1 not in ['entityid', 'empid']:
               
                col2 = None
                for c in file2_df.columns:
                    if compare_values(row1[col1], row2[c]):
                        col2 = c
                        break
                
                if col2:
                    if not compare_values(row1[col1], row2[col2]):
                        result_details.append(f"{col1} mismatched")
                else:
                    result_details.append(f"{col1} Mismatched")
        
        if result_details:
            result_summary = ', '.join(result_details)
            result_df = result_df.append({'entityid': entityid, 'empid': empid, 'result_summary': result_summary}, ignore_index=True)
        else:
            result_df = result_df.append({'entityid': entityid, 'empid': empid, 'result_summary': 'Match'}, ignore_index=True)
    else:
        result_df = result_df.append({'entityid': entityid, 'empid': empid, 'result_summary': 'Entity id not available in File2'}, ignore_index=True)


entities_only_in_file2 = [(entityid, empid) for entityid, empid in zip(file2_df['entityid'], file2_df['empid'])
                         if (entityid, empid) not in zip(file1_df['entityid'], file1_df['empid'])]

for entityid, empid in entities_only_in_file2:
    result_df = result_df.append({'entityid': entityid, 'empid': empid, 'result_summary': 'Entity id not available in File1'},
                                ignore_index=True)

result_df.to_excel("Comparison_Result.xlsx", index=False)