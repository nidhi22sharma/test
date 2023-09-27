#!/usr/bin/env python3
# -*- coding: utf-8 -*-



Created on Thu Sep 28 00:50:14 2023

import xml.etree.ElementTree as ET
import pandas as pd
from openpyxl import Workbook  # Ensure you have this module installed

tree = ET.parse("test.xml")
root = tree.getroot()

data_dict = {}

for list_element in root:
    list_name = list_element.tag
    for item in list_element.findall('./*'):
        cpid_element = item.find('contractid')
        instrumentid_element = item.find('instrumentid')
        
        if cpid_element is not None and instrumentid_element is not None:
            unique_key = f"{cpid_element.text}_{instrumentid_element.text}"
            
            if unique_key not in data_dict:
                data_dict[unique_key] = {'contractid': cpid_element.text, 'instrumentid': instrumentid_element.text}
                
            for sub_element in item:
                if sub_element.tag not in ['contractid', 'instrumentid'] and sub_element.text is not None:
                    data_dict[unique_key][f'{list_name}_{sub_element.tag}'] = sub_element.text
                    
df = pd.DataFrame.from_dict(data_dict, orient='index')
df.to_excel('report_output.xlsx', index=False)