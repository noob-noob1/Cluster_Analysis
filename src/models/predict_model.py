

def evaluate_model(model, df):
    # Predict the loan eligibility on the testing set
    
    df['Cluster'] = model.predict(df)

    

    # Calculate the confusion matrix
    return df
