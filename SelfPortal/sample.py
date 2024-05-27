import pprint


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


# pprint.pprint(get_slot_mapping(False, 1))
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
