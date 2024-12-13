import pandas as pd
example = 1

def change_marital_status(df):
    marital_dict = {'Married':True, 'Widowed':False, 'Single':False}
    df_out = df.copy()
    df_out['Is Married'] = df_out['Marital Status'].map(marital_dict)
    return df_out.drop(columns=['Marital Status'])

def widows_u25(df):
    df_out = df.copy()
    df_out.loc[(df['Age'] <25) & (df['Marital Status'] =='Widowed'), 'Age'] = 25
    return df_out