import typing
import pandas as pd
import datetime as dt

class Exporter:
    def __init__(self, data: typing.Union[list, tuple], columns_names: list[int]):
        self.dataframe = pd.DataFrame(data, columns=columns_names)

    def export(self, file_type: str, filename: str):
        date = dt.datetime.now()
        if file_type == "excel":
            self.dataframe.to_excel(f"./exports/{filename}-{date.strftime('%d-%m-%Y %H:%M:%S')}.xlsx", index=False)