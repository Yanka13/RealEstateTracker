import pandas as pd
import numpy as np

# preprocessing functions

df = pd.read_csv("../raw_data/real_estate_data.csv",index_col="Unnamed: 0").drop(columns="Unnamed: 0.1")
df = df.drop(columns=["elevator","heating","floor"])

def surface(df):
    # dropping nulls
    df_nonull = df[df['surface'].notna()]
    # cleaning string
    new = df_nonull["surface"].str.split(" ", n = 1, expand = True)
    df_nonull["surface"] = new[0]
    # filter numbers
    df_nonull = df_nonull[df_nonull['surface'].str.isnumeric()]
    # to float
    df_nonull["surface"] = df_nonull["surface"].astype(float)
    df = df_nonull
    return df

def neighborhood(df):
    # new data frame with split value columns
    new = df["neighborhood"].str.split(" en ", n = 1, expand = True)

    # making separate housetype
    df["nhousetype"]= new[0]

    # making separate dirty neighborhood
    df["ndirty"]= new[1]

    # cleaning neighborhood
    new = df["ndirty"].str.split(" en ", n = 1, expand = True)
    df["neighborhood"] = new[1]
    df["neighborhood"] = df["neighborhood"].apply(lambda x: x.split(",")[-1])
    df = df.drop(columns="ndirty")
    return df

def price(df):
    # cleaning string
    new = df["price"].str.split(" ", n = 1, expand = True)
    new[0] = new[0].str.replace(".","")
    df["price"] = new[0]
    # number filter
    df = df[df['price'].str.isnumeric()]
    # to float
    df["price"] = df["price"].astype(float)
    return df

def rooms(df):
    # rooms
    # cleaning string
    new = df["rooms"].str.split(" ", n = 1, expand = True)
    # to float
    new[0] = new[0].astype(float)
    df["rooms"] = new[0]
    df_clean = df
    return df_clean

def preprocess(df):
    df = surface(df)
    df = neighborhood(df)
    df = price(df)
    df = rooms(df)
    return df
