deviceFamily = [
    {
        "_id": "cc694df1-44db-4753-9b85-4ff480fe764b",
        "key": "Power meter",
        "value": "Energy",
        "type": "devicefamily",
        "isActive": True,
        "subItemIds": []
    },
    {
        "_id": "c4f144e1-3259-476d-a85e-0e1e0d34d893",
        "key": "Other",
        "value": "Other",
        "type": "devicefamily",
        "isActive": True,
        "subItemIds": []
    },
    {
        "_id": "1d7aed53-b8f2-4ff7-bb89-6287a7163220",
        "key": "Control",
        "value": "Control",
        "type": "devicefamily",
        "isActive": True,
        "subItemIds": []
    },
    {
        "_id": "c0a3dae3-00bd-4f24-b890-fde58b433376",
        "key": "Ambient sensor",
        "value": "Ambient",
        "type": "devicefamily",
        "isActive": True,
        "subItemIds": []
    },
    {
        "_id": "b3f17d67-1593-4fee-be85-c9c8db8226ed",
        "key": "Circuit Breaker",
        "value": "Wireless Protection",
        "type": "devicefamily",
        "isActive": True,
        "subItemIds": []
    },
    {
        "_id": "b3f17d67-1593-4fee-be85-c9c8db8226ed",
        "key": "Cond. Monitoring",
        "value": "Cond. Monitoring",
        "type": "devicefamily",
        "isActive": True,
        "subItemIds": []
    },
    {
        "_id": "b3f17d67-1593-4fee-be85-c9c8db8226ed",
        "key": "I/O Device",
        "value": "I/O Device",
        "type": "devicefamily",
        "isActive": True,
        "subItemIds": []
    },
    {
        "_id": "b3f17d67-1593-4fee-be85-c9c8db8226ed",
        "key": "Schneider Electric",
        "value": "Schneider Electric",
        "type": "devicefamily",
        "isActive": True,
        "subItemIds": []
    }
]

categoryName = {
    "Associated breaker settings": [
        "Associated breaker label",
        "Mounting position",
        "Breaker reference",
        "Rated voltage",
        "Rated current",
        "Load name",
        "Load zone",
        "Load works",
        "Trip curve type"
    ],
    "Device settings": [
        "Device label",
        "Asset name"
    ],
    "Ambient settings": [
        "Equipment",
        "Sensor position",
        "Measured point",
        "Cubicle type",
        "Cubicle id",
        "Drawer id"
    ],
    "Alarm settings": [
        "Over load threshold",
        "Over voltage threshold",
        "Earth leakage tripping"
    ],
    "Power settings": [
        "System type",
        "PF sign",
        "Power supply",
        "Current direction",
        "Phase sequence"
    ],
    "Communication": [
        "Modbus address"
    ],
    "Usage": [
        "Usage"
    ]
}


def get_devicefamily_with_value(value):
    for device in deviceFamily:
        if device['key'].lower() == value.lower():
            return device['value']
    return None
