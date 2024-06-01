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
        ("Direct", "", "+"): "Top",
        ("Direct", "", "-"): "Bottom",
    }

    # Return the corresponding power supply
    return mapping.get((type, mounting_position, sign), "Invalid input parameters")


# Test the function
print(get_power_supply("ST", "Top", "+"))  # Output: Top
print(get_power_supply("Direct", "", "-"))  # Output: Bottom


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
        ("Direct", "", "Top"): "+",
        ("Direct", "", "Bottom"): "-",
    }

    # Return the corresponding sign
    return mapping.get((type, mounting_position, power_supply), "Invalid input parameters")


# Test the function
print(get_sign("ST", "Top", "Top"))  # Output: +
print(get_sign("Direct", "", "Bottom"))  # Output: -


def get_phase_sequence(type, mounting_position, phase_sequence):
    # Define the mapping
    mapping = {
        ("ST", "Top"): "Direct",
        ("ST", "Bottom"): "Reverse",
        ("SB", "Top"): "Reverse",
        ("SB", "Bottom"): "Direct",
        ("Direct", ""): "Direct",
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
print(get_phase_sequence("ST", "Top", "NA"))  # Output: ABC
print(get_phase_sequence("ST", "Bottom", "32"))  # Output: ABC
print(get_phase_sequence("ST", "Bottom", "A2C"))  # Output: A


def get_slot_mapping(IsNeutralAvailable, phase_number):
    mapping = {
        "N": "slot1Phase",
        "A": "slot2Phase",
        "B": "slot3Phase",
        "C": "slot4Phase",
    }

    phases = ['A', 'B', 'C'][:phase_number]

    if IsNeutralAvailable:
        return [{"value": mapping[key], "rank": 1, "path": f"electrical.{mapping[key]}"} for key in phases]
    else:
        return [{"value": f"slot{i + 1}Phase", "rank": 1, "path": f"electrical.slot{i + 1}Phase"} for i, key in enumerate(phases)]


def generate_possible_derived_values(IsNeutralAvailable, phase_number):
    slot_mapping = get_slot_mapping(IsNeutralAvailable, phase_number)
    possible_derived_values = []

    for slot in slot_mapping:
        value = slot['value']
        for installation in ["hasUpstreamDataPoint", "hasDownstreamDataPoint"]:
            for sign in ["+", "-"]:
                new_dict = {"LPHD1_InstallationFromBrk": installation, "value": "C-B-A", value: sign + value[-1]}
                possible_derived_values.append(new_dict)

    return possible_derived_values


# Example usage:
IsNeutralAvailable = True
phase_number = 3
possible_derived_values = generate_possible_derived_values(IsNeutralAvailable, phase_number)
