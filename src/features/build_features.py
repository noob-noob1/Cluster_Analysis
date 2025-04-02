import pandas as pd

# create dummy features
def create_dummy_vars(df):
    
    categorical= ['Gender']
    df = pd.get_dummies(df, columns=categorical, drop_first=True)
    
    #change true and false to 1 and 0
    
    df = df.astype(int)
    
    # save the dataset
    df.to_csv('data/processed/Processed_mall_customers.csv', index=None)
    

    return df