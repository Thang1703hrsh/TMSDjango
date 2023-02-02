import requests
from datetime import datetime
import time
import psutil
import json
import pandas as pd

# REST_API_URL = 'https://api.powerbi.com/beta/f6485721-951c-4db9-b0ac-15e553069c0f/datasets/8f102ddd-d3f8-4017-b718-3e1d54916edf/rows?key=gsHeEy1Twc3W90GT%2FVk%2FR%2FFa7ebHUV9el6jcz4RlAW%2FIvkmXm73HgpzGSoXGSUiMfj3vIOIDd1NPaBfTMroimA%3D%3D'


REST_API_URL = 'https://api.powerbi.com/beta/f6485721-951c-4db9-b0ac-15e553069c0f/datasets/fa1b7bb3-643d-4293-bfc7-2e18ec95f16d/rows?key=Ons9O2MPq71u5wFbf%2B0O5E6vGihwAbHJX8F1DuoutliaCssW1DkTArIl15uS3oGFKJY2X%2Bl0CnBQFfwkDGwo%2BA%3D%3D'
data = pd.read_excel("ProductUnit.xlsx")

json_data = bytes(data.to_json(orient='records'), encoding='utf-8')
# print(json_data)
res = requests.post(REST_API_URL,json_data)
print("Data posted in Power BI API")

time.sleep(5)