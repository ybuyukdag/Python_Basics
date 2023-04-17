import matplotlib.pyplot as plt

yil = [2011, 2012, 2013, 2014, 2015]

oyuncul = [8,10,12,97,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]

# Stack Plot (yığın grafiği)
'''
plt.plot([],[],color="y", label="oyuncu1" )
plt.plot([],[],color="r", label="oyuncu2")
plt.plot([],[],color="b", label="oyuncu3")

plt.stackplot(yil,oyuncul,oyuncu2,oyuncu3, colors=["y","r","b"])
plt.title("Yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("Gol Sayısı")
'''
# Pie (pasta grafiği)
'''
goal_types = ["Penaltı","Akan Oyun","Serbest Vuruş"]

goals = [12,35,7]
colors = ["y","r","b"]

plt.pie(goals,labels=goal_types,colors=colors,shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%") #explode dilimler arası mesafe // #autopct yüzdelik şekilde gösterir 1.1f% formatlı iki % işareti arasında
'''
'''
#Bar Grafiği

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW", width=0.5,color="red")
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi", width=0.5, color ="grey")

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe(Km)")
plt.title("Araç Bilgileri")
'''
import numpy as np

yaslar = np.random.randint(20,120,30)
yas_grupları = np.arange(0,110,10)

plt.hist(yaslar,yas_grupları,histtype="bar",rwidth=0.8)
plt.xlabel("Yaş Grupları")
plt.ylabel("Kişi Sayısı")
plt.title("Histogram Grafiği")

plt.show()
