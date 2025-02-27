import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

import pickle as pkl

with open("model_XGB.pkl","rb") as files:
    model=pkl.load(files)
with open("ordinal.pkl","rb") as files:
    ordinal=pkl.load(files)
with open("standard.pkl","rb") as files:
    scalar=pkl.load(files)


twn=['','ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
       'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
       'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
       'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
       'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN',
       'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS',
       'PUNGGOL']

stee=['','ANG MO KIO AVE 1', 'ANG MO KIO AVE 3', 'ANG MO KIO AVE 4',
       'ANG MO KIO AVE 10', 'ANG MO KIO AVE 5', 'ANG MO KIO AVE 8',
       'ANG MO KIO AVE 6', 'ANG MO KIO AVE 9', 'ANG MO KIO AVE 2',
       'BEDOK RESERVOIR RD', 'BEDOK NTH ST 3', 'BEDOK STH RD',
       'NEW UPP CHANGI RD', 'BEDOK NTH RD', 'BEDOK STH AVE 1',
       'CHAI CHEE RD', 'CHAI CHEE DR', 'BEDOK NTH AVE 4',
       'BEDOK STH AVE 3', 'BEDOK STH AVE 2', 'BEDOK NTH ST 2',
       'BEDOK NTH ST 4', 'BEDOK NTH AVE 2', 'BEDOK NTH AVE 3',
       'BEDOK NTH AVE 1', 'BEDOK NTH ST 1', 'CHAI CHEE ST', 'SIN MING RD',
       'SHUNFU RD', 'BT BATOK ST 11', 'BT BATOK WEST AVE 8',
       'BT BATOK WEST AVE 6', 'BT BATOK ST 21', 'BT BATOK EAST AVE 5',
       'BT BATOK EAST AVE 4', 'HILLVIEW AVE', 'BT BATOK CTRL',
       'BT BATOK ST 31', 'BT BATOK EAST AVE 3', 'TAMAN HO SWEE',
       'TELOK BLANGAH CRES', 'BEO CRES', 'TELOK BLANGAH DR', 'DEPOT RD',
       'TELOK BLANGAH RISE', 'JLN BT MERAH', 'HENDERSON RD', 'INDUS RD',
       'BT MERAH VIEW', 'HENDERSON CRES', 'BT PURMEI RD',
       'TELOK BLANGAH HTS', 'EVERTON PK', 'KG BAHRU HILL', 'REDHILL CL',
       'HOY FATT RD', 'HAVELOCK RD', 'JLN KLINIK', 'JLN RUMAH TINGGI',
       'JLN BT HO SWEE', 'KIM CHENG ST', 'MOH GUAN TER',
       'TELOK BLANGAH WAY', 'KIM TIAN RD', 'KIM TIAN PL', 'EMPRESS RD',
       "QUEEN'S RD", 'FARRER RD', 'JLN KUKOH', 'OUTRAM PK', 'SHORT ST',
       'SELEGIE RD', 'UPP CROSS ST', 'WATERLOO ST', 'QUEEN ST',
       'BUFFALO RD', 'ROWELL RD', 'ROCHOR RD', 'BAIN ST', 'SMITH ST',
       'VEERASAMY RD', 'TECK WHYE AVE', 'TECK WHYE LANE',
       'CLEMENTI AVE 3', 'WEST COAST DR', 'CLEMENTI AVE 2',
       'CLEMENTI AVE 5', 'CLEMENTI AVE 4', 'CLEMENTI AVE 1',
       'WEST COAST RD', 'CLEMENTI WEST ST 1', 'CLEMENTI WEST ST 2',
       'CLEMENTI ST 13', "C'WEALTH AVE WEST", 'CLEMENTI AVE 6',
       'CLEMENTI ST 14', 'CIRCUIT RD', 'MACPHERSON LANE',
       'JLN PASAR BARU', 'GEYLANG SERAI', 'EUNOS CRES', 'SIMS DR',
       'ALJUNIED CRES', 'GEYLANG EAST AVE 1', 'DAKOTA CRES', 'PINE CL',
       'HAIG RD', 'BALAM RD', 'JLN DUA', 'GEYLANG EAST CTRL',
       'EUNOS RD 5', 'HOUGANG AVE 3', 'HOUGANG AVE 5', 'HOUGANG AVE 1',
       'HOUGANG ST 22', 'HOUGANG AVE 10', 'LOR AH SOO', 'HOUGANG ST 11',
       'HOUGANG AVE 7', 'HOUGANG ST 21', 'TEBAN GDNS RD',
       'JURONG EAST AVE 1', 'JURONG EAST ST 32', 'JURONG EAST ST 13',
       'JURONG EAST ST 21', 'JURONG EAST ST 24', 'JURONG EAST ST 31',
       'PANDAN GDNS', 'YUNG KUANG RD', 'HO CHING RD', 'HU CHING RD',
       'BOON LAY DR', 'BOON LAY AVE', 'BOON LAY PL', 'JURONG WEST ST 52',
       'JURONG WEST ST 41', 'JURONG WEST AVE 1', 'JURONG WEST ST 42',
       'JLN BATU', "ST. GEORGE'S RD", 'NTH BRIDGE RD', 'FRENCH RD',
       'BEACH RD', 'WHAMPOA DR', 'UPP BOON KENG RD', 'BENDEMEER RD',
       'WHAMPOA WEST', 'LOR LIMAU', 'KALLANG BAHRU', 'GEYLANG BAHRU',
       'DORSET RD', 'OWEN RD', 'KG ARANG RD', 'JLN BAHAGIA',
       'MOULMEIN RD', 'TOWNER RD', 'JLN RAJAH', 'KENT RD', 'AH HOOD RD',
       "KING GEORGE'S AVE", 'CRAWFORD LANE', 'MARINE CRES', 'MARINE DR',
       'MARINE TER', "C'WEALTH CL", "C'WEALTH DR", 'TANGLIN HALT RD',
       "C'WEALTH CRES", 'DOVER RD', 'MARGARET DR', 'GHIM MOH RD',
       'DOVER CRES', 'STIRLING RD', 'MEI LING ST', 'HOLLAND CL',
       'HOLLAND AVE', 'HOLLAND DR', 'DOVER CL EAST',
       'SELETAR WEST FARMWAY 6', 'LOR LEW LIAN', 'SERANGOON NTH AVE 1',
       'SERANGOON AVE 2', 'SERANGOON AVE 4', 'SERANGOON CTRL',
       'TAMPINES ST 11', 'TAMPINES ST 21', 'TAMPINES ST 91',
       'TAMPINES ST 81', 'TAMPINES AVE 4', 'TAMPINES ST 22',
       'TAMPINES ST 12', 'TAMPINES ST 23', 'TAMPINES ST 24',
       'TAMPINES ST 41', 'TAMPINES ST 82', 'TAMPINES ST 83',
       'TAMPINES AVE 5', 'LOR 2 TOA PAYOH', 'LOR 8 TOA PAYOH',
       'LOR 1 TOA PAYOH', 'LOR 5 TOA PAYOH', 'LOR 3 TOA PAYOH',
       'LOR 7 TOA PAYOH', 'TOA PAYOH EAST', 'LOR 4 TOA PAYOH',
       'TOA PAYOH CTRL', 'TOA PAYOH NTH', 'POTONG PASIR AVE 3',
       'POTONG PASIR AVE 1', 'UPP ALJUNIED LANE', 'JOO SENG RD',
       'MARSILING LANE', 'MARSILING DR', 'MARSILING RISE',
       'MARSILING CRES', 'WOODLANDS CTR RD', 'WOODLANDS ST 13',
       'WOODLANDS ST 11', 'YISHUN RING RD', 'YISHUN AVE 5',
       'YISHUN ST 72', 'YISHUN ST 11', 'YISHUN ST 21', 'YISHUN ST 22',
       'YISHUN AVE 3', 'CHAI CHEE AVE', 'ZION RD', 'LENGKOK BAHRU',
       'SPOTTISWOODE PK RD', 'NEW MKT RD', 'TG PAGAR PLAZA',
       'KELANTAN RD', 'PAYA LEBAR WAY', 'UBI AVE 1', 'SIMS AVE',
       'YUNG PING RD', 'TAO CHING RD', 'GLOUCESTER RD', 'BOON KENG RD',
       'WHAMPOA STH', 'CAMBRIDGE RD', 'TAMPINES ST 42', 'LOR 6 TOA PAYOH',
       'KIM KEAT AVE', 'YISHUN AVE 6', 'YISHUN AVE 9', 'YISHUN ST 71',
       'BT BATOK ST 32', 'SILAT AVE', 'TIONG BAHRU RD', 'SAGO LANE',
       "ST. GEORGE'S LANE", 'LIM CHU KANG RD', "C'WEALTH AVE",
       "QUEEN'S CL", 'SERANGOON AVE 3', 'POTONG PASIR AVE 2',
       'WOODLANDS AVE 1', 'YISHUN AVE 4', 'LOWER DELTA RD', 'NILE RD',
       'JLN MEMBINA BARAT', 'JLN BERSEH', 'CHANDER RD', 'CASSIA CRES',
       'OLD AIRPORT RD', 'ALJUNIED RD', 'BUANGKOK STH FARMWAY 1',
       'BT BATOK ST 33', 'ALEXANDRA RD', 'CHIN SWEE RD', 'SIMS PL',
       'HOUGANG AVE 2', 'HOUGANG AVE 8', 'SEMBAWANG RD', 'SIMEI ST 1',
       'BT BATOK ST 34', 'BT MERAH CTRL', 'LIM LIAK ST', 'JLN TENTERAM',
       'WOODLANDS ST 32', 'SIN MING AVE', 'BT BATOK ST 52', 'DELTA AVE',
       'PIPIT RD', 'HOUGANG AVE 4', 'QUEENSWAY', 'YISHUN ST 61',
       'BISHAN ST 12', "JLN MA'MOR", 'TAMPINES ST 44', 'TAMPINES ST 43',
       'BISHAN ST 13', 'JLN DUSUN', 'YISHUN AVE 2', 'JOO CHIAT RD',
       'EAST COAST RD', 'REDHILL RD', 'KIM PONG RD', 'RACE COURSE RD',
       'KRETA AYER RD', 'HOUGANG ST 61', 'TESSENSOHN RD', 'MARSILING RD',
       'YISHUN ST 81', 'BT BATOK ST 51', 'BT BATOK WEST AVE 4',
       'BT BATOK WEST AVE 2', 'JURONG WEST ST 91', 'JURONG WEST ST 81',
       'GANGSA RD', 'MCNAIR RD', 'SIMEI ST 4', 'YISHUN AVE 7',
       'SERANGOON NTH AVE 2', 'YISHUN AVE 11', 'BANGKIT RD',
       'JURONG WEST ST 73', 'OUTRAM HILL', 'HOUGANG AVE 6',
       'PASIR RIS ST 12', 'PENDING RD', 'PETIR RD', 'LOR 3 GEYLANG',
       'BISHAN ST 11', 'PASIR RIS DR 6', 'BISHAN ST 23',
       'JURONG WEST ST 92', 'PASIR RIS ST 11', 'YISHUN CTRL',
       'BISHAN ST 22', 'SIMEI RD', 'TAMPINES ST 84', 'BT PANJANG RING RD',
       'JURONG WEST ST 93', 'FAJAR RD', 'WOODLANDS ST 81',
       'CHOA CHU KANG CTRL', 'PASIR RIS ST 51', 'HOUGANG ST 52',
       'CASHEW RD', 'TOH YI DR', 'HOUGANG CTRL', 'KG KAYU RD',
       'TAMPINES AVE 8', 'TAMPINES ST 45', 'SIMEI ST 2',
       'WOODLANDS AVE 3', 'LENGKONG TIGA', 'WOODLANDS ST 82',
       'SERANGOON NTH AVE 4', 'SERANGOON CTRL DR', 'BRIGHT HILL DR',
       'SAUJANA RD', 'CHOA CHU KANG AVE 3', 'TAMPINES AVE 9',
       'JURONG WEST ST 51', 'YUNG HO RD', 'SERANGOON AVE 1',
       'PASIR RIS ST 41', 'GEYLANG EAST AVE 2', 'CHOA CHU KANG AVE 2',
       'KIM KEAT LINK', 'PASIR RIS DR 4', 'PASIR RIS ST 21',
       'SENG POH RD', 'HOUGANG ST 51', 'JURONG WEST ST 72',
       'JURONG WEST ST 71', 'PASIR RIS ST 52', 'TAMPINES ST 32',
       'CHOA CHU KANG AVE 4', 'CHOA CHU KANG LOOP', 'JLN TENAGA',
       'TAMPINES CTRL 1', 'TAMPINES ST 33', 'BT BATOK WEST AVE 7',
       'JURONG WEST AVE 5', 'TAMPINES AVE 7', 'WOODLANDS ST 83',
       'CHOA CHU KANG ST 51', 'PASIR RIS DR 3', 'YISHUN CTRL 1',
       'CHOA CHU KANG AVE 1', 'WOODLANDS ST 31', 'BT MERAH LANE 1',
       'PASIR RIS ST 13', 'ELIAS RD', 'BISHAN ST 24', 'WHAMPOA RD',
       'WOODLANDS ST 41', 'PASIR RIS ST 71', 'JURONG WEST ST 74',
       'PASIR RIS DR 1', 'PASIR RIS ST 72', 'PASIR RIS DR 10',
       'CHOA CHU KANG ST 52', 'CLARENCE LANE', 'CHOA CHU KANG NTH 6',
       'PASIR RIS ST 53', 'CHOA CHU KANG NTH 5', 'ANG MO KIO ST 21',
       'JLN DAMAI', 'CHOA CHU KANG ST 62', 'WOODLANDS AVE 5',
       'WOODLANDS DR 50', 'CHOA CHU KANG ST 53', 'TAMPINES ST 72',
       'UPP SERANGOON RD', 'JURONG WEST ST 75', 'STRATHMORE AVE',
       'ANG MO KIO ST 31', 'TAMPINES ST 34', 'YUNG AN RD',
       'WOODLANDS AVE 4', 'CHOA CHU KANG NTH 7', 'ANG MO KIO ST 11',
       'WOODLANDS AVE 9', 'YUNG LOH RD', 'CHOA CHU KANG DR',
       'CHOA CHU KANG ST 54', 'REDHILL LANE', 'KANG CHING RD',
       'TAH CHING RD', 'SIMEI ST 5', 'WOODLANDS DR 40', 'WOODLANDS DR 70',
       'TAMPINES ST 71', 'WOODLANDS DR 42', 'SERANGOON NTH AVE 3',
       'JELAPANG RD', 'BT BATOK ST 22', 'HOUGANG ST 91',
       'WOODLANDS AVE 6', 'WOODLANDS CIRCLE', 'CORPORATION DR',
       'LOMPANG RD', 'WOODLANDS DR 72', 'CHOA CHU KANG ST 64',
       'BT BATOK ST 24', 'JLN TECK WHYE', 'WOODLANDS CRES',
       'WOODLANDS DR 60', 'CHANGI VILLAGE RD', 'BT BATOK ST 25',
       'HOUGANG AVE 9', 'JURONG WEST CTRL 1', 'WOODLANDS RING RD',
       'CHOA CHU KANG AVE 5', 'TOH GUAN RD', 'JURONG WEST ST 61',
       'WOODLANDS DR 14', 'HOUGANG ST 92', 'CHOA CHU KANG CRES',
       'SEMBAWANG CL', 'CANBERRA RD', 'SEMBAWANG CRES', 'SEMBAWANG VISTA',
       'COMPASSVALE WALK', 'RIVERVALE ST', 'WOODLANDS DR 62',
       'SEMBAWANG DR', 'WOODLANDS DR 53', 'WOODLANDS DR 52',
       'RIVERVALE WALK', 'COMPASSVALE LANE', 'RIVERVALE DR', 'SENJA RD',
       'JURONG WEST ST 65', 'RIVERVALE CRES', 'WOODLANDS DR 44',
       'COMPASSVALE DR', 'WOODLANDS DR 16', 'COMPASSVALE RD',
       'WOODLANDS DR 73', 'HOUGANG ST 31', 'JURONG WEST ST 64',
       'WOODLANDS DR 71', 'YISHUN ST 20', 'ADMIRALTY DR',
       'COMPASSVALE ST', 'BEDOK RESERVOIR VIEW', 'YUNG SHENG RD',
       'ADMIRALTY LINK', 'SENGKANG EAST WAY', 'ANG MO KIO ST 32',
       'ANG MO KIO ST 52', 'BOON TIONG RD', 'JURONG WEST ST 62',
       'ANCHORVALE LINK', 'CANBERRA LINK', 'COMPASSVALE CRES',
       'CLEMENTI ST 12', 'MONTREAL DR', 'WELLINGTON CIRCLE',
       'SENGKANG EAST RD', 'JURONG WEST AVE 3', 'ANCHORVALE LANE',
       'SENJA LINK', 'EDGEFIELD PLAINS', 'ANCHORVALE DR', 'SEGAR RD',
       'FARRER PK RD', 'PUNGGOL FIELD', 'EDGEDALE PLAINS',
       'ANCHORVALE RD', 'CANTONMENT CL', 'JLN MEMBINA', 'FERNVALE LANE',
       'JURONG WEST ST 25', 'CLEMENTI ST 11', 'PUNGGOL FIELD WALK',
       'KLANG LANE', 'PUNGGOL CTRL', 'JELEBU RD', 'BUANGKOK CRES',
       'WOODLANDS DR 75', 'BT BATOK WEST AVE 5', 'JELLICOE RD',
       'PUNGGOL DR', 'JURONG WEST ST 24', 'SEMBAWANG WAY', 'FERNVALE RD',
       'BUANGKOK LINK', 'FERNVALE LINK', 'JLN TIGA', 'YUAN CHING RD',
       'COMPASSVALE LINK', 'MARINE PARADE CTRL', 'COMPASSVALE BOW',
       'PUNGGOL RD', 'BEDOK CTRL', 'PUNGGOL EAST', 'SENGKANG CTRL',
       'TAMPINES CTRL 7', 'SENGKANG WEST AVE', 'PUNGGOL PL',
       'CANTONMENT RD', 'GHIM MOH LINK', 'SIMEI LANE', 'YISHUN ST 41',
       'TELOK BLANGAH ST 31', 'JLN KAYU', 'LOR 1A TOA PAYOH',
       'PUNGGOL WALK', 'SENGKANG WEST WAY', 'BUANGKOK GREEN',
       'PUNGGOL WAY', 'YISHUN ST 31', 'TECK WHYE CRES', 'MONTREAL LINK',
       'UPP SERANGOON CRES', 'SUMANG LINK', 'SENGKANG EAST AVE',
       'YISHUN AVE 1', 'ANCHORVALE CRES', 'ANCHORVALE ST',
       'TAMPINES CTRL 8', 'YISHUN ST 51', 'UPP SERANGOON VIEW',
       'TAMPINES AVE 1', 'BEDOK RESERVOIR CRES', 'ANG MO KIO ST 61',
       'DAWSON RD', 'FERNVALE ST', 'HOUGANG ST 32', 'TAMPINES ST 86',
       'SUMANG WALK', 'CHOA CHU KANG AVE 7', 'KEAT HONG CL',
       'JURONG WEST CTRL 3', 'KEAT HONG LINK', 'ALJUNIED AVE 2',
       'CANBERRA CRES', 'SUMANG LANE', 'CANBERRA ST', 'ANG MO KIO ST 44',
       'ANG MO KIO ST 51', 'BT BATOK EAST AVE 6', 'BT BATOK WEST AVE 9',
       'CANBERRA WALK', 'WOODLANDS RISE', 'TAMPINES ST 61',
       'YISHUN ST 43']

flt_type=['','1 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE',
       'MULTI GENERATION']

flt_model=['','IMPROVED', 'NEW GENERATION', 'MODEL A', 'STANDARD', 'SIMPLIFIED',
       'MODEL A-MAISONETTE', 'APARTMENT', 'MAISONETTE', 'TERRACE',
       '2-ROOM', 'IMPROVED-MAISONETTE', 'MULTI GENERATION',
       'PREMIUM APARTMENT', 'ADJOINED FLAT', 'PREMIUM MAISONETTE',
       'MODEL A2', 'DBSS', 'TYPE S1', 'TYPE S2', 'PREMIUM APARTMENT LOFT',
       '3GEN']

yearold=[""]
for i in range(1965,2024):
    yearold.append(i)

yearnew=[""]
for j in range(2024,2050):
    yearnew.append(j)

st.set_page_config(page_title="Flat Resale",
                   page_icon=None,
                   layout="wide")

with st.sidebar:
    selected=option_menu(None,["Home","Resale Price"],
                     icons=["house","currency-dollar"])

if selected=="Home":
    st.title(":rainbow[Singapore Flats Resale Prices Predicting]")

    st.write('## :violet[Overview]')
    st.write('#### 👉 The resale flat market in Singapore is highly competitive, and it can be challenging to accurately estimate the resale value of a flat. There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration.')
    st.write('#### 👉 The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. ')
    st.write('#### 👉 This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.')
    st.write("")
    st.write('## :red[ML Regression Model]')
    st.markdown("#### 👉 A Regression Machine Learning model is a type of model used to predict the :green[Continuous outcomes] based on the input data...")
    st.write("")
    st.markdown("#### 👉 The Goal of Regression is to establish a relationship between one more independent variables(feautures) and a dependent variable(target) and use this relationship to make the Predictions...")
    st.write('#### 👉 The ML model used in this project is :blue[XGB Regressor].')


if selected=="Resale Price":
    st.title(":rainbow[Singapore Flats Resale Prices Predicting]")

    col1,col2=st.columns(2)
    with col1:
        town1=st.selectbox("Select Town",twn)
        street1=st.selectbox("Select Street",stee)
        flat1=st.selectbox("Select Flat Type",flt_type)
        flat_model1=st.selectbox("Select the Flat Model",flt_model)
        block=st.text_input("Enter Block Number(only numbers=1-9,No A-Z)",max_chars=3)
        sqm=st.text_input("Enter the Floor Area in Sq.mtr(1 to 9)",max_chars=3)
    
    with col2:
        lease=st.selectbox("Lease Commenced Year",yearold)
        resale_year=st.selectbox("Select Resale Year",yearnew)
        month=st.selectbox("Select Month",("",1,2,3,4,5,6,7,8,9,10,11,12))
        lower=st.selectbox("Storey Lower Range",("",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
        upper=st.selectbox("Storey Upper Range",("",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25))
    
    on=st.button("Predict the Price")
    if on:
        try:
            #encoding
            object={"town":[town1],"flat_type":[flat1],"street_name":[street1],
            "flat_model":[flat_model1]}
            t=pd.DataFrame(object)
            f1=ordinal.transform(t)

            town=f1["town"][0]
            flat=f1["flat_type"][0]
            street=f1["street_name"][0]
            flat_model=f1["flat_model"][0]

            final={"town":[town],"flat_type":[flat],"block":[block],"street_name":[street],
            "floor_area_sqm":[sqm],"flat_model":[flat_model],"lease_commence_date":[lease],"resale_year":[resale_year],
            "resale_month":[month],"storey_lower_bound":[lower],"storey_upper_bound":[upper]}
            final_df=pd.DataFrame(final)

            #normalization
            prediction=scalar.transform(final_df)
            
            #Prediction
            
            price_prediction=model.predict(prediction)
            st.success(f"The Predicted Price is 💲 {price_prediction[0]}")

        except:
            st.markdown("#### :red[Oops!, Could not predict, Please Enter all Details Properly]")
