from dataclasses import dataclass, field
from typing import List
from pydantic import BaseModel


@dataclass
class Range:
    min: int
    max: int
    stepValue: int


@dataclass
class Mapping:
    key: str = ""
    value: str = ""


@dataclass
class Settings:
    id: str
    name: str
    inputType: str
    defaultValue: str
    unitSymbol: str
    helpText: str = None
    isMandatory: bool = False
    range: Range = None
    values: List[Mapping] = None
    isReadOnly: bool = False
    deviceValue: str = ""


@dataclass
class Categories:
    id: str
    name: str
    settings: List[Settings]


@dataclass
class DeviceModel:
    deviceImage: str = ''
    categories: [Categories] = field(default_factory=list)
    alarms: [Categories] = field(default_factory=list)
    Usages: List[Mapping] = field(default_factory=list)
    ZigbeeId: str = ""
    Name: str = ""
    Label: str = ""
    CommercialReference: str = ""
    SerialNumber: str = ""
    Range: str = ""
    Model: str = ""
    IsSelected: bool = False
    IsDeviceModelAvailable: bool = False
    Family: str = ""
    addr: str = ""
