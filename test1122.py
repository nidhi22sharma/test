#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:44:50 2023

@author: nidhisharma
"""

import pandas as pd

# Load both DataFrames with your actual data
file1_df = pd.read_excel("File1.xlsx")
file2_df = pd.read_excel("File2.xlsx")

print("file1_df",file1_df)
print("file2_df",file2_df)


# Create a function to compare two values while handling various data types and formats
def compare_values(val1, val2):
    if pd.isna(val1) and pd.isna(val2):
        return True
    elif (isinstance(val1, (int, float)) or str(val1).isdigit()) and (isinstance(val2, (int, float)) or str(val2).isdigit()):
        # Compare numeric values regardless of format
        return float(val1) == float(val2)
    else:
        # Compare non-numeric values without considering case and leading/trailing spaces
        return str(val1).strip().lower() == str(val2).strip().lower()

# Initialize an empty result DataFrame
result_df = pd.DataFrame(columns=['entityid', 'result_summary'])

# Iterate through rows in File1 and compare with File2
for index, row1 in file1_df.iterrows():
    entityid = row1['entityid']
    
    if entityid in file2_df['entityid'].values:
        row2 = file2_df[file2_df['entityid'] == entityid].iloc[0]
        
        result_details = []
        
        for col1 in file1_df.columns:
            if col1 != 'entityid':
                # Find the corresponding column in File2 based on data type and value
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
            result_df = result_df.append({'entityid': entityid, 'result_summary': result_summary}, ignore_index=True)
        else:
            result_df = result_df.append({'entityid': entityid, 'result_summary': 'Match'}, ignore_index=True)
    else:
        result_df = result_df.append({'entityid': entityid, 'result_summary': 'Entity id not available in File2'}, ignore_index=True)

# Identify entities in File2 that are not in File1
entities_only_in_file2 = [entityid for entityid in file2_df['entityid'] if entityid not in file1_df['entityid'].values]
for entityid in entities_only_in_file2:
    result_df = result_df.append({'entityid': entityid, 'result_summary': 'Entity id not available in File1'}, ignore_index=True)

# Save the result to a new Excel file
result_df.to_excel("Comparison_Result.xlsx", index=False)



