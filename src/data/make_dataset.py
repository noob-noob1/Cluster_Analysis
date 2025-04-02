import pandas as pd

def load_and_preprocess_data(data_path):
    
    # Import the data 
    df = pd.read_csv(data_path)
    
    #Pick only the three columns that are relevant for the model
    df = df[['Gender','Age','Annual_Income','Spending_Score']]
    

    return df