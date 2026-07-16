from Definitions.constants import OUTPUT_DIR_p
from Helpers.data_extract_and_preprocessing import DATA
from Helpers.plotters import PLOT


class EDA:
    def __init__(self):
        self.data = DATA().return_data()

    def run(self):
        plt = PLOT()
        plt.plot_correlation(OUTPUT_DIR_p)
        plt.plot_joint_plot(path=OUTPUT_DIR_p, data=self.data, x="jet1_pt", y="label")
        plt.plot_scatter_plot(path=OUTPUT_DIR_p, data=self.data, x="jet1_pt", y="label")
        plt.plot_count_plot(path=OUTPUT_DIR_p, data=self.data)
        plt.histplot(path=OUTPUT_DIR_p, data=self.data, x="jet1_pt")
        plt.kdeplot(path=OUTPUT_DIR_p, data=self.data, x="jet1_pt")
        plt.pairplot(path=OUTPUT_DIR_p, data=self.data, list_=["jet1_pt", "jet2_pt", "jet3_pt", "jet4_pt", "label"])


if __name__ == "__main__":
    plot = EDA()
    plot.run()
