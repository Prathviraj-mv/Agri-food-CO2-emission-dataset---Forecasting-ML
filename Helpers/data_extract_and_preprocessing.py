import pandas as pd
from Definitions.constants import DATASET_PATH
path_ = DATASET_PATH

class DATA:
    def __init__(self):
        self.path = path_
        self.columns = [
            "label",
            "lepton_pt", "lepton_eta", "lepton_phi",
            "missing_energy_magnitude", "missing_energy_phi",
            "jet1_pt", "jet1_eta", "jet1_phi", "jet1_btag",
            "jet2_pt", "jet2_eta", "jet2_phi", "jet2_btag",
            "jet3_pt", "jet3_eta", "jet3_phi", "jet3_btag",
            "jet4_pt", "jet4_eta", "jet4_phi", "jet4_btag",
            "m_jj", "m_jjj", "m_lv", "m_jlv", "m_bb", "m_wbb", "m_wwbb"
        ]

        self.data = pd.read_csv(
            self.path,
            names=self.columns,
            header=None,
            dtype="float32"
        )

    def head(self):
        return print(self.data.head(5))

    def print_data_col(self):
        return print(self.data.columns)

    def null_data(self):
        return print(self.data.isnull().sum())

    def calc_corr(self):
        corr_ = self.data.corr()
        return corr_

    def print_corr(self):
        print(self.calc_corr()["label"].sort_values(ascending=True))

    # Final Data Return

    def return_data(self):
        return self.data

if __name__ == "__main__":
    data =DATA()
    data.null_data()
    data.print_data_col()
    data.head()
    data.print_corr()

