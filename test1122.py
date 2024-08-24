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

# Create a function to compare two values while handling various data types and formats
def compare_values(val1, val2):
    if pd.isna(val1) and pd.isna(val2):
        return True
    elif (isinstance(val1, (int, float)) or str(val1).isdigit()) and (isinstance(val2, (int, float)) or str(val2).isdigit()):
        # Compare numeric values regardless of format
        val1 = float(val1) if isinstance(val1, (int, float)) else val1
        val2 = float(val2) if isinstance(val2, (int, float)) else val2
        return val1 == val2
    else:
        # Compare non-numeric values without considering case and leading/trailing spaces
        return str(val1).strip().lower() == str(val2).strip().lower()

# Initialize an empty result DataFrame
result_df = pd.DataFrame(columns=['entityid', 'empid', 'result_summary'])

# Iterate through rows in File1 and compare with File2
for index, row1 in file1_df.iterrows():
    entityid = row1['entityid']
    empid = row1['empid']
    
    if (entityid, empid) in file2_df[['entityid', 'empid']].apply(tuple, axis=1).values:
        row2 = file2_df[(file2_df['entityid'] == entityid) & (file2_df['empid'] == empid)].iloc[0]
        
        result_details = []
        
        for col1 in file1_df.columns:
            if col1 not in ['entityid', 'empid']:
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
            result_df = result_df.append({'entityid': entityid, 'empid': empid, 'result_summary': result_summary}, ignore_index=True)
        else:
            result_df = result_df.append({'entityid': entityid, 'empid': empid, 'result_summary': 'Match'}, ignore_index=True)
    else:
        result_df = result_df.append({'entityid': entityid, 'empid': empid, 'result_summary': 'Entity id not available in File2'}, ignore_index=True)

# Identify entities in File2 that are not in File1
entities_only_in_file2 = [(entityid, empid) for entityid, empid in zip(file2_df['entityid'], file2_df['empid']) if (entityid, empid) not in zip(file1_df['entityid'], file1_df['empid'])]
for entityid, empid in entities_only_in_file2:
    result_df = result_df.append({'entityid': entityid, 'empid': empid, 'result_summary': 'Entity id not available in File1'}, ignore_index=True)

# Save the result to a new Excel file
result_df.to_excel("Comparison_Result.xlsx", index=False)


cc


#include <stdio.h>
#include <stdlib.h>
#include "Python.h"  // Include the Python API header

Action()
{
    lr_output_message("I am going to execute python script using Python C API");

    // Initialize the Python interpreter
    Py_Initialize();

    // Define the Python code as a string
    const char *pythonScript =
        "def main():\n"
        "    with open('D:\\\\testing_app_dev\\\\selenium_suite\\\\apptio\\\\LRE_log', 'a') as LRE_log:\n"
        "        print('Hello I have executed Python script!', file=LRE_log)\n"
        "\n"
        "if __name__ == '__main__':\n"
        "    main()\n";

    // Execute the Python script
    int result = PyRun_SimpleString(pythonScript);
    if (result == 0)
    {
        lr_output_message("Python script executed successfully using Python C API");
    }
    else
    {
        lr_error_message("Failed to execute python script using Python C API");
    }

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}


var isTextVisible = false;  // Boolean to track if the text is visible
var maxRetries = 5;  // Maximum number of retries to avoid infinite loops
var retryCount = 0;  // Counter for retries

// Start the loop
for (retryCount = 0; retryCount < maxRetries; retryCount++) {

    // Navigate to the page
    window.location.href = "https://yoururl.com";  // Replace with your actual URL

    // Wait for the page to load
    Wait(5);  // Wait for 5 seconds, adjust as needed

    // Check if the text is visible
    isTextVisible = evalXPath("//span[text()='YourTextHere']").exists();  // Replace with actual XPath for the text

    if (isTextVisible) {
        lr.output_message("Text is visible. Proceeding with the script.");
        break;  // Exit the loop if the text is visible
    } else {
        lr.output_message("Text not visible. Attempting to navigate again.");
    }
}

// After the loop, check if the text was found
if (!isTextVisible) {
    lr.error_message("Text was not found after " + maxRetries + " attempts.");
    // Handle this scenario (e.g., fail the script or take another action)
}

// Continue with the rest of your script


