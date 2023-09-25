import pandas as pd
import datetime
import os

def rename_column(df):
    new_column_names = ['open_time','Open','High','Low','Close','Volume','close_time','quote_volume','count','taker_buy_volume','taker_buy_quote_volume','ignore']
    df.columns = new_column_names
    return df

def epoch_to_datetime(df):
    df['Datetime'] =  df['open_time'].apply(lambda x: datetime.datetime.fromtimestamp(x/1000.0))
    return df

def df_preprocess(parameters):
    data_frames = []
    directory_path = parameters['directory_path']
    time_frame = parameters['time_frame']
    for filename in os.listdir(directory_path):
        if time_frame in filename:
            # Construct the full file path
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)
            df = rename_column(df)
            df = epoch_to_datetime(df)
            df = df[['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']]
            df.set_index('Datetime', inplace=True)

            # Read the CSV file into a DataFrame and store it in the dictionary
            data_frames.append(df)

    df = pd.concat(data_frames)
    df = df.sort_index()
    return df
