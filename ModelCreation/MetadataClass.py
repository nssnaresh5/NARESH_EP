

from __future__ import annotations

import os
from typing import List, Optional

from pydantic import BaseModel, Field


class Value(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None


class DependentSettingValue(BaseModel):
    pdmShortNameID_Equipment: Optional[str] = Field(
        None, alias='pdmShortNameID-Equipment'
    )
    pdmShortNameID_Sensor: Optional[str] = Field(None, alias='pdmShortNameID-Sensor')


class PossibleDerivedValue(BaseModel):
    # dependentSettingValues: Optional[List[DependentSettingValue]] = None
    dependentSettingValues: Optional[List[dict]] = []
    values: Optional[List[Value]] = []
    range: Optional[Range] = None


class LogicalMapping(BaseModel):
    derivedSetting: Optional[str] = None
    dependentSettings: Optional[List[str]] = []
    possibleDerivedValues: Optional[List[PossibleDerivedValue]] = []
    logicalOperation: Optional[str] = None


class DictionaryConfig(BaseModel):
    pdmShortNameId: Optional[str] = None
    logicalMapping: Optional[List[LogicalMapping]] = []


class FieldValidation(BaseModel):
    minLength: Optional[int] = None
    maxLength: Optional[int] = None
    regularExpression: Optional[str] = None


class Range(BaseModel):
    isNoneAvailable: Optional[bool] = None
    min: Optional[int] = None
    max: Optional[int] = None
    stepValue: Optional[int] = None


class Setting(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    inputType: Optional[str] = None
    values: Optional[List[Value]] = []
    fieldValidation: Optional[FieldValidation] = None
    defaultValue: Optional[str] = None
    unitSymbol: Optional[str] = None
    deviceValue: Optional[str] = None
    helpText: Optional[str] = None
    isMandatory: Optional[bool] = None
    isReadOnly: Optional[bool] = None
    logicalMapping: Optional[List[str]] = []
    range: Optional[Range] = None
    scaleFactor: Optional[int] = None


class Category(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    settings: Optional[List[Setting]] = []


class Alarm(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    settings: Optional[List[Setting]] = []


class Configuration(BaseModel):
    categories: Optional[List[Category]] = []
    alarms: Optional[List[Alarm]] = []


class Identification(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None


class Device(BaseModel):
    identification: Optional[List[Identification]] = []
    configuration: Optional[Configuration] = None
    dictionaryConfig: Optional[List[DictionaryConfig]] = []
    deviceImageId: Optional[str] = None
    deviceImageUrl: Optional[str] = None


class MetadataModel(BaseModel):
    device: Optional[Device] = None




