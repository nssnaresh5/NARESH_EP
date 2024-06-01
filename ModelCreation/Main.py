from Utility import ExcelManipulation
from MetadataClass import MetadataModel
from ConfiguratorClass import ConfiguratorModel
from requiredJson import get_devicefamily_with_value

metadata = MetadataModel()
configurator = ConfiguratorModel()
input_data = ExcelManipulation().read_excel()
for k1, v1 in input_data.items():
    commercialReference = input_data["Commercial Reference"]
    range = input_data["Commercial Reference"] + "_" + input_data["Family"].replace(" ", "_")
    family = get_devicefamily_with_value(input_data["Family"])
    brand = "Schneider Electric"
    print(range)
    # if v1.lower() == "yes":
    #     for k2, v2 in categoryName.items():
    #         if k1 in v2:
    #             pass
pass
