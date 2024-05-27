import uuid

print(uuid.uuid4())
data = [
    {
        "_id": "70242ab7-55f1-4061-b990-95b736c078ce",
        "pdmId": "LPHD1_InstallationFromBrk",
        "edmId": "mountingPosition",
        "edmPath": "electrical._links",
        "function": "category"
    },
    {
        "_id": "45a45a2a-35d1-4b50-ad08-25217034665f",
        "pdmId": "LPHD1_CircuitID",
        "edmId": "label",
        "edmPath": "label",
        "function": "category"
    },
    {
        "_id": "0623a031-3ed9-4445-be31-e33e28ed38fb",
        "pdmId": "LPHD1_UserAppliName",
        "edmId": "label",
        "edmPath": "label",
        "function": "category"
    },
    {
        "_id": "e733bd3b-84f6-4cef-b564-65ef4cdc63fc",
        "pdmId": "LPHD1_ProductCode",
        "edmId": "range",
        "edmPath": "identification.range",
        "function": "category"
    },
    {
        "_id": "bc4c6570-43d9-49a9-b44d-21a62b7ae9b0",
        "pdmId": "LPHD1_ARtg",
        "edmId": "ratedCurrent",
        "edmPath": "electrical.ratedCurrent",
        "function": "category"
    },
    {
        "_id": "698004fb-7ba3-4258-8b51-f9ec6b55eb92",
        "pdmId": "LPHD1_PhsRot",
        "edmId": "slot1Phase",
        "edmPath": "",
        "function": "category"
    },
    {
        "_id": "672f11f2-6a6b-445f-b306-8c5778d6b03e",
        "pdmId": "LPHD1_PowSupCfg",
        "edmId": "powerSupply",
        "edmPath": "",
        "function": "category"
    },
    {
        "_id": "67a03e18-cdd9-478f-a32e-a8ce0ad2ef80",
        "pdmId": "LPHD1_Usage",
        "edmId": "usage",
        "edmPath": "usages[0]._id",
        "function": "category"
    },
    {
        "_id": "7e7e6cb3-c317-41ed-a96d-ccdd8554ba19",
        "pdmId": "MBSL_LCCH1_Address",
        "edmId": "address",
        "edmPath": "port.address",
        "function": "category"
    },
    {
        "_id": "73159196-b14b-4578-a3bf-ff0e44ecc3b8",
        "pdmId": "pdmShortNameID-Loadname",
        "edmId": "name",
        "edmPath": "electrical.load.name",
        "function": "category"
    },
    {
        "_id": "224e1f31-ea0d-4d36-98be-bd104008680c",
        "pdmId": "pdmShortNameID-Zone",
        "edmId": "zone",
        "edmPath": "electrical.load.zone",
        "function": "category"
    },
    {
        "_id": "a643ce32-a58f-420b-9ea2-3c3426dfc04d",
        "pdmId": "OpTimeLoadPStrVal",
        "edmId": "worksWhenPower",
        "edmPath": "electrical.load.worksWhenPowerGreaterThan",
        "function": "category"
    },
    {
        "_id": "822476e9-9437-4b89-b526-62910fe6e9f4",
        "pdmId": "pdmShortNameID-TripCurve",
        "edmId": "tripCurveType",
        "edmPath": "electrical.tripCurveType",
        "function": "category"
    },
    {
        "_id": "c94b5e72-098d-49f8-9d88-60c1040febae",
        "pdmId": "CALH1_IOverloadAlm",
        "edmId": "overThreshold",
        "edmPath": "pickupThreshold",
        "function": "alarm"
    },
    {
        "_id": "d29e6194-0151-4c03-a264-6ad23ba0c961",
        "pdmId": "CALH1_OverVAlm",
        "edmId": "overVoltage",
        "edmPath": "pickupThreshold",
        "function": "alarm"
    },
    {
        "_id": "621663cb-4007-467a-adc3-5838c9a2c980",
        "pdmId": "CALH1_AEFAlm",
        "edmId": "earthLeakage",
        "edmPath": "pickupThreshold",
        "function": "alarm"
    },
    {
        "_id": "4f616855-2944-43b4-9b39-4b9ae451b514",
        "pdmId": "pdmShortNameID-IsIncomer",
        "edmId": "isIncomer",
        "edmPath": "electrical.isIncomer",
        "function": "category"
    },
    {
        "_id": "6454b483-d51a-4e12-90ba-96b4756d6d8c",
        "pdmId": "pdmShortNameID-PowerFactorSign",
        "edmId": "powerFactorSign",
        "edmPath": "electrical.powerFactorSign",
        "function": "category"
    },
    {
        "_id": "aeba04e9-6bc9-4214-8c04-cdf1f98c7c1b",
        "pdmId": "pdmShortNameID-RatedVoltage",
        "edmId": "ratedVoltage",
        "edmPath": "electrical.ratedVoltage",
        "function": "category"
    },
    {
        "_id": "655d4186-8347-4034-b60a-b5b01f295e7d",
        "pdmId": "pdmShortNameID-SystemType",
        "edmId": "neutralVT",
        "edmPath": "electrical.neutralVT",
        "function": "category"
    },
    {
        "_id": "90fa77fa-e1d1-4674-aba2-7427e218a137",
        "pdmId": "pdmShortNameID-Equipment",
        "edmId": "value",
        "edmPath": "settings[0].value",
        "function": "category"
    },
    {
        "_id": "f9776a26-df98-4999-8405-c66800126764",
        "pdmId": "pdmShortNameID-Sensor",
        "edmId": "value",
        "edmPath": "settings[0].value",
        "function": "category"
    },
    {
        "_id": "5100096a-8b20-4d47-b196-4c0f428f0151",
        "pdmId": "pdmShortNameID-MeasuredPoint",
        "edmId": "value",
        "edmPath": "settings[0].value",
        "function": "category"
    },
    {
        "_id": "72aab977-2bff-422e-a314-452a3393366f",
        "pdmId": "pdmShortNameID-CubicleType",
        "edmId": "value",
        "edmPath": "settings[0].value",
        "function": "category"
    },
    {
        "_id": "ead4b160-1fb9-485b-9bfc-6d617b388984",
        "pdmId": "pdmShortNameID-CubicleId",
        "edmId": "value",
        "edmPath": "settings[0].value",
        "function": "category"
    },
    {
        "_id": "a749faec-279a-485d-b0fc-7a593b900f7f",
        "pdmId": "pdmShortNameID-DrawerId",
        "edmId": "value",
        "edmPath": "settings[0].value",
        "function": "category"
    },
    {
        "_id": "248df972-f100-4975-af03-286dee5c1f8b",
        "pdmId": "pdmShortNameID-AssetName",
        "edmId": "name",
        "edmPath": "name",
        "function": "category"
    },
    {
        "_id": "525c3d1f-116d-4367-a7c8-093c16e35f82",
        "pdmId": "pdmShortNameID-CircuitBreakerId",
        "edmId": "value",
        "edmPath": "settings[0].value",
        "function": "category"
    },
    {
        "_id": "7a83cfad-b71f-43b8-85fc-47966fb76795",
        "pdmId": "pdmShortNameID-FeederId",
        "edmId": "value",
        "edmPath": "settings[0].value",
        "function": "category"
    }
]
print(data)