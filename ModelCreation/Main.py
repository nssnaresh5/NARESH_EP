from Utility import ExcelManipulation
from MetadataClass import *
from ConfiguratorClass import *
from requiredJson import *
from settingclass import *
import uuid, json
from itertools import zip_longest

"""
Commercial reference = 9
referenceOfTheBreaker = 12
ratedCurrent = 16
phaseSequence = 35
mountingPosition = 36
powerSupply = 37
"""


class ModelCreation:
    def __init__(self):
        self.filtered_commercial_reference = None
        self.input_data = ExcelManipulation().read_input_file()
        self.device_list = ExcelManipulation().read_device_list()

        self.metadata = MetadataModel()
        self.configurator = ConfiguratorModel()
        self.global_mounting_position = {
            "Line": "Top",
            "Load": "Bottom",
            "Top": "Top",
            "Bottom": "Bottom"
        }
        self.mp_mapping = {
            "Top": "hasUpstreamDataPoint",
            "Bottom": "hasDownstreamDataPoint",
            "Line": "hasUpstreamDataPoint",
            "Load": "hasDownstreamDataPoint"
        }
        self.global_power_supply = {
            "Direct": "Top",
            "Reverse": "Bottom",
            "Line": "Top",
            "Load": "Bottom"
        }

    def metadata_identification(self, model):
        name_list = ["Brand", "DeviceFamily", "CommercialReference", "CommercialRange"]
        for c in self.device_list:
            if c[9] == model['Commercial Reference']:
                self.filtered_commercial_reference = c
                break
        identification_data = []
        for i in name_list:
            x1 = Identification()
            x1.id = str(uuid.uuid4())
            x1.name = i
            if i == "Brand":
                x1.value = "Schneider Electric"
            elif i == "DeviceFamily":
                x1.value = [device['value'] for device in deviceFamily if device['key'].lower() == model['Family'].lower()][0]
            elif i == "CommercialReference":
                x1.value = model['Commercial Reference']
            elif i == "CommercialRange":
                x1.value = self.filtered_commercial_reference[5]
            identification_data.append(x1)
        x2 = Device()
        x2.identification = identification_data
        self.metadata.device = x2

    @staticmethod
    def filter_yes_settings(model):
        filtered_category = {}
        for category, settings in categoryName.items():
            filtered_settings = [setting for setting in settings if model.get(setting, '').lower() == 'yes']
            if filtered_settings:
                filtered_category[category] = filtered_settings
        return filtered_category

    @staticmethod
    def replace_phase_sequence(phase_sequence):
        letter_to_number = {'A': '1', 'B': '2', 'C': '3'}
        phase_sequence_list = phase_sequence.split('-')
        phase_sequence_list = [letter_to_number.get(item, item) for item in phase_sequence_list]
        phase_sequence = '-'.join(phase_sequence_list)
        return phase_sequence

    def metadata_configuration(self, model):
        category_settings = self.filter_yes_settings(model)
        c1 = Configuration()
        for category, settings in category_settings.items():
            if category != "Alarm settings":
                x1 = Category()
                x1.id = str(uuid.uuid4())
                x1.name = category
                for setting in settings:
                    x2 = eval(setting.replace(" ", "").upper())()
                    x1.settings.append(x2)
                c1.categories.append(x1)
            else:
                x2 = Alarm()
                x2.id = str(uuid.uuid4())
                x2.name = category
                for setting in settings:
                    x3 = eval(setting.replace(" ", "").upper())()
                    x2.settings.append(x3)
                c1.alarms.append(x2)
        self.metadata.device.configuration = c1

    def metadata_update_model(self):
        global devicelist_data
        for c in self.metadata.device.identification:
            if c.name == "CommercialReference":
                CommercialReference = c.value
                for cr_data in self.device_list:
                    if cr_data[9] == CommercialReference:
                        devicelist_data = cr_data
                        break
        for category in self.metadata.device.configuration.categories:
            for setting in category.settings:
                if setting.id == 'LPHD1_ProductCode':
                    if devicelist_data[12] != 'NA' and type(devicelist_data[12]).__name__ != 'float':
                        d1 = devicelist_data[12].split('\n')
                        for ref in d1:
                            val_ref = Value(key=ref, value=ref)
                            setting.values.append(val_ref)
                        setting.defaultValue = d1[0]
                    else:
                        continue
                if setting.id == 'LPHD1_ARtg':
                    if devicelist_data[16] != 'NA' and type(devicelist_data[16]).__name__ != 'float':
                        d2 = devicelist_data[16].split('\n')
                        d2_amp = [item.replace('A', '').replace(',', '.') if 'A' in item else item.replace(',', '.') for item in d2]
                        for ref1 in d2_amp:
                            val_ref1 = Value(key=ref1, value=ref1)
                            setting.values.append(val_ref1)
                        setting.defaultValue = d2_amp[0]
                    else:
                        continue
                if setting.id == 'LPHD1_InstallationFromBrk':
                    if devicelist_data[36] != 'NA' and type(devicelist_data[36]).__name__ != 'float':
                        data = devicelist_data[36].lower()
                        result = []
                        if '\n' in data:
                            result = data.split('\n')
                        else:
                            result.append(data)
                        for i in range(len(result)):
                            val_mp = Value()
                            if result[i] in ['line', 'top']:
                                val_mp = Value(key='hasUpstreamDataPoint', value=result[i].upper())
                            elif result[i] in ['load', 'bottom']:
                                val_mp = Value(key='hasDownstreamDataPoint', value=result[i].upper())
                            setting.values.append(val_mp)
                        setting.defaultValue = result[0].upper()
                    else:
                        continue
                if setting.id == 'LPHD1_PowSupCfg':
                    if devicelist_data[37] != 'NA' and type(devicelist_data[37]).__name__ != 'float':
                        data = devicelist_data[37].lower()
                        result = []
                        if '\n' in data:
                            result = data.split('\n')
                        else:
                            result.append(data)
                        for ref in result:
                            val1 = Value()
                            val1.key = ref.upper()
                            val1.value = ref.upper()
                            setting.values.append(val1)
                        setting.defaultValue = result[0].upper()
                    else:
                        continue
                if setting.id == 'LPHD1_PhsRot':

                    if devicelist_data[35] != 'NA' and type(devicelist_data[35]).__name__ != 'float':
                        data = devicelist_data[35]
                        result = []
                        if '\n' in data:
                            result = data.split('\n')
                        else:
                            result.append(data)
                        phase_sequences = [self.replace_phase_sequence(phase_sequence) for phase_sequence in result]
                        for ref in phase_sequences:
                            val2 = Value()
                            val2.key = ref
                            val2.value = ref
                            setting.values.append(val2)
                        setting.defaultValue = result[0]
                    else:
                        continue

    @staticmethod
    def read_json_file(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    def configurator_common_device_attributes(self):
        static_data = self.read_json_file('staticdata.json')
        global_variables = []
        for category1 in self.metadata.device.configuration.categories:
            for setting in category1.settings:
                for v1 in static_data['configurator']:
                    if setting.id in v1['pdmShortNameIds']:
                        for v2 in v1['globalVariables']:
                            if v2 not in global_variables:
                                global_variables.append(v2)
        c1 = CommonDeviceAttributes()
        c1.id = str(uuid.uuid4())
        c1.globalVariables = global_variables
        for s1 in global_variables:
            for s2 in static_data['globalVariableServices']:
                if s1 == s2['globalVariable']:
                    c1.services.append(Services(**s2))
        c2 = ServiceMapping()
        c2.commonDeviceAttributes = c1
        self.configurator.serviceMapping = c2

    def configurator_categories(self):
        static_data = self.read_json_file('staticdata.json')
        cate = []
        for cat1 in self.metadata.device.configuration.categories:
            c1 = category()
            c1.id = cat1.id
            for s1 in cat1.settings:
                c1.pdmShortNameIds.append(s1.id)
                if c1.read is None or c1.write is None:
                    for c2 in static_data['configurator']:
                        if s1.id in c2['pdmShortNameIds']:
                            c1.read = Read(**c2['read'])
                            c1.write = Write(**c2['write'])
                            break
            cate.append(c1)
        self.configurator.serviceMapping.categories = cate

    @staticmethod
    def dict_to_json_file(dictionary, filename):
        # Create directory if it doesn't exist
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Write dictionary to JSON file
        with open(filename, 'w') as f:
            json.dump(dictionary, f, indent=4)

    def get_dependent_response_values(self, isneutralavailable, phase_number):
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

    def get_power_supply(self, type: str = "", mounting_position: str = "", sign: str = ""):
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

    def get_sign(self, type, mounting_position, power_supply):
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

    def get_phase_sequence(self, type, mounting_position, phase_sequence):
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

    def get_possible_derived_values_powersupply(self, isneutralavailable, phase_number, type, actualmountingposition, actualpowersupply):
        global psresult, mpresult
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
        slot_mapping = [self.get_dependent_response_values(isneutralavailable, phase_number)[0]]
        possible_derived_values = []
        for slot in slot_mapping:
            slptphase = slot['value']

            for installation in mpresult:
                for sign in ["+", "-"]:
                    for p in ["A", "B", "C"]:
                        power_supply = self.get_power_supply(type, self.global_mounting_position.get(installation), sign)
                        new_dict = {"LPHD1_InstallationFromBrk": self.mp_mapping.get(installation), "value": mapping_ps_to_custom.get(power_supply), slptphase: sign + p}
                        possible_derived_values.append(new_dict)

        return possible_derived_values

    def get_possible_derived_values_phasesequence(self, isneutralavailable, phase_number, type, actualmountingposition, actualpowersupply):
        global mpresult
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

        slot_mapping = self.get_dependent_response_values(isneutralavailable, phase_number)
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
                    ps = "-".join(self.get_phase_sequence(type, self.global_mounting_position.get(i1), i2))
                    new_dict = {"LPHD1_InstallationFromBrk": self.mp_mapping.get(i1), "value": ps}
                    for n, slot in enumerate(slot_mapping):
                        new_dict[slot['value']] = i3 + i2[n]
                    possible_derived_values.append(new_dict)
        return possible_derived_values

    def get_possible_derived_values_write_phase_sequence(self, isneutralavailable, phase_number, type, actualmountingposition, actualpowersupply, slotvalue):
        global psresult, mpresult
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
        slot_mapping = self.get_dependent_response_values(isneutralavailable, phase_number)
        mapping_ps = {
            "1": ["A", "B", "C"],
            "2": ["AB", "AC", "BA", "BC", "CA", "CB"],
            "3": ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
        }
        possible_derived_values = []
        for i1 in mpresult:
            for i2 in psresult:
                for i3 in mapping_ps.get(str(phase_number), []):
                    ps = self.get_phase_sequence(type, self.global_mounting_position.get(i1), i3)
                    sign = self.get_sign(type, self.global_mounting_position.get(i1), i2)
                    new_dict = {
                        "LPHD1_InstallationFromBrk": self.mp_mapping.get(i1),
                        "LPHD1_PowSupCfg": i2,
                        "LPHD1_PhsRot": "-".join(i3),
                        "value": sign + ps[slotvalue]
                    }
                    possible_derived_values.append(new_dict)
        return possible_derived_values

    def configurator_advanced_settings(self, device):
        isneutralavailable = device["IsNeutral"]
        phase_number = int(device["Phase"])

        # # Power supply
        attribute1 = AdvancedSetting()
        attribute1.pdmShortNameId = "LPHD1_PowSupCfg"
        attribute1.dependentSettings = ["LPHD1_InstallationFromBrk"]
        dependent_response_values = self.get_dependent_response_values(isneutralavailable, phase_number)
        attribute1.dependentResponseValues = [dependent_response_values[0]]
        possible_derived_values_powersupply = self.get_possible_derived_values_powersupply(isneutralavailable, phase_number, device['ConversionType'], self.filtered_commercial_reference[36], self.filtered_commercial_reference[37])
        attribute1.possibleDerivedValues = possible_derived_values_powersupply

        # # Phase sequence read
        attribute2 = AdvancedSetting()
        attribute2.pdmShortNameId = "LPHD1_PhsRot"
        attribute2.dependentSettings = ["LPHD1_InstallationFromBrk"]
        attribute2.dependentResponseValues = dependent_response_values
        possible_derived_values_pasesequence = self.get_possible_derived_values_phasesequence(isneutralavailable, phase_number, device['ConversionType'], self.filtered_commercial_reference[36], self.filtered_commercial_reference[37])
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
            attribute3.possibleDerivedValues = self.get_possible_derived_values_write_phase_sequence(isneutralavailable, phase_number, device['ConversionType'], self.filtered_commercial_reference[36], self.filtered_commercial_reference[37], n)
            write.advancedSettings.append(attribute3)

        for category in self.configurator.serviceMapping.categories:
            if "LPHD1_PowSupCfg" in category.pdmShortNameIds and "LPHD1_PhsRot" in category.pdmShortNameIds:
                read.id = category.id
                write.id = category.id
                break

        x1 = AdvancedSettingsConfig()
        x1.read = read
        x1.write = write
        self.configurator.advancedSettingsConfig = x1

    def create_metadata_model(self):
        for device in self.input_data:
            self.metadata_identification(device)
            self.metadata_configuration(device)
            self.metadata_update_model()
            self.configurator_common_device_attributes()
            self.configurator_categories()
            self.configurator_advanced_settings(device)

            # Create directory and file names
            directory = f'ModelFiles/{device["Commercial Reference"]}'
            metadata_filename = f'{directory}/{device["Commercial Reference"]}_metadata.json'
            configurator_filename = f'{directory}/{device["Commercial Reference"]}_configurator.json'

            # Write metadata and configurator to JSON files
            self.dict_to_json_file(self.metadata.dict(), metadata_filename)
            self.dict_to_json_file(self.configurator.dict(), configurator_filename)


x = ModelCreation()
x.create_metadata_model()
