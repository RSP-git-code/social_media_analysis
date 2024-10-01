#This project represents  Social Media Usage  in Pie Chart form 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Note: the given data is taken from pew Research and it is about Social Media Data of US citizens and data is in % form
social_media_data= pd.read_excel("C:\\Users\\RIYA\\OneDrive\\Desktop\\Social_media_usage.xlsx")
print(social_media_data.head())
young_users=social_media_data['Ages 18-29']
labels=social_media_data['Platform']
sizes=[i for i in young_users]
print(sizes)
colors=['#F7CAC9','#3572A3','#4D997A','#FFCC00','#CB2027' ,'#993F43','#ff80ed','#00ffff','#8a2be2','#ff4040','#00ff7f']
print(sizes)
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%')
plt.title('Social Media Usage (18-29 Years Old)',fontdict={'fontname':'Times New Roman','fontsize':20})
plt.show()
