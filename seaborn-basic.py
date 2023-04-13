import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("classic") #grafik stili seçimi

rng = np.random.RandomState()

x = np.linspace(0,10,250)
y = np.cumsum(rng.randn(250,6),0)  #rng.random dizi atama np.cumsum=satırları toplayarak gider
sns.set()
# plt.plot(x,y)

# plt.legend("ABCDEF", ncol = 2, loc="best")

iris = pd.read_csv("iris.csv",sep=",")
#print(iris.head())

setosa = iris[iris["variety"] == "Setosa"]
virginica = iris.loc[iris.variety=="Virginica"]
#print(virginica)

#setosa["sepal.length"].plot.hist() #histogram

#sns.kdeplot(setosa["sepal.length"], shade=True , color="b") #yoğunluk grafiği için

# sns.distplot(iris["sepal.length"]) #histogram ve yoğunluk grafikleri genellile birlikte istenir
# sns.distplot(iris["sepal.width"])

#sns.kdeplot(x= iris.sepal_length, y = iris.sepal_width, shade = True, color="grey") #iki boyutlu grafik

# with sns.axes_style("white"):
#     sns.jointplot(x = "sepal_length", y ="sepal_width", data=iris, ) #(kind="kde") belirtilmezse varsayılan olarak saçılım ve histogram beraber gelir/
#     #birleşik ve marjinal dağılım grafiği
    
# plt.show()

"""" İkili İlişkiler Grafiği"""

# sns.pairplot(iris, hue="variety") #Değişkenlerin ikili ilişkilerini görmek için kullanılır
# plt.show()

bahsis = pd.read_csv("tips.csv")
#print(bahsis.head())

bahsis["percentage"] = bahsis["tip"]*100/bahsis["total_bill"]
#print(bahsis.head())

# grid = sns.FacetGrid(bahsis, row="smoker", col="time", margin_titles=True) #kategorilerin histogramı
# grid.map(plt.hist,"percentage", bins = np.linspace(0,40,15))  #değişken haritalandırılır
# plt.show()

# df = pd.DataFrame(bahsis)
# bahsis_df = df.drop(["total_bill","day","smoker"], axis=1)
# with sns.axes_style(style="ticks"):                             #kutu grafiği
#     g = sns.catplot( data=bahsis_df, kind="box")
#     g.set_axis_labels("Gün","Toplam Hesap")
# plt.show()

with sns.axes_style("white"):
    g = sns.catplot(x ="size",data=bahsis, aspect=2,kind="count")
plt.show()