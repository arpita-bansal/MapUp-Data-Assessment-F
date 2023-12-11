import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
 matrix_df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
# Set the diagonal values to 0
for col in matrix_df.columns:
    matrix_df.loc[matrix_df.index == col, col] = 0
    matrix_df


def get_type_count(df)->dict:
    
def car_category(x):
    if x<=15:
        return "low"
    elif x>15 and x<=25:
        return "medium"
    else:
        return "high"
df["Car Cat"] = df["car"].apply(lambda x: car_category(x))
dict1 = df["Car Cat"].value_counts().to_dict()
{k: v for k, v in sorted(list(dict1.items()))}


def get_bus_indexes(df)->list:
a = (np.where(df["bus"] > 2*(df["bus"].mean())))[0].tolist()


def filter_routes(df)->list:
   df_new = df.groupby("route").agg({"truck":"mean"})
    df_new.index.tolist()


def multiply_matrix(matrix)->pd.DataFrame:
  
   matrix_df = matrix_df.applymap(lambda x: round((x*0.75),1) if x>20 else round((x*1.25),1))


def time_check(df)->pd.Series:
    df2 = pd.read_csv("./dataset-2.csv")
    df2 = df2.sort_values(["id","id_2"])
    df2
    
