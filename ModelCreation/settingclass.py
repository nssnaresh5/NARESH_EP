from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from MetadataClass import Value, Range, FieldValidation
class MAININCOMER(BaseModel):
    id: Optional[str] = "pdmShortNameID-IsIncomer"
    name: Optional[str] = "Main/incomer"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = [{"key": "True", "value": "ON"}, {"key": "False", "value": "OFF"}]
    defaultValue: Optional[str] = "False"
    helpText: Optional[str] = ""
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class REFERENCEOFBREAKER(BaseModel):
    id: Optional[str] = "LPHD1_ProductCode"
    name: Optional[str] = "Reference of breaker"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = []
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = ""
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class RATEDCURRENT(BaseModel):
    id: Optional[str] = "LPHD1_ARtg"
    name: Optional[str] = "Rate current"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = []
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = ""
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class RATEDVOLTAGE(BaseModel):
    id: Optional[str] = "pdmShortNameID-RatedVoltage"
    name: Optional[str] = "Rate voltage"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = []
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = ""
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class LOADNAME(BaseModel):
    id: Optional[str] = "pdmShortNameID-Loadname"
    name: Optional[str] = "Load name"
    inputType: Optional[str] = "Text"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = "Name of the load applied on the single line diagram (HVAC Motor, Strip Lighting, IT closet,...)."
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = {
        "minLength": 1,
        "maxLength": 65535,
        "regularExpression": ""
    }
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None
    shortname: Optional[str] = ""
    parametername: Optional[str] = ""
    addreport: Optional[bool] = True
    edit: Optional[bool] = True
    helpTextSelect: Optional[bool] = False


class LOADZONE(BaseModel):
    id: Optional[str] = "pdmShortNameID-Zone"
    name: Optional[str] = "Load zone"
    inputType: Optional[str] = "Text"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = ""
    helpText: Optional[
        str] = "Name a zone to subdivide a building. It is used to tag and aggregate all consumptions which are related to a zone in the building: floor 1; floor 2..."
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = {
        "minLength": 1,
        "maxLength": 65535,
        "regularExpression": ""
    }
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None
    shortname: Optional[str] = ""
    parametername: Optional[str] = ""
    addreport: Optional[bool] = True
    edit: Optional[bool] = True
    helpTextSelect: Optional[bool] = False


class LOADWORKS(BaseModel):
    id: Optional[str] = "OpTimeLoadPStrVal"
    name: Optional[str] = "Load works when power greater than (W)"
    inputType: Optional[str] = "Scale"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = None
    helpText: Optional[
        str] = "The load operating time counter increments only when the power is greater or equal to the set value. You can set the value between 10W and 15000W."
    range: Optional[Range] = {
        "min": 10,
        "max": 15000,
        "stepValue": 1,
        "isNoneApplicable": False
    }
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class ASSOCIATEDBREAKERLABEL(BaseModel):
    id: Optional[str] = "LPHD1_CircuitID"
    name: Optional[str] = "Associated breaker label"
    inputType: Optional[str] = "Text"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = ""
    helpText: Optional[
        str] = ""
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = {
        "minLength": 0,
        "maxLength": 5,
        "regularExpression": ""
    }
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None
    shortname: Optional[str] = ""
    parametername: Optional[str] = ""
    addreport: Optional[bool] = True
    edit: Optional[bool] = True
    helpTextSelect: Optional[bool] = False


class MOUNTINGPOSITION(BaseModel):
    id: Optional[str] = "LPHD1_InstallationFromBrk"
    name: Optional[str] = "Mounting position"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = []
    defaultValue: Optional[str] = "BOTTOM"
    helpText: Optional[
        str] = "Top : The sensor is mounted on the Top/Line of the protective device (circuit breaker or switch) Bottom : The sensor is mounted on the Bottom / Load of the protective device(circuit breaker or switch)."
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class TRIPCURVETYPE(BaseModel):
    id: Optional[str] = "pdmShortNameID-TripCurve"
    name: Optional[str] = "Trip curve type"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = [{"key": "B", "value": "B"}, {"key": "C", "value": "C"}]
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = ""
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class USAGE(BaseModel):
    id: Optional[str] = "LPHD1_Usage"
    name: Optional[str] = "Usage"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = [{"key": "Lighting", "value": "Lighting"}]
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = "Select load usage type. It is used to tag and aggregate all consumptions related to an usage for energy analysis: lighting, HVAC..."
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class POWERSUPPLY(BaseModel):
    id: Optional[str] = "LPHD1_PowSupCfg"
    name: Optional[str] = "Power supply"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = []
    defaultValue: Optional[str] = ""
    helpText: Optional[
        str] = "Top : The current flow is coming from the top / line power terminals of the protective device Bottom : The current flow is coming from the bottom / load power terminals of the protective device."
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class PHASESEQUENCE(BaseModel):
    id: Optional[str] = "LPHD1_PhsRot"
    name: Optional[str] = "Phase sequence"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = []
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = "For this device, you can select the phase on which the device is wired."
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class POWERFACTORSIGN(BaseModel):
    id: Optional[str] = "pdmShortNameID-PowerFactorSign"
    name: Optional[str] = "PF sign convention"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = [
        {
            "key": "IEC",
            "value": "IEC"
        },
        {
            "key": "IEEE",
            "value": "IEEE"
        }
    ]
    defaultValue: Optional[str] = "IEC"
    helpText: Optional[
        str] = "IEC: PF sign indicates if active power is delivered (+) or received (-). PF takes the same sign as Active power P. default value. IEEE: PF sign indicates if the installation is lagging (-) or leading(+). Commonly used in North America."
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class SYSTEMTYPE(BaseModel):
    id: Optional[str] = "pdmShortNameID-SystemType"
    name: Optional[str] = "System type"
    inputType: Optional[str] = "Options"
    values: Optional[List[Value]] = [
        {
            "key": "false",
            "value": "3PH3W"
        },
        {
            "key": "true",
            "value": "3PH4W"
        }
    ]
    defaultValue: Optional[str] = "3PH3W"
    helpText: Optional[str] = ""
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class DEVICELABEL(BaseModel):
    id: Optional[str] = "LPHD1_UserAppliName"
    name: Optional[str] = "Device label"
    inputType: Optional[str] = "Text"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = "Alphanumerical value assigned to the device on the single line diagram."
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = {
        "minLength": 0,
        "maxLength": 5,
        "regularExpression": ""
    }
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None
    shortname: Optional[str] = ""
    parametername: Optional[str] = ""
    addreport: Optional[bool] = True
    edit: Optional[bool] = True
    helpTextSelect: Optional[bool] = False


class ASSETNAME(BaseModel):
    id: Optional[str] = "pdmShortNameID-AssetName"
    name: Optional[str] = "Asset name"
    inputType: Optional[str] = "Text"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = ""
    range: Optional[Range] = None
    fieldValidation: Optional[FieldValidation] = {
        "minLength": 1,
        "maxLength": 32,
        "regularExpression": ""
    }
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None
    shortname: Optional[str] = ""
    parametername: Optional[str] = ""
    addreport: Optional[bool] = True
    edit: Optional[bool] = True
    helpTextSelect: Optional[bool] = False


class MODBUSADDRESS(BaseModel):
    id: Optional[str] = "MBSL_LCCH1_Address"
    name: Optional[str] = "Modbus address"
    inputType: Optional[str] = "Scale"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = ""
    range: Optional[Range] = {
        "min": 1,
        "max": 247,
        "stepValue": 1,
        "isNoneApplicable": False
    }
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = ""
    scaleFactor: Optional[int] = None
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None


class ALARMOVERLOADTHRESHOLD(BaseModel):
    id: Optional[str] = "CALH1_IOverloadAlm"
    name: Optional[str] = "Overload threshold"
    inputType: Optional[str] = "Scale"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = "Overload threshold indicates the current value above which a notification is sent, in % of the nominal value."
    range: Optional[Range] = {
        "min": 0,
        "max": 100,
        "stepValue": 5,
        "isNoneApplicable": False
    }
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = "%"
    scaleFactor: Optional[int] = 100
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None
    logicalMapping: Optional[List[str]] = None


class ALARMOVERVOLTAGE(BaseModel):
    id: Optional[str] = "CALH1_OverVAlm"
    name: Optional[str] = "Over voltage"
    inputType: Optional[str] = "Scale"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = "Over voltage indicates the voltage value above which a notification is sent, in % of the nominal value."
    range: Optional[Range] = {
        "min": 100,
        "max": 120,
        "stepValue": 1,
        "isNoneApplicable": False
    }
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = "%"
    scaleFactor: Optional[None] = 100
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None
    logicalMapping: Optional[List[str]] = None


class ALARMEARTHLEAKAGE(BaseModel):
    id: Optional[str] = "CALH1_AEFAlm"
    name: Optional[str] = "Earth leakage tripping threshold"
    inputType: Optional[str] = "Scale"
    values: Optional[List[Value]] = None
    defaultValue: Optional[str] = ""
    helpText: Optional[str] = "E.L. tripping threshold indicates the E.L. current value above which a notification is sent, in % of the nominal value."
    range: Optional[Range] = {
        "min": 30,
        "max": 100,
        "stepValue": 5,
        "isNoneApplicable": False
    }
    fieldValidation: Optional[FieldValidation] = None
    unitSymbol: Optional[str] = "%"
    scaleFactor: Optional[None] = 100
    isMandatory: Optional[bool] = False
    isReadOnly: Optional[bool] = False
    dependencyConfig: Optional[None] = None
    logicalMapping: Optional[List[str]] = None
