import pandas as pd


# print(df.head())
# print(df.info())
# print(df[df["Gender"]=='M'])
def preprocess_data():
    df = pd.read_csv("Data/card.csv")
    df = df.drop(columns=['Card Type' , 'Gender' , 'Exp Type'])
    df['Date'] = pd.to_datetime(df['Date'], format = '%d-%b-%y')
    df.columns = df.columns.str.lower()
    df['city'] = df['city'].str.replace(', India', '',regex = False)
    df['month'] = df['date'].dt.to_period('M')
    df['amount'] = df['amount'].astype(float)
    monthly = df.groupby('month')['amount'].sum().reset_index()
    monthly['month_num'] = range(len(monthly))

    return monthly


# print(preprocess_data())