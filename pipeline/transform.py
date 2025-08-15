from config import TABLE_NAME
import pandas as pd

# Transform function to process the DataFrame
def transform(df):

    print("Transforming data...")

    # Order of the following transformations is up to you...

    #TODO: Drop rows with missing essential fields 
    # we'll need the org and user to be able to link the user to the org and the action, 
    # what they did, and how it could affect the credit balance
    # (we can assume a missing credits value = 1 credit)

    #TODO:Trim whitespace and normalise strings
        
    #TODO: Fill missing optional numeric fields

    #TODO: Parse dates to a consistent format

    #TODO: Ensure users only belong to a single organisation

    return df
