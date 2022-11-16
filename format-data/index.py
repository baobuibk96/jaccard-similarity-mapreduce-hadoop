import os
import sys

os.system('pip install pandas')

import pandas as pd

csv_file = 'gutenberg_data_short_100.csv'
output_path = './out/short_100'
df_metadata = pd.read_csv(csv_file)

def safe_open_w(path):
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')

for key, row in df_metadata.iterrows():
    with safe_open_w(output_path + '/file_' + str(row['ID']) + '.txt') as file:
        content = str(row['ID']) + ' ' + row['Text']
        file.write(content)
        file.close()