import cv2
import pandas as pd
import numpy as np 
import requests
from io import BytesIO

# Read the Excel file
df = pd.read_csv("class_data.csv")
print(df.columns)

