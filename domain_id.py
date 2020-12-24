import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import os

data = pd.read_excel(open('/home/user/Downloads/Old_Articles_Redirection.xlsx'))
df = pd.DataFrame(data, columns= ['OLD Article Url', 'URL to Redirect'])
print(df)