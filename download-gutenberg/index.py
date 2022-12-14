import os

os.system('apt install libdb5.3-dev')
os.system('pip install gutenberg')
os.system('pip install requests')
os.system('pip install pandas')
os.system('pip install numpy')
os.system('pip install bs4')

os.system('pip install nltk')

import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

input = 'gutenberg_metadata.csv' # url of 9073 docs
output = './content/gutenberg_data_10.csv' # ouput file
min = 0 # from file index
max = 10 # to file index

# only removes funny tokens for English texts
def remove_funny_tokens(text):
    tokens = text.split()
    sample = ' '.join(' '.join(tokens).replace('xe2x80x9c', ' ').replace('xe2x80x9d', ' ')\
                                      .replace('xe2x80x94', ' ').replace('xe2x80x99', "'")\
                                      .replace('xe2x80x98', "'")\
                                      .replace('.', "")\
                                      .replace(',', "")\
                                      .replace(':', "")\
                                      .replace('"', "")\
                                      .replace('\'', "")\
                                      .replace('[', "")\
                                      .replace(']', "")\
                                      .replace('|', "")\
                                        .split())
    return sample

# clean newlines, carriage returns and tabs
def clean_text(text):
    cleaned_listed_text = []
    listed_text = list(text)

    for iter in range(len(listed_text) - 1):
        if (listed_text[iter] == '\\' and listed_text[iter + 1] == 'n') or \
            (listed_text[iter] == 'n' and listed_text[iter - 1] == '\\'):
            continue
        elif listed_text[iter] == '\\' and listed_text[iter + 1] == 'r' or \
            (listed_text[iter] == 'r' and listed_text[iter - 1] == '\\'):
            continue
        elif listed_text[iter] == '\\' and listed_text[iter + 1] == 't' or \
            (listed_text[iter] == 't' and listed_text[iter - 1] == '\\'):
            continue
        elif listed_text[iter] == '\\':
            continue
        else:
            cleaned_listed_text.append(listed_text[iter])

    cleaned_text = ''.join([str(char) for char in cleaned_listed_text])
    cleaned_text = remove_funny_tokens(cleaned_text)

    # return filter(''.join(cleaned_text))
    return re.sub(' +', ' ',''.join(cleaned_text))

df_metadata = pd.read_csv(input)

data = {'Author': None, 'Title': None, 'Link': None, 'ID': None, 'Bookshelf': None, 'Text': None}

for key, row in df_metadata.iterrows():
    if key >= min and key < max:
        if data['Author'] == None:
            data['Author'] = [row['Author']]
        else:
            data['Author'].append(row['Author'])
        
        if data['Title'] == None:
            data['Title'] = [row['Title']]
        else:
            data['Title'].append(row['Title'])
        
        if data['Link'] == None:
            data['Link'] = [row['Link']]
        else:
            data['Link'].append(row['Link'])
        
        book_id = int(row['Link'].split('/')[-1])

        if data['ID'] == None:
            data['ID'] = [book_id]
        else:
            data['ID'].append(book_id)
        
        if data['Bookshelf'] == None:
            data['Bookshelf'] = [row['Bookshelf']]
        else:
            data['Bookshelf'].append(row['Bookshelf'])

        text = np.nan
        try:
            text = strip_headers(load_etext(etextno=book_id, 
                                            mirror='http://www.mirrorservice.org/sites/ftp.ibiblio.org/pub/docs/books/gutenberg/')).strip()
            text = ' '.join(' '.join(' '.join(' '.join(text.split('\n')).split('\t')).split('\r')).split('\\r\\n'))
            text = ' '.join(text.split())
            text = clean_text(str(text))
        except:
            try: 
                page = requests.get(row['Link'])
                soup = BeautifulSoup(page.content, 'html.parser')
                text_link = 'http://www.gutenberg.org' + soup.find_all("a", string="Plain Text UTF-8")[0]['href']
                http_response_object = urlopen(text_link)

                text = strip_headers(str(http_response_object.read()))
                text = ' '.join(' '.join(' '.join(' '.join(text.split('\n')).split('\t')).split('\r')).split('\\r\\n'))
                text = ' '.join(text.split())
                text = clean_text(str(text))
            except:
                print("Couldn't acquire text for " + row['Title'] + ' with ID ' + str(book_id) + '. Link: ' + row['Link'] + ' - ' + text_link)
                
        if data['Text'] == None:
            data['Text'] = [' '.join(text.split(' '))]
        else:
            try:
                data['Text'].append(' '.join(text.split(' ')))
            except:
                data['Text'].append(None)
                print("Couldn't save data for " + row['Title'] + ' with ID ' + str(book_id) + '. Link: ' + row['Link'])

df_data = pd.DataFrame(data, columns = ['Title', 'Author', 'Link', 'ID', 'Bookshelf', 'Text'])

df_data.to_csv(output, index=False, encoding='utf-8')
