import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Titre de l'application
st.title("Manipulation de données et création de graphiques")

# Sélection du dataset
st.sidebar.header("Configuration des données")
datasets = sns.get_dataset_names()
dataset_name = st.sidebar.selectbox("Quel dataset veux-tu utiliser", datasets)

data = sns.load_dataset(dataset_name)
st.write("### Aperçu des données")
st.write(data.head())

# Sélection des colonnes X et Y
columns = data.columns
col_x = st.sidebar.selectbox("Choisissez la colonne X", columns)
col_y = st.sidebar.selectbox("Choisissez la colonne Y", columns)

# Sélection du type de graphique
graph_type = st.sidebar.selectbox(
    "Quel graphique veux-tu utiliser ?",
    ["scatter_chart", "bar_chart", "line_chart"]
)

# Affichage du graphique
st.write("### Graphique")
if graph_type == "scatter_chart":
    fig, ax = plt.subplots()
    ax.scatter(data[col_x], data[col_y])
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    st.pyplot(fig)
elif graph_type == "bar_chart":
    fig, ax = plt.subplots()
    ax.bar(data[col_x], data[col_y])
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    st.pyplot(fig)
elif graph_type == "line_chart":
    fig, ax = plt.subplots()
    ax.plot(data[col_x], data[col_y])
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    st.pyplot(fig)

# Option pour afficher la matrice de corrélation
show_corr = st.sidebar.checkbox("Afficher la matrice de corrélation")
if show_corr:
    st.write("### Ma matrice de corrélation")
    corr = data.select_dtypes(include=[np.number]).corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)
