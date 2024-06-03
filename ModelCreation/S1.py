from itertools import zip_longest

global_mounting_position = {
    "Line": "Top",
    "Load": "Bottom",
    "Top": "Top",
    "Bottom": "Bottom"
}
mp_mapping = {
    "Top": "hasUpstreamDataPoint",
    "Bottom": "hasDownstreamDataPoint",
    "Line": "hasUpstreamDataPoint",
    "Load": "hasDownstreamDataPoint"
}
global_power_supply = {
    "Direct": "Top",
    "Reverse": "Bottom",
    "Line": "Top",
    "Load": "Bottom"
}


def get_power_supply(type: str = "", mounting_position: str = "", sign: str = ""):
    # Define the mapping
    mapping = {
        ("ST", "Top", "+"): "Top",
        ("ST", "Top", "-"): "Bottom",
        ("ST", "Bottom", "+"): "Bottom",
        ("ST", "Bottom", "-"): "Top",
        ("SB", "Top", "+"): "Bottom",
        ("SB", "Top", "-"): "Top",
        ("SB", "Bottom", "+"): "Top",
        ("SB", "Bottom", "-"): "Bottom",
        ("SD", "Top", "+"): "Top",
        ("SD", "Top", "-"): "Bottom",
        ("SD", "Bottom", "+"): "Top",
        ("SD", "Bottom", "-"): "Bottom",
    }

    # Return the corresponding power supply
    return mapping.get((type, mounting_position, sign), "Invalid input parameters")


# Test the function
# print(get_power_supply("ST", "Top", "+"))  # Output: Top
# print(get_power_supply("Direct", "", "-"))  # Output: Bottom


def get_sign(type, mounting_position, power_supply):
    # Define the mapping
    mapping = {
        ("ST", "Top", "Top"): "+",
        ("ST", "Top", "Bottom"): "-",
        ("ST", "Bottom", "Top"): "-",
        ("ST", "Bottom", "Bottom"): "+",
        ("SB", "Top", "Top"): "-",
        ("SB", "Top", "Bottom"): "+",
        ("SB", "Bottom", "Top"): "+",
        ("SB", "Bottom", "Bottom"): "-",
        ("SD", "Top", "Top"): "+",
        ("SD", "Top", "Bottom"): "-",
        ("SD", "Bottom", "Top"): "+",
        ("SD", "Bottom", "Bottom"): "-",
    }

    # Return the corresponding sign
    return mapping.get((type, mounting_position, power_supply), "Invalid input parameters")


# # Test the function
# print(get_sign("ST", "Top", "Top"))  # Output: +
# print(get_sign("Direct", "", "Bottom"))  # Output: -


def get_phase_sequence(type, mounting_position, phase_sequence):
    # Define the mapping
    mapping = {
        ("ST", "Top"): "Direct",
        ("ST", "Bottom"): "Reverse",
        ("SB", "Top"): "Reverse",
        ("SB", "Bottom"): "Direct",
        ("SD", "Top"): "Direct",
        ("SD", "Bottom"): "Direct",
    }

    # Get the corresponding phase sequence type
    phase_sequence_type = mapping.get((type, mounting_position), "Invalid input parameters")

    # Modify the phase sequence based on the rules
    if phase_sequence_type == "Direct":  # Direct, no change
        return phase_sequence
    elif phase_sequence_type == "Reverse":  # Reverse
        if len(phase_sequence) == 3:
            return phase_sequence[2] + phase_sequence[1] + phase_sequence[0]
        elif len(phase_sequence) == 2:
            return phase_sequence[1] + phase_sequence[0]
        elif len(phase_sequence) == 1:  # If phase sequence is a single character, return as is
            return phase_sequence

    return "Invalid phase sequence"


# Test the function
# print(get_phase_sequence("ST", "Top", "NA"))  # Output: NA
# print(get_phase_sequence("ST", "Bottom", "32"))  # Output: 23
# print(get_phase_sequence("ST", "Bottom", "A2C"))  # Output: C2A


def get_dependent_response_values(isneutralavailable, phase_number):
    mapping = {
        "N": "slot1Phase",
        "A": "slot2Phase",
        "B": "slot3Phase",
        "C": "slot4Phase",
    }

    phases = ['A', 'B', 'C'][:phase_number]

    if isneutralavailable.lower() == "yes":
        return [{"value": mapping[key], "rank": 1, "path": f"electrical.{mapping[key]}"} for key in phases]
    else:
        return [{"value": f"slot{i + 1}Phase", "rank": 1, "path": f"electrical.slot{i + 1}Phase"} for i, key in enumerate(phases)]


def get_possible_derived_values_powersupply(isneutralavailable, phase_number, type, actualmountingposition, actualpowersupply):
    if actualmountingposition != 'NA':
        data = actualmountingposition
        mpresult = []
        if '\n' in data:
            mpresult = data.split('\n')
        else:
            mpresult.append(data)
    if actualpowersupply != 'NA':
        data1 = actualpowersupply
        psresult = []
        if '\n' in data1:
            psresult = data1.split('\n')
        else:
            psresult.append(data1)
    mapping_ps_to_custom = dict(zip_longest(["Top", "Bottom"], psresult))
    slot_mapping = [get_dependent_response_values(isneutralavailable, phase_number)[0]]
    possible_derived_values = []
    for slot in slot_mapping:
        slptphase = slot['value']

        for installation in mpresult:
            for sign in ["+", "-"]:
                for p in ["A", "B", "C"]:
                    power_supply = get_power_supply(type, global_mounting_position.get(installation), sign)
                    new_dict = {"LPHD1_InstallationFromBrk": mp_mapping.get(installation), "value": mapping_ps_to_custom.get(power_supply), slptphase: sign + p}
                    possible_derived_values.append(new_dict)

    return possible_derived_values


def get_possible_derived_values_phasesequence(isneutralavailable, phase_number, type, actualmountingposition, actualpowersupply):
    if actualmountingposition != 'NA':
        data = actualmountingposition
        mpresult = []
        if '\n' in data:
            mpresult = data.split('\n')
        else:
            mpresult.append(data)
    if actualpowersupply != 'NA':
        data1 = actualpowersupply
        psresult = []
        if '\n' in data1:
            psresult = data1.split('\n')
        else:
            psresult.append(data1)

    slot_mapping = get_dependent_response_values(isneutralavailable, phase_number)
    # mapping_mp_to_custom = dict(zip_longest(["Top", "Bottom"], psresult))
    mapping_ps = {
        "1": ["A", "B", "C"],
        "2": ["AB", "AC", "BA", "BC", "CA", "CB"],
        "3": ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
    }
    possible_derived_values = []
    for i1 in mpresult:
        for i2 in mapping_ps.get(str(phase_number), []):
            for i3 in ["+", "-"]:
                ps = "-".join(get_phase_sequence(type, global_mounting_position.get(i1), i2))
                new_dict = {"LPHD1_InstallationFromBrk": mp_mapping.get(i1), "value": ps}
                for n, slot in enumerate(slot_mapping):
                    new_dict[slot['value']] = i3 + i2[n]
                possible_derived_values.append(new_dict)
    return possible_derived_values


def get_possible_derived_values_write_phase_sequence(isneutralavailable, phase_number, type, actualmountingposition, actualpowersupply, slotvalue):
    if actualmountingposition != 'NA':
        data = actualmountingposition
        mpresult = []
        if '\n' in data:
            mpresult = data.split('\n')
        else:
            mpresult.append(data)
    if actualpowersupply != 'NA':
        data1 = actualpowersupply
        psresult = []
        if '\n' in data1:
            psresult = data1.split('\n')
        else:
            psresult.append(data1)
    mapping_ps_to_custom = dict(zip_longest(["Top", "Bottom"], psresult))
    slot_mapping = get_dependent_response_values(isneutralavailable, phase_number)
    mapping_ps = {
        "1": ["A", "B", "C"],
        "2": ["AB", "AC", "BA", "BC", "CA", "CB"],
        "3": ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
    }
    possible_derived_values = []
    for i1 in mpresult:
        for i2 in psresult:
            for i3 in mapping_ps.get(str(phase_number), []):
                ps = get_phase_sequence(type, global_mounting_position.get(i1), i3)
                sign = get_sign(type, global_mounting_position.get(i1), i2)
                new_dict = {
                    "LPHD1_InstallationFromBrk": mp_mapping.get(i1),
                    "LPHD1_PowSupCfg": i2,
                    "LPHD1_PhsRot": "-".join(i3),
                    "value": sign + ps[slotvalue]
                }
                possible_derived_values.append(new_dict)
    return possible_derived_values


from ConfiguratorClass import *
from Utility import ExcelManipulation


def create_advanced_settings_read():
    configurator = ConfiguratorModel()
    Excel = ExcelManipulation()
    input_data = Excel.read_input_file()[3]
    device_list = Excel.read_device_list(input_data['Commercial Reference'])
    """
    The list item number for the main objects
    Commercial reference = 9
    referenceOfTheBreaker = 12
    ratedCurrent = 16
    phaseSequence = 35
    mountingPosition = 36
    powerSupply = 37
    """

    isneutralavailable = input_data["IsNeutral"]
    # Power supply read
    phase_number = int(input_data["Phase"])
    attribute1 = AdvancedSetting()
    attribute1.pdmShortNameId = "LPHD1_PowSupCfg"
    attribute1.dependentSettings = ["LPHD1_InstallationFromBrk"]
    dependent_response_values = get_dependent_response_values(isneutralavailable, phase_number)
    attribute1.dependentResponseValues = [dependent_response_values[0]]
    possible_derived_values_powersupply = get_possible_derived_values_powersupply(isneutralavailable, phase_number, input_data['ConversionType'], device_list[36], device_list[37])
    attribute1.possibleDerivedValues = possible_derived_values_powersupply
    # # Phase sequence read
    attribute2 = AdvancedSetting()
    attribute2.pdmShortNameId = "LPHD1_PhsRot"
    attribute2.dependentSettings = ["LPHD1_InstallationFromBrk"]
    attribute2.dependentResponseValues = dependent_response_values
    possible_derived_values_pasesequence = get_possible_derived_values_phasesequence(isneutralavailable, phase_number, input_data['ConversionType'], device_list[36], device_list[37])
    attribute2.possibleDerivedValues = possible_derived_values_pasesequence

    # # Read
    read = Read()
    read.advancedSettings.append(attribute1)
    read.advancedSettings.append(attribute2)

    # Write
    write = Write()
    write.advancedSettings = []
    for n, att in enumerate(dependent_response_values):
        attribute3 = AdvancedSetting()
        attribute3.attribute = att
        attribute3.dependentSettings = [
            "LPHD1_InstallationFromBrk",
            "LPHD1_PowSupCfg",
            "LPHD1_PhsRot"
        ]
        attribute3.possibleDerivedValues = get_possible_derived_values_write_phase_sequence(isneutralavailable, phase_number, input_data['ConversionType'], device_list[36], device_list[37], n)
        write.advancedSettings.append(attribute3)
    pass


# def create_advanced_settings_write():
#     pass


create_advanced_settings_read()
# create_advanced_settings_write()
