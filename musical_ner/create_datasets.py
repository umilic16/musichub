import os
import csv
import re
import numpy as np
import pandas as pd
import json

# functions for extracting information from multiple datasources from keggle and wiki

# specify which columns to extract and their corresponding output file names
columns_to_extract = {'artist': 'artists', 'producer': 'artists', 'writer': 'artists',
                      'album': 'albums', 'genre': 'genres', 'subgenre': 'genres', 'song': 'songs'}


def create_output_files(folderpath):
    # Create output folder if it doesnt exist
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    # create output files and write headers
    for column, output in columns_to_extract.items():
        with open(f'{folderpath}/{output}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([output])


def write_outputs(source_path, output_path):
    try:
        if not os.path.exists(source_path):
            print(f'Source directory: {source_path} doesnt exist')
            return
        for filename in os.listdir(source_path):
            if filename.endswith('.csv'):
                # open the CSV file
                with open(os.path.join(source_path, filename), 'r', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    data = list(reader)
                    # Find columns to extract
                    columns = []
                    for col, output in columns_to_extract.items():
                        if col in reader.fieldnames:
                            columns.append(col)
                    # Create output folder if it doesnt exist
                    if not os.path.exists(output_path):
                        os.makedirs(output_path)
                    # Extract columns and write them to output files
                    for col in columns:
                        with open(f'{output_path}/{columns_to_extract[col]}.csv', 'a', newline='', encoding='utf-8') as output_file:
                            writer = csv.writer(output_file)
                            for row in data:
                                if col in row:
                                    # convert text to lowercase and remove quotation marks and square brackets
                                    text = row[col].lower()
                                    # new_text = re.sub(r'"', '', text)
                                    # text = re.sub(r'[\[\'\"\]]', '', text)
                                    writer.writerow([text])
                    print(f'file {filename} done')
    except Exception as ex:
        print(ex)


def remove_duplicates(folder_path):
    try:
        if not os.path.exists(folder_path):
            print(f'Source directory: {folder_path} doesnt exist')
            return
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as csvfile:
                    # read the CSV file
                    df = pd.read_csv(csvfile)
                    # print(f'processing {filename}')
                    df.drop_duplicates(keep='first', inplace=True)
                with open(os.path.join(folder_path, f'{filename}'), 'w', newline='', encoding='utf-8') as outputfile:
                    df.to_csv(outputfile, index=False)
                    print(f'Removed duplicates from {filename}')
    except Exception as ex:
        print(ex)


def split_multiple_genres(folder_path):
    try:
        if not os.path.exists(folder_path):
            print(f'Source directory: {folder_path} doesnt exist')
            return
        with open(f'{folder_path}/genres.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            unique_rows = []
            header = next(reader)
            for row in reader:
                if ',' in row[0]:
                    genres = [genre.strip() for genre in re.split(
                        r'((?<!\s),| \/ (?=[^\/]+$))', row[0])]
                    for genre in genres:
                        if genre != ',':
                            unique_rows.append(genre)
                else:
                    unique_rows.append(row[0])
        # write unique rows back to file
        with open(f'{folder_path}/genres.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            for row in unique_rows:
                writer.writerow([row.lower()])
            print('genres are split')
    except Exception as ex:
        print(ex)


def split_multiple_artists(folder_path):
    try:
        if not os.path.exists(folder_path):
            print(f'Source directory: {folder_path} doesnt exist')
            return
        with open(f'{folder_path}/artists.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            unique_rows = []
            header = next(reader)
            for row in reader:
                if any(token in row[0] for token in [',', 'ft.', 'feat ', 'featuring ']):
                    artists = [artist.strip() for artist in re.split(
                        r'(,|ft\.|feat |featuring )', row[0])]
                    # print(genres)
                    for artist in artists:
                        unique_rows.append(artist)
                else:
                    unique_rows.append(row[0])
        # write unique rows back to file
        with open(f'{folder_path}/artists.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            for row in unique_rows:
                writer.writerow([row.lower()])
            print('artists are split')
    except Exception as ex:
        print(ex)


source_path = 'data/keggle_data'
output_path = 'data/keggle_data_exported'

# # set the path to the folder containing CSV files
# create_output_files(output_path)

# # write all columns needed from music/data
# write_outputs(source_path, output_path)

# split rows that contain multiple values in genres.csv and remove duplicates again
# split_multiple_genres(output_path)
# split_multiple_artists(output_path)

# # remove duplicates from exported files
# output_path = 'data'
# remove_duplicates(output_path)


# input_dir = 'data/csv_data.old'
# for file in os.listdir(input_dir):
#     # Read CSV file into pandas DataFrame
#     with open(os.path.join(input_dir, file), 'r', encoding='utf-8') as csv_file:
#         df = pd.read_csv(csv_file)
#         file_name = os.path.splitext(file)[0] + '.json'
#         # print(file_name)
#         values = [val for row in df.values for val in row]
#         # df.to_json(f'data/{file_name}', orient='values', indent=4)
#         with open(f'data/{file_name}', 'w', encoding='utf-8') as json_file:
#             json.dump(values, json_file, indent=4)