import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class SimpleDatasetInfo:
    def info(self, filename, imagename):
        df = pd.read_csv(filename)
        sns.pairplot(df)
        plt.savefig(imagename)
        return df.describe()
