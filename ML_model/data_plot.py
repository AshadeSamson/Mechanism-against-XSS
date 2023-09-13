import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../dataset/urldata.csv")

print(data.groupby(['label'])['url'].count())
data.groupby(['label'])['url'].count().plot(kind="bar")
plt.show()

