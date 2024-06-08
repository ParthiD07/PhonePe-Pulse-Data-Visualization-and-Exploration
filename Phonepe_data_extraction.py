#Libaries Used
import os
import json
import pandas as pd
import pymysql
from sqlalchemy import create_engine

#Aggregate Transaction Details
path="C:/Users/user/Desktop/Data Science Project/Phonepe Pulse Data Visualization and Exploration/pulse/data/aggregated/transaction/country/india/state/"
agg_trans_list=os.listdir(path)

agg_trans={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in agg_trans_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)

    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)

        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            Data1=json.load(Data)
            
            for z in Data1['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              agg_trans['Transaction_type'].append(Name)
              agg_trans['Transaction_count'].append(count)
              agg_trans['Transaction_amount'].append(amount)
              agg_trans['State'].append(i)
              agg_trans['Year'].append(j)
              agg_trans['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
agg_trans_data=pd.DataFrame(agg_trans)
agg_trans_data["State"]=agg_trans_data["State"].str.replace('-',' ')
agg_trans_data["State"]=agg_trans_data["State"].str.title()
agg_trans_data['State']=agg_trans_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
agg_trans_data['State']=agg_trans_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Aggregate User Details
path2="C:/Users/user/Desktop/Data Science Project/Phonepe Pulse Data Visualization and Exploration/pulse/data/aggregated/user/country/india/state/"
agg_user_list=os.listdir(path)

agg_user={'State':[], 'Year':[],'Quarter':[],'User_Brands':[], 'User_count':[], 'User_Percentage':[]}

for i in agg_user_list:
    p_i=path2+i+"/"
    Agg_yr=os.listdir(p_i)

    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)

        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            Data2=json.load(Data)
            
            try:
                for z in Data2["data"]["usersByDevice"]:
                    brand=z["brand"]
                    count=z["count"]
                    percentage=z["percentage"]
                    agg_user['User_Brands'].append(brand)
                    agg_user['User_count'].append(count)
                    agg_user['User_Percentage'].append(percentage)
                    agg_user['State'].append(i)
                    agg_user['Year'].append(j)
                    agg_user['Quarter'].append(int(k.strip('.json')))
            except:
                pass

#Converting to dataframe and cleaning
agg_user_data=pd.DataFrame(agg_user)
agg_user_data["State"]=agg_user_data["State"].str.replace('-',' ')
agg_user_data["State"]=agg_user_data["State"].str.title()
agg_user_data['State']=agg_user_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
agg_user_data['State']=agg_user_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Map Transaction Details
path3="C:/Users/user/Desktop/Data Science Project/Phonepe Pulse Data Visualization and Exploration/pulse/data/map/transaction/hover/country/india/state/"
map_trans_list=os.listdir(path)

map_trans={'State':[], 'Year':[],'Quarter':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in map_trans_list:
    p_i=path3+i+"/"
    Agg_yr=os.listdir(p_i)

    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)

        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            Data3=json.load(Data)

            for z in Data3["data"]["hoverDataList"]:
                    name=z["name"]
                    count=z["metric"][0]["count"]
                    amount=z["metric"][0]["amount"]
                    map_trans['District'].append(name)
                    map_trans['Transaction_count'].append(count)
                    map_trans['Transaction_amount'].append(amount)
                    map_trans['State'].append(i)
                    map_trans['Year'].append(j)
                    map_trans['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
map_trans_data=pd.DataFrame(map_trans)
map_trans_data["State"]=map_trans_data["State"].str.replace('-',' ')
map_trans_data["State"]=map_trans_data["State"].str.title()
map_trans_data["District"]=map_trans_data["District"].str.title()
map_trans_data['State']=map_trans_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
map_trans_data['State']=map_trans_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Map User Details
path4='C:/Users/user/Desktop/Data Science Project/Phonepe Pulse Data Visualization and Exploration/pulse/data/map/user/hover/country/india/state/'
map_user_list=os.listdir(path)

map_user={'State':[], 'Year':[],'Quarter':[],'District':[], 'Registered_Users':[], 'App_Opens':[]}

for i in map_user_list:
    p_i=path4+i+"/"
    Agg_yr=os.listdir(p_i)

    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)

        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            Data4=json.load(Data)
            
            for z in Data4["data"]["hoverData"].items():
                district=z[0]
                registeredUsers=z[1]["registeredUsers"]
                appOpens=z[1]["appOpens"]
                map_user['District'].append(district)
                map_user['Registered_Users'].append(registeredUsers)
                map_user['App_Opens'].append(appOpens)
                map_user['State'].append(i)
                map_user['Year'].append(j)
                map_user['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
map_user_data=pd.DataFrame(map_user)
map_user_data["State"]=map_user_data["State"].str.replace('-',' ')
map_user_data["State"]=map_user_data["State"].str.title()
map_user_data['State']=map_user_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
map_user_data['State']=map_user_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Top Transaction Details
path5="C:/Users/user/Desktop/Data Science Project/Phonepe Pulse Data Visualization and Exploration/pulse/data/top/transaction/country/india/state/"
top_trans_list=os.listdir(path)

top_trans={'State':[], 'Year':[],'Quarter':[],'Pincodes':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in top_trans_list:
    p_i=path5+i+"/"
    Agg_yr=os.listdir(p_i)

    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)

        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            Data5=json.load(Data)

            for z in Data5["data"]["pincodes"]:
                entityName=z["entityName"]
                count=z["metric"]["count"]
                amount=z["metric"]["amount"]
                top_trans['Pincodes'].append(entityName)
                top_trans['Transaction_count'].append(count)
                top_trans['Transaction_amount'].append(amount)
                top_trans['State'].append(i)
                top_trans['Year'].append(j)
                top_trans['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
top_trans_data=pd.DataFrame(top_trans)
top_trans_data["State"]=top_trans_data["State"].str.replace('-',' ')
top_trans_data["State"]=top_trans_data["State"].str.title()
top_trans_data['State']=top_trans_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
top_trans_data['State']=top_trans_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Top User Details
path6="C:/Users/user/Desktop/Data Science Project/Phonepe Pulse Data Visualization and Exploration/pulse/data/top/user/country/india/state/"
top_user_list=os.listdir(path)

top_user={'State':[], 'Year':[],'Quarter':[],'Pincodes':[],'Registered_Users':[]}

for i in top_user_list:
    p_i=path6+i+"/"
    Agg_yr=os.listdir(p_i)

    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)

        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            Data6=json.load(Data)

            for z in Data6["data"]["pincodes"]:
                pincode=z["name"]
                registeredUsers=z["registeredUsers"]
                top_user['Pincodes'].append(pincode)
                top_user['Registered_Users'].append(registeredUsers)
                top_user['State'].append(i)
                top_user['Year'].append(j)
                top_user['Quarter'].append(int(k.strip('.json')))

#Converting to dataframe and cleaning
top_user_data=pd.DataFrame(top_user)
top_user_data["State"]=top_user_data["State"].str.replace('-',' ')
top_user_data["State"]=top_user_data["State"].str.title()
top_user_data['State']=top_user_data['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
top_user_data['State']=top_user_data['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#MySQL connection
my_connection = pymysql.connect(host="127.0.0.1",user="root",password="1234")
mycursor = my_connection.cursor()
engine = create_engine("mysql+pymysql://root:1234@127.0.0.1/phonepe")

mycursor.execute('create database if not exists phonepe')
mycursor.execute('use phonepe')

# Tables Creation:
mycursor.execute('''create table if not exists aggregate_transaction(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    Transaction_type VARCHAR(500),Transaction_count BIGINT,
                                    Transaction_amount FLOAT)''')

mycursor.execute('''create table if not exists aggregate_user(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    User_Brands VARCHAR(500),User_count BIGINT,
                                    User_Percentage FLOAT)''')

mycursor.execute('''create table if not exists map_transaction(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    District VARCHAR(500),Transaction_count BIGINT,
                                    Transaction_amount FLOAT)''')

mycursor.execute('''create table if not exists map_user(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    District VARCHAR(500),Registered_Users BIGINT,
                                    App_Opens BIGINT)''')

mycursor.execute('''create table if not exists top_transaction(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    Pincodes INT,Transaction_count BIGINT,
                                    Transaction_amount FLOAT)''')

mycursor.execute('''create table if not exists top_user(State VARCHAR(500),
                                    Year INT,Quarter INT,
                                    Pincodes INT,Registered_Users BIGINT)''')
#Insert dataframe to sql table
agg_trans_data.to_sql('aggregate_transaction',engine,if_exists='append',index=False)
agg_user_data.to_sql('aggregate_user',engine,if_exists='append',index=False)
map_trans_data.to_sql('map_transaction',engine,if_exists='append',index=False)
map_user_data.to_sql('map_user',engine,if_exists='append',index=False)
top_trans_data.to_sql('top_transaction',engine,if_exists='append',index=False)
top_user_data.to_sql('top_user',engine,if_exists='append',index=False)

my_connection.commit()
