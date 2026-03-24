import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Projet Beans & Pods", layout="wide")
df = pd.read_csv('BeansDataSet.csv')
st.sidebar.title("Navigation")
menu = st.sidebar.selectbox("Choisir une section", 
    ['Accueil', 'Données', 'Statistiques', 'Visualisation', 'Recommandations'])

if menu == 'Accueil':
    st.markdown("<center><h1 style='color:yellow'> Beans & Pods </h1></center>", unsafe_allow_html=True)
    st.markdown("<center><h3 style='color:blue'>Analyse des ventes pour Angeli VC</h3></center>", unsafe_allow_html=True)
    
    st.write("---")
    st.write("""
    Cette application a été conçue pour analyser les 440 transactions de Beans & Pods. 
    L'objectif est de comprendre les habitudes d'achat par région et par canal (Store/Online) 
    pour optimiser la prochaine campagne marketing.
    """)
    st.image("https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=500", caption="Analyse de données café")

elif menu == 'Données':
    st.header("1. Aperçu des transactions")
    st.write("Aperçu des 10 premières lignes (head) :")
    st.dataframe(df.head(10))
    
    st.subheader("Dimensions du dataset")
    st.write(f"Nombre de lignes : {df.shape[0]}")
    st.write(f"Nombre de colonnes : {df.shape[1]}")
    
    st.subheader("Colonnes disponibles")
    st.write(df.columns.tolist())

elif menu == 'Statistiques':
    st.header("2. Étude Statistique Descriptive")
    
    st.subheader("Résumé global")

    st.write(df.describe())
    
    st.subheader("Ventes totales par produit")
    produits = ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']
    totaux = df[produits].sum()
    st.bar_chart(totaux)

elif menu == 'Visualisation':
    st.header("3. Analyse Graphique")

    st.subheader("Distribution des ventes par Canal")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x='Channel', y='Robusta', data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("Répartition des clients par Région")
    fig2, ax2 = plt.subplots()
    df['Region'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax2)
    st.pyplot(fig2)

elif menu == 'Recommandations':
    st.header("4. Rapport & Recommandations")
    
    st.subheader("Tendances observées")
    st.info("""
    - Les ventes en ligne (Online) montrent une forte préférence pour les gousses d'Espresso.
    - La région 'South' est notre plus gros marché actuel.
    """)
    
    st.subheader("Stratégie Marketing")