from typing import Union
from fastapi import FastAPI

app = FastAPI(
    title="ETPX Firmware Repository Service API", 
    version="v1", 
    description="""
    The Firmware Repository Service enables panel builders and electricians to find and download device firmware files in order to carry out device firmware upgrade.
    Firmware is software that is embedded in a device's hardware and controls its operation. Firmware updates are often necessary to fix bugs, add new features, or improve performance.

    A firmware repository service can be used to:
    - Get the firmware binary from the cloud based on the commercial reference and version of the firmware binary
    - Distribute firmware images to devices in a secure and efficient manner.

    *Authentication Information*
    Access to all Commissioning services will be through authentication services provided by Schneider’s Identity Management System (IDMS) and the Azure APIM Gateway access. Access to the vast majority of the CommissioningAPI endpoints require both an IDMS and application key(x-api-key), from the consuming application, to access the Commissioning Services. However, there are a few pre-approved exceptions for specific clients and Commisioning endpoints, where only the ApplicationKey(x-api-key) is required. Application Keys are generated from Azure APIM and assigned to consumer applications. The App Key is mandatory for all clients requesting connections to the Commissioning APIs. IDMS Tokens are generated and acquired based on the client’s integration with Schneider IDMS,when the user logs into the Schneider domain from the client application. This User token is passed during the request to the specific Commissioning Endpoint. All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.
    """
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}