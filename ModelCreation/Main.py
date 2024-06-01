from Utility import ExcelManipulation
from MetadataClass import MetadataModel
from ConfiguratorClass import ConfiguratorModel
from requiredJson import get_devicefamily_with_value

metadata = MetadataModel()
configurator = ConfiguratorModel()
input_data = ExcelManipulation().read_input_file()
for inp in input_data:
    commercialReference = inp["Commercial Reference"]
    range = inp["Commercial Reference"] + "_" + inp["Family"].replace(" ", "_")
    family = get_devicefamily_with_value(inp["Family"])
    brand = "Schneider Electric"
    print(range.replace("/", "_"))
    print("Metadata and Configurator created for " + commercialReference)
    print("----------------------------------------------------")
print("All Metadata and Configurator created successfully")