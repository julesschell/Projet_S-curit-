import numpy as np
import pandas as pd
import pytz


def delete(df, options):
    """
    Delete algorithm that replace all values in a column by an alias.

    Parameters
    ----------
    **options: dict
        Object container

    Other Parameters
    ----------------
        options.columns: list of string
           Column names to apply algorithm
        options.alias: str, default=Nan
            String value to replace affected lines
    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    for col in options.columns:
        df.loc[:, col] = options.alias
    return df

def delete_ids(df, options):
    """
    Replaces given IDs by an alias

    Parameters
    ----------
    **options: dict
        Object container

    Other Parameters
    ----------------
        options.column: string
           Column name to apply algorithm
        options.ids: list of int
            IDs to delete
        options.alias: str, default='DEL'
            String value to replace affected IDs

    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    df.loc[:,options.column] = df.loc[:,options.column].replace(options.ids, options.alias)
    return df

def disturb(df, options):
    """
    Disturb given integer or float typed column with an uniform distribution with parameter p

    Parameters
    ----------
    **options: dict
        Object container

    Other Parameters
    ----------------
        options.column: string
           Column name to apply algorithm
        options.parameter: float
            uniform parameter

    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    df.loc[:,options.column] = df.loc[:,options.column].apply( lambda x: x+np.random.uniform(options.parameter) )
    return df

def pseudo(df, options):
    """
    Find all unique ids and replace each of them by a random value

    Parameters
    ----------
    **options: dict
        Object container

    Other Parameters
    ----------------
        options.column: string
           Column name to apply algorithm

    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    # find all unique ids and create random unique values with size len(ids)+1000
    # Example: if you have ids=[3,5,7], you can generate randomized=[1006,242,938]
    ids = pd.unique( df.loc[:,options.column] )
    randomized = np.random.choice(len(ids)+1000,size=len(ids), replace=False)
    # replace all ids by randomized values
    df.loc[:,options.column] = df.loc[:,options.column].replace(ids, randomized)


def convert_datetime_to_float(df, datetime_column_name, timezone='UTC'):
    """
    Converts a datetime64 column to a float by converting to the total number of seconds 
    since the Unix epoch (1970-01-01 00:00:00 UTC), with consideration for timezone.
    
    Parameters:
    ----------
    df : pandas.DataFrame
        The DataFrame containing the datetime column to convert.
        
    datetime_column_name : str
        The name of the column to be converted to float.
        
    timezone : str
        The timezone of the datetime. For example 'UTC', 'Europe/Paris'. Default is 'UTC'.
    
    Returns:
    -------
    pandas.DataFrame
        A DataFrame with the datetime column replaced by a column of floats, with the timezone offset applied.
    
    Examples:
    --------
    >>> df = pd.DataFrame({'date': pd.to_datetime(['2023-01-01', '2023-01-02'])})
    >>> df = convert_datetime_to_float(df, 'date', timezone='Europe/Paris')
    >>> df
            date
    0  1672531200.0
    1  1672617600.0
    
    Notes:
    -----
    This function does not modify the original DataFrame; a new DataFrame is returned 
    with the modifications. The conversion assumes that the datetime objects are naive and 
    will localize them to the specified timezone before conversion.
    """
    df = df.copy()
    tz = pytz.timezone(timezone)
    df[datetime_column_name] = df[datetime_column_name].apply(lambda x: tz.localize(x).timestamp())
    return df

# Example usage:
# df = pd.DataFrame({'date': pd.to_datetime(['2023-01-01', '2023-01-02'])})
# df = convert_datetime_to_float(df, 'date', timezone='Europe/Paris')
# print(df)


