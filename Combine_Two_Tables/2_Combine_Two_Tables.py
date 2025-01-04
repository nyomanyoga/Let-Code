import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    """
    :param person: pd.DataFrame with columns ['personId', 'firstName', 'lastName']
    :param address: pd.DataFrame with columns ['personId', 'city', 'state']
    :return: pd.DataFrame with columns ['firstName', 'lastName', 'city', 'state']
    """
    # Melakukan LEFT JOIN antara person dan address menggunakan kolom 'personId'
    merged_df = pd.merge(person, address, on='personId', how='left')
    
    # Memilih kolom yang relevan
    result = merged_df[['firstName', 'lastName', 'city', 'state']]
    
    return result
