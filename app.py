from Helpers.data_extract_and_preprocessing import DATA
from Helpers.plotters import  PLOT
from Helpers.IOdata import  IO
from Model.Random_forest import RF_MODEL


class APP_:
    def __init__(self):
        DATA().return_data()
        PLOT().plot_correlation()
        RF_MODEL().rf_model()







