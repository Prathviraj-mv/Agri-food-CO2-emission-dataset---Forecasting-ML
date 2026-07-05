from Helpers.data_extract_and_preprocessing import DATA
from Model.xgb_boost import XGB_MODEL
from Model.Random_forest import RF_MODEL


class APP_:
    def __init__(self):
        DATA().return_data()
        XGB_MODEL().xgb_model()
        RF_MODEL().rf_model()




if __name__ == "__main__":
    a = APP_()



