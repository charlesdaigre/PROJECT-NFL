import pandas as pd

#lire mon csv
df_nfl = pd.read_csv('team_stats_2003_2023.csv')

df_nfl.head

df_nfl = pd.read_csv('C:/Users/Charles/Documents/GitHub/PROJECT-NFL/team_stats_2003_2023.csv')

import pandas as pd

# Lire le fichier CSV avec le chemin complet
df_nfl = pd.read_csv('C:/Users/Charles/Documents/GitHub/PROJECT-NFL/team_stats_2003_2023.csv')

# Afficher les 5 premières lignes pour vérifier les données
print(df_nfl.head())

# Optionnel : Afficher des informations sur le DataFrame
print(df_nfl.info())


# Compter les valeurs nulles dans chaque colonne
valeurs_nulles = df_nfl.isnull().sum()

# Afficher le résultat
print("Nombre de valeurs nulles par colonne :")
print(valeurs_nulles)

df_nfl.isnull().mean() * 100

df_nfl.columns

import pandas as pd

# Lire le fichier CSV
df_nfl = pd.read_csv('C:/Users/Charles/Documents/GitHub/PROJECT-NFL/team_stats_2003_2023.csv')

# Grouper par équipe et année, puis additionner les victoires et les défaites
resultats = df_nfl.groupby(['team', 'year'])[['wins', 'losses']].sum()

# Afficher les résultats pour vérifier
print(resultats.head())

import pandas as pd
import matplotlib.pyplot as plt

print(resultats)

