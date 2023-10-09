import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../dataset/urls_dataset.csv")

print(data.groupby(['type'])['url'].count())
data.groupby(['type'])['url'].count().plot(kind="bar")
plt.show()

