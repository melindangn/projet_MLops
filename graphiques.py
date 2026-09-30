import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Style des graphiques
sns.set_theme(style="whitegrid")
os.makedirs("figures", exist_ok=True)

# 1. Chargement des données
df = pd.read_csv("Movie_Data_File.csv")

# Nettoyage rapide pour les colonnes numériques si nécessaire
# (ex: s'assurer que 'rating' et 'minute' sont bien au format float/int)
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
print("Colonnes numériques détectées :", list(numeric_cols))

# ---------------------------------------------------------
# Graphique 1 : Distribution des notes (si une colonne note existe)
# ---------------------------------------------------------
rating_col = [c for c in df.columns if "rating" in c.lower() or "score" in c.lower()]
if rating_col:
    col = rating_col[0]
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col].dropna(), kde=True, bins=20, color="#00e054")  # Vert Letterboxd
    plt.title(f"Distribution des notes ({col})", fontsize=14)
    plt.xlabel("Note")
    plt.ylabel("Nombre de films")
    plt.tight_layout()
    plt.savefig("figures/distribution_notes.png", dpi=300)
    plt.close()
    print("-> Graphique 1 sauvegardé : figures/distribution_notes.png")

# ---------------------------------------------------------
# Graphique 2 : Distribution de la durée des films (runtime/minute)
# ---------------------------------------------------------
runtime_col = [c for c in df.columns if "minute" in c.lower() or "runtime" in c.lower() or "duration" in c.lower()]
if runtime_col:
    col = runtime_col[0]
    plt.figure(figsize=(8, 4))
    # On filtre les valeurs aberrantes (ex: durées > 300 min) pour la lisibilité
    filtre_duree = df[df[col].between(40, 250)][col]
    sns.boxplot(x=filtre_duree, color="#40bcf4")
    plt.title("Répartition des durées de films (entre 40 et 250 min)", fontsize=14)
    plt.xlabel("Durée (minutes)")
    plt.tight_layout()
    plt.savefig("figures/boxplot_duree.png", dpi=300)
    plt.close()
    print("-> Graphique 2 sauvegardé : figures/boxplot_duree.png")

# ---------------------------------------------------------
# Graphique 3 : Matrice de corrélation
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
correlation = df[numeric_cols].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
plt.title("Matrice de corrélation des variables numériques", fontsize=14)
plt.tight_layout()
plt.savefig("figures/matrice_correlation.png", dpi=300)
plt.close()
print("-> Graphique 3 sauvegardé : figures/matrice_correlation.png")

print("\nTous les graphiques ont été générés dans le dossier 'figures/'.")