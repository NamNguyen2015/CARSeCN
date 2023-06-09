#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:15:55 2022

@author: namnguyen
"""
import numpy as np
import streamlit as st
import json
import pandas as pd
import os
from collections import defaultdict
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import CARSEC as CS
from zipfile import ZipFile
import tempfile


#%%%%%%%%%%%%%%%%%%
st.subheader('Download Excel Template input')
with open("Input_files/CARSEC_excel.xlsx", "rb") as fp:
	btn = st.download_button(label="Download Excel Template",data=fp,file_name="CARSEC_Excel_Input.xlsx",mime="application/xlsx")
#%%%%%%%%%%%%%%%%%%%	
st.subheader('Upload your own Excel file')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	st.write('Data preview')
	_tables=pd.read_excel(uploaded_file,sheet_name=None)
	for k in _tables:  
		st.write(_tables[k])
#%%%%%%%%%%%%%%%%%%%
st.subheader('Download Muti CARSEC files')

# if uploaded_file is not None:
# 	multi_name_file = tempfile.gettempdir()
# 	#CS.CARSEC_Writer(DB=DB, export_path=name_file)
# 	CS.excel_to_CARSEC(load_path=uploaded_file,export_path=multi_name_file+'/CS_Multi_')	

#dirs=tempfile.gettempdir()

# st_directory_picker()

# path=os.walk("Output_files/Multi_CARSEC/CS_Multi_")
# for (root,dirs,files) in os.walk('.', topdown=True):
#         print (root)
#         print (dirs)
#         print (files)
#         print ('--------------------------------')
# if uploaded_file is not None:
# 	CS.excel_to_CARSEC(load_path=uploaded_file,export_path=str(path))

# path2=os.walk("Output_files/Multi_CARSEC")
# # dirs = os.listdir(path)
# st.write(path2)
# with ZipFile('CARSEC_multi.zip', 'w') as zipObj:
# 	# Add multiple files to the zip
# 	for file in path2:
# 		st.write(file)
# 		zipObj.write(file)
	
# with open('CARSEC_multi.zip', "rb") as fp:
# 	btn = st.download_button(label='Download CARSEC files',data=fp,file_name="CARSEC_multi.zip",mime="application/ZIP")


# zip_path=tempfile.gettempdir()
# with ZipFile('CARSEC_multi.zip', 'w') as zipObj:
#  	#Add multiple files to the zip
# 	for file in dirs:
		#print(file)
		#zip_path_files=tempfile.join(zip_path,file)
 		#zipObj.write(zip_path+'//'+file)


# with open(zip_path, "rb") as fp:
# 	btn = st.download_button(label='Download CARSEC files',data=fp,file_name="CARSEC_multi.zip",mime="application/ZIP")
	
		
#%%
#name_file = tempfile.gettempdir() + "/Carsec_AutoGenerated"
#CS.CARSEC_Writer(DB=DB, export_path=name_file)
#st.write(CS.CARSEC_Writer(DB=DB, export_path="Output_files/Carsec_AutoGenerated.txt"))


#st.subheader('Download data')
#name_file_txt = name_file + '.txt'
#with open(name_file_txt, "rb") as fp:
#	btn = st.download_button(label="Download Carsec Input file",data=fp,file_name="Carsec_AutoGenerated.txt",mime="application/txt")
	



#=============================================================================
path='/app/carsecn_applications/Output_files/Multi_CARSEC'
if os.path.exists(path):
	dirs = os.listdir(path)
	for file in dirs:
		os.remove(path+'/'+file)
		

if uploaded_file is not None:
	CS.excel_to_CARSEC(load_path=uploaded_file,export_path='/app/carsecn_applications/Output_files/Multi_CARSEC/CS_Multi_')


dirs = os.listdir(path)
with ZipFile('CARSEC_multi.zip', 'w') as zipObj:
	# Add multiple files to the zip
	for file in dirs:
		st.write(file)
		zipObj.write('Output_files/Multi_CARSEC'+'/'+file)
	
with open('CARSEC_multi.zip', "rb") as fp:
	btn = st.download_button(label='Download CARSEC files',data=fp,file_name="CARSEC_multi.zip",mime="application/ZIP")
# =============================================================================
	
	
	
	
	
