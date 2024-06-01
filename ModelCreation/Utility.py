import pandas as pd


class ExcelManipulation:
    def __init__(self):
        self.input_excel_path = (r"C:\Users\SESA503669\OneDrive - Schneider Electric\D\D\ETPX\wirelessModels\ESXP_Param_v1.xlsx")

    def read_excel(self):
        df = pd.read_excel(self.input_excel_path, sheet_name='Param', header=[0])
        data_dict = df.to_dict(orient='list')
        self.input_data = []
        num_rows = len(next(iter(data_dict.values())))
        for i in range(num_rows):
            new_dict = {}
            for key, values in data_dict.items():
                if key not in new_dict:
                    new_dict[key] = values[i]
            self.input_data.append(new_dict)
        return self.input_data[0]

# print(ExcelManipulation().input_data[0])
