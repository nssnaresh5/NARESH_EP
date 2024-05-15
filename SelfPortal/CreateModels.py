data = {
  "pdmData": {
    "LPHD1_CircuitID": "Circuit ID",
    "LPHD1_UserAppliName": "User Application Name",
    "LPHD1_ARtg": "Rated Current",
    "LPHD1_PhsRot": "Phase Rotation",
    "LPHD1_Usage": "Usage",
    "MBSL_LCCH1_Address": "Address",
    "pdmShortNameID-Zone": "Zone",
    "pdmShortNameID-IsIncomer": "Is Incomer",
    "pdmShortNameID-PowerFactorSign": "Power Factor Sign",
    "pdmShortNameID-Equipment": "Equipment",
    "pdmShortNameID-MeasuredPoint": "Measured Point",
    "pdmShortNameID-CubicleType": "Cubicle Type",
    "pdmShortNameID-CubicleId": "Cubicle ID",
    "pdmShortNameID-AssetName": "Asset Name",
    "pdmShortNameID-CircuitBreakerId": "Circuit Breaker ID",
    "LPHD1_InstallationFromBrk": "Installation From Breaker",
    "LPHD1_ProductCode": "Product Code",
    "LPHD1_PowSupCfg": "Power Supply Configuration",
    "pdmShortNameID-Loadname": "Load Name",
    "OpTimeLoadPStrVal": "Operating Time Load Pickup Start Value",
    "pdmShortNameID-TripCurve": "Trip Curve",
    "pdmShortNameID-RatedVoltage": "Rated Voltage",
    "pdmShortNameID-SystemType": "System Type",
    "pdmShortNameID-Sensor": "Sensor",
    "pdmShortNameID-DrawerId": "Drawer ID",
    "pdmShortNameID-FeederId": "Feeder ID"
  }
}

new_data = []

for key, value in data["pdmData"].items():
    new_data.append({
        "pdmShortName": key,
        "columnName": value,
        "type": "string"
    })

print(new_data)