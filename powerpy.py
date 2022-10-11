
#                                                                               _         _       
#                                                                              | |       | |      
#   _ __    ___ __      __ ___  _ __  _ __   _   _        _ __ ___    ___    __| | _   _ | |  ___ 
#  | '_ \  / _ \\ \ /\ / // _ \| '__|| '_ \ | | | |      | '_ ` _ \  / _ \  / _` || | | || | / _ \
#  | |_) || (_) |\ V  V /|  __/| |   | |_) || |_| |      | | | | | || (_) || (_| || |_| || ||  __/
#  | .__/  \___/  \_/\_/  \___||_|   | .__/  \__, |      |_| |_| |_| \___/  \__,_| \__,_||_| \___|
#  | |                               | |      __/ |                                               
#  |_|                               |_|     |___/                                                
#     __                ______  __ __                 ____
#    / /_  __  __      / ____ \/ // / _____________  / __/
#   / __ \/ / / /     / / __ `/ // /_/ ___/ ___/ _ \/ /_  
#  / /_/ / /_/ /     / / /_/ /__  __(__  |__  )  __/ __/  
# /_.___/\__, /      \ \__,_/  /_/ /____/____/\___/_/     
#       /____/        \____/                              

from modules import *

REST_API_URL = "https://api.powerbi.com/v1.0/"

def get_access_token(tenant_id, workspace_client_id, workspace_user, workspace_pwd):
	auth_url = f"https://login.microsoftonline.com/{tenant_id}"
	scopes = ["https://analysis.windows.net/powerbi/api/.default"]
	
	client = msal.PublicClientApplication(workspace_client_id, authority = auth_url)
	response = client.acquire_token_by_username_password(username=workspace_user, password=workspace_pwd, scopes=scopes)
	access_token = response.get('access_token')
	
	return access_token

def get_authorization_token(access_token):
	return f"Bearer {access_token}"

def get(pbi_rest_api_url, authorization, files = None):
	headers = {
		'Authorization': authorization
	}
	return requests.get(pbi_rest_api_url, headers=headers, files=files)

def get_token_usage(authorization):
	url = "https://api.powerbi.com/v1.0/myorg/availableFeatures"
	
	response = get(url, authorization)
	available_features = response.json()
	features = available_features['features']
	
	return features[1]['additionalInfo']['usage']