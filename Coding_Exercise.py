import pandas as pd
import numpy as np
import argparse

def parseMetaData(file):
	"""
	Parse the metadata file for countries with the region of Sub Saharan
	Africa. Output to dictionary for efficient lookup.
	"""
	subSaharan = {} #Dictionary for region look up
	meta = pd.read_csv(file,header = 0) #Read in data from specified file
	[subSaharan[meta.loc[i,"Country Name"]=meta.loc[i,"Region"] for i in range(meta.shape[0]) if meta.loc[i,"Region"] == "Sub-Saharan Africa"]
	return subSaharan

print parseMetaData("/Users/scottkellert/Google_Drive/Nielsen/Python Exercise Package/data_files/Metadata_Country.csv")