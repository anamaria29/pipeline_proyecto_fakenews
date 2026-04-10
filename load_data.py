import pandas as pd
from sqlalchemy import create_engine


fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")


fake["label"] = 0
true["label"] = 1


df = pd.concat([fake, true])


engine = create_engine("postgresql://postgres:Sagitario129!@localhost/postgres")


df.to_sql("noticias", engine, if_exists="replace", index=False)

print("Datos cargados correctamente")

print(df.shape)