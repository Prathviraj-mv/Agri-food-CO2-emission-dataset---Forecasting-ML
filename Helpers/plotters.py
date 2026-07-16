import seaborn as sns
import matplotlib.pyplot as plt

from Helpers.data_extract_and_preprocessing import DATA

class PLOT:
    def __init__(self):
        pass

    def plot_correlation(self,x):
        correlation = DATA().calc_corr()

        plt.figure(figsize=(10,5))
        sns.heatmap(correlation,
            fmt=".1f",
            annot=True,
            vmin=-1,
            vmax=1,
            linewidths=0.5,
            )
        plt.title("Correlation Matrix Heatmap")
        plt.savefig(x /"heatmap.png")
        plt.close()



    def  plot_confusion_matrix(self,value,x):
        plt.figure(figsize=(20,15))
        sns.heatmap(value,
                    fmt=".1f",
                    annot=True,
                    vmin=-1,
                    vmax=1,
                    linewidths=0.5,
                    )
        plt.title("CONFUSION Matrix ")
        plt.savefig(x / "confusion.png")
        plt.close()


    def plot_joint_plot(self,path,data,x,y):
        plt.figure(figsize=(20,15))
        sns.jointplot(data=data,x=x,y=y)
        plt.title("Joint Plot ")
        plt.savefig(path / f"{x}_{y}_joint_plot.png")
        plt.close()



    def plot_scatter_plot(self,path,data,x,y):
        plt.figure(figsize=(20,15))
        sns.scatterplot(data=data,x=x,y=y)
        plt.title("scatterplot")
        plt.savefig(path / f"{x}_{y}scatter_plot.png")
        plt.close()

    def plot_count_plot(self,path,data):
        plt.figure(figsize=(20, 15))
        sns.countplot(data=data, x="label")
        plt.title("countplot")
        plt.savefig(path / f"countplot.png")
        plt.close()

    def histplot(self,path,data,x):
        plt.figure(figsize=(20, 15))
        sns.histplot(
            data=data,
            x=x,
            hue="label",
            bins=50,
            kde=True,
            stat="density",
            common_norm=False
        )
        plt.title("histplot")
        plt.savefig(path / f"histplot.png")
        plt.close()

    def kdeplot(self,path,data,x):
        plt.figure(figsize=(20, 15))
        sns.kdeplot(
            data=data,
            x=x,
            hue="label",
            fill=True
        )
        plt.title("kdeplot")
        plt.savefig(path / f"kdeplot.png")
        plt.close()

    def pairplot(self,path,data,list_):
        plt.figure(figsize=(20, 15))
        sns.pairplot(
            data[list_],
            hue="label"
        )
        plt.title("pairplot")
        plt.savefig(path / f"pairplot.png")
        plt.close()


