import pandas as pd
import numpy as np

# 1. Chargement des données
df = pd.read_csv("Movie_Data_File.csv")

# ---------------------------------------------
# STATISTIQUES DESCRIPTIVES
# ---------------------------------------------
print("=== 1. APERÇU GÉNÉRAL ===")
print(f"Dimensions (lignes, colonnes) : {df.shape}")
print("\nTypes des colonnes et valeurs non nulles :")
print(df.info())

print("\n=== 2. STATISTIQUES DES VARIABLES NUMÉRIQUES ===")
# Affiche moyenne, écart-type, min, quartiles, max
print(df.describe())

print("\n=== 3. VÉRIFICATION DES VALEURS MANQUANTES (NaN) ===")
valeurs_nulles = df.isnull().sum()
print(valeurs_nulles[valeurs_nulles > 0])

print("\n=== 4. VÉRIFICATION DES DOUBLONS ===")
print(f"Nombre de doublons stricts : {df.duplicated().sum()}")


# ---------------------------------------------
# NETTOYAGE DES DONNÉES (CLEANING)
# ---------------------------------------------

# Suppression des doublons s'il y en a
df_cleaned = df.drop_duplicates().copy()

# Exemple de traitement des valeurs manquantes :
# - Supprimer les lignes où le titre ou l'année manque
if 'name' in df_cleaned.columns:
    df_cleaned = df_cleaned.dropna(subset=['name'])

# Sauvegarde du dataset propre pour la suite du pipeline MLOps
df_cleaned.to_csv("Movie_Data_Cleaned.csv", index=False)
print("\nNettoyage terminé ! Fichier enregistré sous 'Movie_Data_Cleaned.csv'.")