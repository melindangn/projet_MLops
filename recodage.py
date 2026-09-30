import pandas as pd

df = pd.read_csv("Movie_Data_File.csv")

# Affiche la liste des colonnes
print(list(df.columns))

import pandas as pd

df = pd.read_csv("Movie_Data_File.csv")

# Dictionnaire de correspondance étoiles -> format texte/chiffre
etoiles_mapping = {
    "½": "rating_0_5",
    "★": "rating_1_0",
    "★½": "rating_1_5",
    "★★": "rating_2_0",
    "★★½": "rating_2_5",
    "★★★": "rating_3_0",
    "★★★½": "rating_3_5",
    "★★★★": "rating_4_0",
    "★★★★½": "rating_4_5",
    "★★★★★": "rating_5_0",
}

# Application du renommage
df = df.rename(columns=etoiles_mapping)

# Vérification
print(df.columns)

df.to_csv("Movie_Data_File.csv", index=False)