import typing
import pandas as pd
import datetime as dt


class Exporter:
    """
    A class to represent a data exporter.

    ...

    Attributes
    ----------
    dataframe : DataFrame()
        Class to store tabular data.


    Methods
    -------
    export(file_type, filename):
        Exports products data to desired format and filename.
    """
    def __init__(self, data: typing.Union[list, tuple], columns_names: list[str]):
        """
        Constructs all the necessary atributes for the Exporter object.

        Parrameters
        ----------
            data : list
                data from which the dataframe will be created
            columns_names: list
                list of columns names for the tabular
        """
        self.dataframe = pd.DataFrame(data, columns=columns_names)

    def export(self, file_type: str, filename: str):
        """
        Exports products data to desired format and filename.

        Parrameters
        ----------
            file_type: str
                file type to export
            filename: str
                filename to export
        """
        date = dt.datetime.now()
        if file_type == "excel":
            self.dataframe.to_excel(
                f"./exports/{filename}-{date.strftime('%d-%m-%Y %H:%M:%S')}.xlsx",
                index=False,
            )
