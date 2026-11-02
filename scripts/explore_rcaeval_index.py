import pandas as pd
from huggingface_hub import HfApi

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)

idx = pd.read_parquet("hf://datasets/phamquiluan/RCAEval/cases.parquet")

# 1. Toutes les colonnes de l'index
print(idx.columns.tolist())

# 2. Seulement RE2 - Online Boutique
ob = idx[idx["dataset"] == "RE2-OB"]
print("\nNombre de cas RE2-OB :", len(ob))
print(ob.head(10))

# 3. Services et types de panne disponibles
print("\nCas par service :")
print(ob["case"].str.split("_").str[1].value_counts())
print("\nCas par type de panne :")
print(ob["case"].str.split("_").str[2].value_counts())

# 4. Comment les fichiers sont rangés sur Hugging Face pour UN cas
files = HfApi().list_repo_files("phamquiluan/RCAEval", repo_type="dataset")
exemple = ob["case"].iloc[0]
print("\nFichiers du cas", exemple, ":")
for f in files:
    if exemple in f:
        print("  ", f)