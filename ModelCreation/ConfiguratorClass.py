from __future__ import annotations
from enum import Enum
from dataclasses import dataclass

import os
from typing import List, Optional, Dict, Any

from pydantic import BaseModel


class ParamType(str, Enum):
    NoneType = "None"
    FromClientApp = "FromClientApp"
    PathRef = "PathRef"
    Direct = "Direct"


class RefType(str, Enum):
    ListWithCondition = "ListWithCondition"
    ListWithConditionOnResponse = "ListWithConditionOnResponse"
    Direct = "Direct"
    PreviousResponse = "PreviousResponse"
    Static = "Static"


class RequestType(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"


class ConditionOperator(str, Enum):
    Equals = "Equals"
    NotEquals = "NotEquals"


class Condition(BaseModel):
    propertyName: Optional[str] = None
    operator: Optional[ConditionOperator] = None
    value: Optional[str] = None


class Params(BaseModel):
    paramName: Optional[str] = None
    paramsType: Optional[ParamType] = None
    refType: Optional[str] = None
    rank: Optional[int] = None
    path: Optional[str] = None
    conditions: Optional[List[Condition]] = None


class Services(BaseModel):
    globalVariable: Optional[str] = None
    reqType: Optional[RequestType] = None
    serviceUrl: Optional[str] = None
    rank: Optional[int] = None
    params: Optional[List[Params]] = None
    preConditions: Optional[List[Params]] = None
    response: Optional[Dict] = None
    requestBody: Optional[Any] = None
    value: Optional[Any] = None

    """
    globalVariable: Any = None
    reqType: RequestType
    serviceUrl: str
    rank: int
    params: List[Params]
    preConditions: Optional[List[Params]] = None
    response: Any = None
    requestBody: Any = None
    value: Any = None
    """


class CommonDeviceAttributes(BaseModel):
    id: Optional[str] = None
    globalVariables: Optional[List[str]] = None
    services: Optional[List[Services]] = None


class Category(BaseModel):
    id: Optional[str] = None
    pdmShortNameIds: Optional[List[str]] = None
    read: Optional[Read] = None
    write: Optional[Write] = None


class ServiceMapping(BaseModel):
    commonDeviceAttributes: Optional[CommonDeviceAttributes] = None
    categories: Optional[List[Category]] = None
    alarms: Optional[List[Category]] = None


class Attribute(BaseModel):
    value: Optional[str] = None
    rank: Optional[int] = None
    path: Optional[str] = None


class AdvancedSetting(BaseModel):
    pdmShortNameId: Optional[str] = None
    attribute: Optional[Attribute] = None
    dependentSettings: Optional[List] = None
    dependentResponseValues: Optional[List[Attribute]] = None
    possibleDerivedValues: Optional[List[Dict]] = None


class Read(BaseModel):
    protocol: Optional[str] = None
    services: Optional[List[Services]] = None
    id: Optional[str] = None
    advancedSettings: Optional[List[AdvancedSetting]] = []


class Write(BaseModel):
    protocol: Optional[str] = None
    services: Optional[List[Services]] = None
    id: Optional[str] = None
    advancedSettings: Optional[List[AdvancedSetting]] = []


class AdvancedSettingsConfig(BaseModel):
    read: Optional[List[Read]] = None
    write: Optional[List[Write]] = None


class ConfiguratorModel(BaseModel):
    serviceMapping: Optional[ServiceMapping] = None
    advancedSettingsConfig: Optional[AdvancedSettingsConfig] = None
    dictionaryConfig: Optional[List[Dict]] = None






