wheather=['Sunny','Sunny','Overcast','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','cool','cool','cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
from sklearn import preprocessing
le =preprocessing.LabelEncoder()
wheather_encoded=le.fit_transform(wheather)
print (wheather_encoded) 
temp_encoded=le.fit_transform(temp) 
label=le.fit_transform(play)
print ("Temp:",temp_encoded)
print ("play:",label)
features=list(zip(wheather_encoded,temp_encoded))
print(features)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(features,label)
predicted= model.predict([[0,2]]) 
print ("Predicted Value:", predicted)
print(Sunny-2,Overcast-1,Rainy-0)
print(Hot-2,cool-1,Mild-0)
print(No-0,Yes-1)
in(input(enter the value for wheather))
b=enter the value for temperature

