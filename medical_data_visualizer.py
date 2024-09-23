import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
def isOver(d):
    if d > 25:
        return 1
    else:
        return 0
df['overweight'] =  df['weight']/(df['height']/100)**2    
df['overweight'] = df['overweight'].apply(isOver)

# 3
def normalize(num):
    if num >1:
        return 1
    else:
        return 0

df['gluc'] = df['gluc'].apply(normalize)
df['cholesterol'] =df['cholesterol'].apply(normalize)

# 4
def draw_cat_plot():

    # 5
    df_cat = pd.melt(df,id_vars = ['cardio'],value_vars=['active','alco','cholesterol','gluc','overweight','smoke'],var_name = 'feature',value_name = 'value')


    # 6
    df_cat = df_cat.groupby(['cardio','feature','value']).size().reset_index(name = "total")
    print("cat", df_cat)

    # 7
    df_cat = pd.melt(df,id_vars = ['cardio'],value_vars=['active','alco','cholesterol','gluc','overweight','smoke'],var_name = 'variable',value_name = 'value')
    graphs = sns.catplot(x='variable', hue="value", col="cardio", data=df_cat, kind="count" )
    graphs.set(ylabel = 'total')




    # 8
    fig = graphs


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
