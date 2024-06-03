from rest_library import RestClient
import pandas as pd
import json, requests
from Models.MetadataModel import *


class SelfPortal:
    def __init__(self):
        self.rest_client = RestClient()
        df = pd.read_excel("input_data.xlsx", sheet_name='Sheet1', header=[0, 1])
        data_dict = df.to_dict(orient='list')
        self.input_data = []
        num_rows = len(next(iter(data_dict.values())))
        for i in range(num_rows):
            new_dict = {}
            for (key1, key2), values in data_dict.items():
                if key1 not in new_dict:
                    new_dict[key1] = {}
                new_dict[key1][key2] = values[i]
            self.input_data.append(new_dict)
        self.input_data = self.input_data[0]  # remove this line if you are working for multiple rows
        self.qa_url = "https://wap-etpx-commission-diservice-qa-v1.azurewebsites.net"
        self.driverId = ""

    @staticmethod
    def get_row_by_string_in_devicelist(search_string):
        df = pd.read_excel("Device List ESXP-2.36.xlsx", sheet_name="DEVICE LIST")
        row_as_list = df[df.iloc[:, 9] == search_string].values.tolist()
        return row_as_list[0]

    @staticmethod
    def replace_phase_sequence(phase_sequence):
        letter_to_number = {'A': '1', 'B': '2', 'C': '3'}
        phase_sequence_list = phase_sequence.split('-')
        phase_sequence_list = [letter_to_number.get(item, item) for item in phase_sequence_list]
        phase_sequence = '-'.join(phase_sequence_list)
        return phase_sequence

    def create_identification_data(self):
        driver = Driver()
        driver.driverType = self.input_data['Identification']['driverType']
        driver.commercialRange = self.input_data['Identification']['commercialRange']
        driver.deviceFamily = self.input_data['Identification']['deviceFamily']
        if ',' in self.input_data['Identification']['commercialModels']:
            commercial_models = self.input_data['Identification']['commercialModels'].split(',')
            driver.noOfModels = len(commercial_models)
            driver.commercialModels = []
            for commercial_model in commercial_models:
                commercial_model_obj = CommercialModel()
                commercial_model_obj.commercialReference = commercial_model
                driver.commercialModels.append(commercial_model_obj)
        else:
            driver.noOfModels = 1
            commercial_model_obj = CommercialModel()
            commercial_model_obj.commercialReference = self.input_data['Identification']['commercialModels']
            driver.commercialModels = [commercial_model_obj]
        return driver.dict()

    def create_new_driver(self):
        new_driver_data = self.create_identification_data()
        response = self.rest_client.post(url=self.qa_url + "/driver/identification", json=new_driver_data)
        self.driverId = response['driverId']
        new_param = {"driverId": self.driverId}
        check_res = self.rest_client.get(url=self.qa_url + "/driver/categories", params=new_param)
        print(self.driverId)
        return check_res

    def create_category_data(self):
        CR = self.input_data['Identification']['commercialModels'].split(',')[0] if "," in self.input_data['Identification']['commercialModels'] else \
            self.input_data['Identification']['commercialModels']
        get_ref_data = self.get_row_by_string_in_devicelist(CR)
        categories_data = []
        for category_name, value in self.input_data.items():
            category_data = Category()
            if category_name == "Associated breaker settings" and "y" in value.values():
                category_data.name = category_name
                for settingName, v in value.items():
                    settingobj = eval(settingName)().dict()
                    if v.lower() == 'y':
                        if settingName == "ReferenceOfBreaker":
                            if get_ref_data[12] != 'NA' and type(get_ref_data[12]).__name__ != 'float':
                                get_ref_data_new = get_ref_data[12].split('\n')
                                for ref in get_ref_data_new:
                                    val_ref = Value(key=ref, value=ref)
                                    settingobj['values'].append(val_ref.dict())
                                settingobj['defaultValue'] = get_ref_data_new[0]
                            else:
                                continue
                        if settingName == "RatedCurrent":
                            if get_ref_data[16] != 'NA' and type(get_ref_data[16]).__name__ != 'float':
                                get_ref_data_new = get_ref_data[16].split('\n')
                                get_ref_data_new_amp = [item.replace('A', '').replace(',', '.') if 'A' in item else item.replace(',', '.') for item in get_ref_data_new]
                                for ref in get_ref_data_new_amp:
                                    val_rc = Value(key=ref, value=ref)
                                    settingobj['values'].append(val_rc.dict())
                                settingobj['defaultValue'] = get_ref_data_new_amp[0]
                            else:
                                continue
                        if settingName == "MountingPosition":
                            val_mp = Value()
                            if get_ref_data[36] != 'NA' and type(get_ref_data[36]).__name__ != 'float':
                                data = get_ref_data[36].lower()
                                result = []
                                if '\n' in data:
                                    result = data.split('\n')
                                else:
                                    result.append(data)
                                for i in range(len(result)):

                                    if result[i] in ['line', 'top']:
                                        val_mp = Value(key='hasUpstreamDataPoint', value=result[i].upper())
                                    elif result[i] in ['load', 'bottom']:
                                        val_mp = Value(key='hasDownstreamDataPoint', value=result[i].upper())
                                    settingobj['values'].append(val_mp.dict())
                                settingobj['defaultValue'] = result[0].upper()
                            else:
                                continue
                        category_data.settings.append(settingobj)
                categories_data.append(category_data.dict())
            elif category_name == "Usage" and "n" not in value.values():
                category_data.name = category_name
                for settingName, v in value.items():
                    settingobj = eval(settingName)().dict()
                    if v.lower() == 'y':
                        category_data.settings.append(settingobj)
                categories_data.append(category_data.dict())
                continue
            elif category_name == "Power Settings" and "y" in value.values():
                category_data.name = category_name
                for settingName, v in value.items():
                    settingobj = eval(settingName)().dict()
                    if v.lower() == 'y':
                        if settingName == "PowerSupply":
                            val1 = Value()
                            if get_ref_data[37] != 'NA' and type(get_ref_data[37]).__name__ != 'float':
                                data = get_ref_data[37].lower()
                                result = []
                                if '\n' in data:
                                    result = data.split('\n')
                                else:
                                    result.append(data)
                                for ref in result:
                                    val1.key = ref.upper()
                                    val1.value = ref.upper()
                                    settingobj['values'].append(val1.dict())
                                settingobj['defaultValue'] = result[0].upper()
                            else:
                                continue
                        if settingName == "PhaseSequence":
                            val2 = Value()
                            if get_ref_data[35] != 'NA' and type(get_ref_data[35]).__name__ != 'float':
                                data = get_ref_data[35]
                                result = []
                                if '\n' in data:
                                    result = data.split('\n')
                                else:
                                    result.append(data)
                                phase_sequences = [self.replace_phase_sequence(phase_sequence) for phase_sequence in result]
                                for ref in phase_sequences:
                                    val2.key = ref
                                    val2.value = ref
                                    settingobj['values'].append(val2.dict())
                                settingobj['defaultValue'] = result[0]
                            else:
                                continue
                        category_data.settings.append(settingobj)
                categories_data.append(category_data.dict())
                continue
            elif category_name in "Device Settings" and "y" in value.values():
                category_data.name = category_name
                for settingName, v in value.items():
                    settingobj = eval(settingName)().dict()
                    if v.lower() == 'y':
                        category_data.settings.append(settingobj)
                categories_data.append(category_data.dict())
                continue
            elif category_name == "Communication" and "y" in value.values():
                category_data.name = category_name
                for settingName, v in value.items():
                    settingobj = eval(settingName)().dict()
                    if v.lower() == 'y':
                        category_data.settings.append(settingobj)
                categories_data.append(category_data.dict())
                continue
        return categories_data

    def create_alarm_data(self):
        alarms_data = []
        for alarm_name, value in self.input_data.items():
            if alarm_name == "Alarm" and "y" in value.values():
                alarm_data = Alarm()
                alarm_data.name = alarm_name
                for settingName, v in value.items():
                    settingobj = eval(settingName)().dict()
                    if v.lower() == 'y':
                        alarm_data.settings.append(settingobj)
                alarms_data.append(alarm_data.dict())
        return alarms_data

    def update_driver_category(self, inputdata1, inputdata2):
        inputdata1["categories"] = inputdata2
        r2 = self_portal.rest_client.put(url=self.qa_url + "/driver/categories", json=inputdata1)
        return r2

    def update_driver_alarm(self, inputdata1):
        inputdata2 = {'driverId': self.driverId, 'settings': inputdata1[0]['settings']}
        r2 = self_portal.rest_client.put(url=self.qa_url + "/driver/alarms", json=inputdata2)
        return r2

    def create_parameters_data(self):
        with open('ParamInput.json', 'r') as f:
            param_data = json.load(f)
        new_param = {"driverId": self.driverId}
        get_categories = self.rest_client.get(url=self.qa_url + "/driver/categories", params=new_param)
        new_param["parameterConfigurations"] = []
        for category in get_categories["categories"]:
            for paramConfig in param_data["parameterConfigurations"]:
                if category["name"] == paramConfig["name"]:
                    new_param["parameterConfigurations"].append(
                        {
                            "id": category["id"],
                            "name": category["name"],
                            "read": paramConfig["read"],
                            "write": paramConfig["write"]
                        }
                    )
        return new_param

    def update_driver_parameters(self, inputdata):
        r2 = self_portal.rest_client.post(url=self.qa_url + "/driver/parameters", json=inputdata)
        return r2

    def create_adv_setting_data(self, categorydata):
        global conversionType
        CR = self.input_data['Identification']['commercialModels'].split(',')[0] if "," in self.input_data['Identification']['commercialModels'] else \
            self.input_data['Identification']['commercialModels']
        get_ref_data = self.get_row_by_string_in_devicelist(CR)
        if get_ref_data[12] != 'NA' and type(get_ref_data[12]).__name__ != 'float':
            conversionType = get_ref_data[63]

        def find_power_supply(type, mounting_position, sign):
            data = [
                {"Type": "SWAPT", "Mounting Position": "hasUpstreamDataPoint", "Sign": "+", "PowerSupply": "TOP"},
                {"Type": "SWAPT", "Mounting Position": "hasUpstreamDataPoint", "Sign": "-", "PowerSupply": "BOTTOM"},
                {"Type": "SWAPT", "Mounting Position": "hasDownstreamDataPoint", "Sign": "+", "PowerSupply": "BOTTOM"},
                {"Type": "SWAPT", "Mounting Position": "hasDownstreamDataPoint", "Sign": "-", "PowerSupply": "TOP"},
                {"Type": "SWAPB", "Mounting Position": "hasUpstreamDataPoint", "Sign": "+", "PowerSupply": "BOTTOM"},
                {"Type": "SWAPB", "Mounting Position": "hasUpstreamDataPoint", "Sign": "-", "PowerSupply": "TOP"},
                {"Type": "SWAPB", "Mounting Position": "hasDownstreamDataPoint", "Sign": "+", "PowerSupply": "TOP"},
                {"Type": "SWAPB", "Mounting Position": "hasDownstreamDataPoint", "Sign": "-", "PowerSupply": "BOTTOM"},
                {"Type": "Direct", "Mounting Position": "hasUpstreamDataPoint", "Sign": "+", "PowerSupply": "TOP"},
                {"Type": "Direct", "Mounting Position": "hasDownstreamDataPoint", "Sign": "-", "PowerSupply": "BOTTOM"},
            ]

            for item in data:
                if item["Type"] == type and item["Mounting Position"] == mounting_position and item["Sign"] == sign:
                    return item["PowerSupply"]

            return "No match found"

        slot2phase = ["+A", "-A", "+B", "-B", "+C", "-C"]
        mp_list = []
        ps_list = []
        for cat in categorydata['categories']:
            for setting in cat['settings']:
                if setting['id'] == 'LPHD1_InstallationFromBrk':
                    for v in setting['values']:
                        mp_list.append(v['key'])
            for setting1 in cat['settings']:
                if setting1['id'] == 'LPHD1_PowSupCfg':
                    for v in setting1['values']:
                        ps_list.append(v['key'])
        powerSupply_possible_vals = []

        def get_ps_values(input_value):
            mapping = {
                "TOP": ps_list[0],
                "BOTTOM": ps_list[1],
            }

            return mapping.get(input_value, [])

        for i in slot2phase:
            for j in mp_list:
                ps = find_power_supply(conversionType, j, i[0])
                powerSupply_possible_vals.append({
                    "LPHD1_InstallationFromBrk": j,
                    "slot2Phase": i,
                    "value": get_ps_values(ps)
                })

        def rotate_type_based_on_sequence(type, mounting_position, text):
            def find_phase_sequence(type, mounting_position):
                data = [
                    {"Type": "SWAPT", "Mounting Position": "hasUpstreamDataPoint", "Phase Sequence": "NOROTATE"},
                    {"Type": "SWAPT", "Mounting Position": "hasDownstreamDataPoint", "Phase Sequence": "ROTATE"},
                    {"Type": "SWAPB", "Mounting Position": "hasUpstreamDataPoint", "Phase Sequence": "ROTATE"},
                    {"Type": "SWAPB", "Mounting Position": "hasDownstreamDataPoint", "Phase Sequence": "NOROTATE"},
                    {"Type": "Direct", "Mounting Position": "", "Phase Sequence": "NOROTATE"},
                ]

                for item in data:
                    if item["Type"] == type and item["Mounting Position"] == mounting_position:
                        return item["Phase Sequence"]

                return "No match found"

            phase_sequence = find_phase_sequence(type, mounting_position)

            if phase_sequence == "ROTATE":
                if len(text) > 1:
                    return text[-1] + text[1:-1] + text[0]
                else:
                    return text
            else:
                return text

        def get_dependentResponseValues(IsNeutralAvailable, phase_number):
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


self_portal = SelfPortal()
new_identification = self_portal.create_new_driver()
new_category_data = self_portal.create_category_data()
new_category = self_portal.update_driver_category(new_identification, new_category_data)
new_alarm_data = self_portal.create_alarm_data()
new_data = self_portal.update_driver_alarm(new_alarm_data)
new_param = self_portal.create_parameters_data()
new_param_data = self_portal.update_driver_parameters(new_param)
self_portal.create_adv_setting_data(new_category)
pass
