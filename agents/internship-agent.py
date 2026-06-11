import pandas as pd

def get_internships():

    df = pd.read_csv(
        "data/internships.csv"
    )

    return df