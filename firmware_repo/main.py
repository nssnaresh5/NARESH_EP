from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="ETPX Firmware Repository Service API",
    version="v1",
    description="""
The Firmware Repository Service enables panel builders and electricians to find and download device firmware files in order to carry out device firmware upgrade.
Firmware is software that is embedded in a device's hardware and controls its operation. Firmware updates are often necessary to fix bugs, add new features, or improve performance.

A firmware repository service can be used to:
- Get the firmware binary from the cloud based on the commercial reference and version of the firmware binary
- Distribute firmware images to devices in a secure and efficient manner.

**Authentication Information**\n
Access to all Commissioning services will be through authentication services provided by Schneider’s Identity Management System (IDMS) and the Azure APIM Gateway access. Access to the vast majority of the 
CommissioningAPI endpoints require both an IDMS and application key(x-api-key), from the consuming application, to access the Commissioning Services. However, there are a few pre-approved exceptions for specific clients 
and Commisioning endpoints, where only the ApplicationKey(x-api-key) is required. Application Keys are generated from Azure APIM and assigned to consumer applications. The App Key is mandatory for all clients requesting 
connections to the Commissioning APIs. IDMS Tokens are generated and acquired based on the client’s integration with Schneider IDMS,when the user logs into the Schneider domain from the client application. This User token is 
passed during the request to the specific Commissioning Endpoint. All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.

**API Key: App Token**

**Security Scheme Type:** API Key\n
**Header Parameter Name:** x-api-key\n\n

**API Key: IDMS Token**

**Security Scheme Type:** API Key\n
**Header Parameter Name:** Authorization\n\n
""",
    openapi_tags=[
        {
            "name": "Firmware Repository",
            "description": "The Firmware Repository Service"
        }
    ],
    servers=[
        {
            "url": "https://etpx-firmware-repo-service.azurewebsites.net",
            "description": "Production Server"
        }
    ],
    contact={
        "name": "ETPX Commissioning Service Team",
        "email": "naresh.s@se.com"
    },
    openapi_url="/api/v1/openapi.json",

)

class ApiResponse(BaseModel):
    message: str

class GetFirmwareListResponse(BaseModel):
    downloadUrl: str
    checkSumSHA256: str
    version: str
    description: str
    fileExtension: str
    fileName: str
    lastModifiedDate: str

@app.get("/FirmwareRepository/list", tags=["Firmware Repository"], response_model=GetFirmwareListResponse,)
async def get_firmware_list(commercialReference: str):
    """
    This API retrieves a list of firmware versions for a given commercial reference.\r\n<br /><br />API response: <br /><b>downloadUrl:</b> firmware file download link. <br /><b>checkSumSHA256:</b> SHA256 Hascode to get integrity of downloaded file from download link.<br /><b>version:</b> Firmware version.<br /><b>description:</b> Description of firmware version.<br /><b>fileExtension:</b> Extension of firmware file.<br /><b>fileName:</b> Name of firmware file.<br /><b>lastModifiedDate:</b> Last modified date of firmware file in UTC format.<br />
    """
    if not commercialReference:
        raise HTTPException(status_code=404, detail="Invalid request. Commercial reference is missing or invalid")
    elif commercialReference == "invalid":
        raise HTTPException(status_code=400, detail="Firmware versions not found due to invalid commercial reference or non-availability of files")

    
    return GetFirmwareListResponse(
        downloadUrl="http://example.com",
        checkSumSHA256="abc123",
        version="1.0.0",
        description="Firmware version 1.0.0",
        fileExtension=".bin",
        fileName="firmware.bin",
        lastModifiedDate="2022-01-01T00:00:00Z"
    )