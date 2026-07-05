from Helpers.plotters import PLOT
from Definitions.constants import OUTPUT_DIR_p


class EDA:
    def __init__(self):
        pass
    def run(self):
        plt =PLOT()
        plt.plot_correlation(OUTPUT_DIR_p)
