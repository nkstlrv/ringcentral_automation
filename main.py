import os
from dotenv import load_dotenv
from ringcentral import SDK

load_dotenv()


# RingCentral API Credentials 
SERVER_URL = os.getenv("SERVER_URL")

ACCOUNT_ID = os.getenv("ACCOUNT_ID")
EXTENSION_ID = os.getenv("EXTENSION_ID")
CLIENT_ID = os.getenv("CLIENT_ID")

USERNAME = os.getenv("USERNAME")
PASSWORD = os.gettenv("PASSWORD")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

EXTENSION = os.getenv("EXTENSION")


queryParams = {
    #'page': 000,
    #'perPage': 000
}

rcsdk = SDK(os.environ[CLIENT_ID], os.environ[CLIENT_SECRET], os.environ[SERVER_URL])
platform = rcsdk.platform()

platform.login(os.environ[USERNAME], os.environ[EXTENSION], os.environ[PASSWORD])

r = platform.get(f'/restapi/v1.0/account/{ACCOUNT_ID}/call-log', queryParams)


print(r)