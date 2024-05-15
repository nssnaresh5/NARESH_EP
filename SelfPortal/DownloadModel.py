import os, json, requests

modelFolder = "Downloaded_models/"
portalURL = "https://wap-etpx-commission-diservice-qa-v1.azurewebsites.net/"


def DownloadDriverMetaData(CommercialRefNo):
    try:
        return requests.get(portalURL + "/driverExport/metadata?commercialReferenceNo=" + CommercialRefNo).json()
    except:
        return False


def DownloadDriverConfigurator(CommercialRefNo):
    try:
        return requests.get(portalURL + "/driverExport/configurator?commercialReferenceNo=" + CommercialRefNo).json()
    except:
        return False


def SaveDriverFiles(CommercialRefNo) -> bool:
    try:
        if not os.path.exists(modelFolder + CommercialRefNo):
            meta_res = DownloadDriverMetaData(CommercialRefNo)
            config_res = DownloadDriverConfigurator(CommercialRefNo)
            if meta_res and config_res:
                os.makedirs(modelFolder + CommercialRefNo, exist_ok=True)
                json_object_metadata = json.dumps(meta_res, indent=2)
                json_object_config = json.dumps(config_res, indent=2)
                with open(modelFolder + "/" + CommercialRefNo + "/" + CommercialRefNo + "_metadata.json", "w") as outfile:
                    outfile.write(json_object_metadata)
                with open(modelFolder + "/" + CommercialRefNo + "/" + CommercialRefNo + "_configurator.json", "w") as outfile:
                    outfile.write(json_object_config)
                return True
            else:
                return False
        else:
            print(f"{CommercialRefNo} Device models already available in Local machine")
            return True
    except:
        return False


# SaveDriverFiles("A9TAB2640")
# SaveDriverFiles("A9TPED625")
# SaveDriverFiles("A9MEM1520")
SaveDriverFiles("A9MEM1543")
# SaveDriverFiles("EMS59440")
