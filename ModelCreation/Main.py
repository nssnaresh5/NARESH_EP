from Utility import ExcelManipulation
from MetadataClass import MetadataModel
from ConfiguratorClass import ConfiguratorModel
from requiredJson import get_devicefamily_with_value

metadata = MetadataModel()
configurator = ConfiguratorModel()
inputdata = ExcelManipulation().read_excel()
for k1, v1 in inputdata.items():
    commercialReference = inputdata["Commercial Reference"]
    range = inputdata["Commercial Reference"] + "_" + inputdata["Family"].replace(" ", "_")
    family = get_devicefamily_with_value(inputdata["Family"])
    brand = "Schneider Electric"
    if v1.lower() == "yes":
        for k2, v2 in categoryName.items():
            if k1 in v2:
                pass
pass
