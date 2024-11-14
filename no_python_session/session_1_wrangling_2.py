import pandas as pd
import glob

path = r'/workspaces/Pyodide_and_Streamlit/no_python_session/Data'

files = glob.glob(path + "/*.csv")
 
print(files)

dfs = {}

for f in files:
    df = pd.read_csv(f)
   
    list_name = f.split("/")[-1][:-17]
 
    dfs[list_name] = df
 
dfs = {key:dfs[key] for key in sorted(dfs.keys())} #sorted the dfs by keys - alphabetically

# print(sorted(dfs.keys()))

permanent_columns = list(dfs['b1_children_in_need'].columns)   [:10]

b1_columns = [f'b1_children_in_need_{column}' if (not column in permanent_columns) else column for column in dfs['b1_children_in_need'].columns]

left_df = dfs['b1_children_in_need']
left_df = left_df.set_axis(b1_columns,axis=1)

for key, df in dfs.items():
    if('headline_figures' not in key
        ) & ('mind-year' not in key
        ) & (key[:1] !='b1'
        ) & (key[0] != 'a'):

        df = df = df.set_axis([f'{key}_{column}' if (not column in permanent_columns) else column for column in df.columns], axis=1)
        left_df = left_df.merge(dfs,how='left',on = permanent_columns)

