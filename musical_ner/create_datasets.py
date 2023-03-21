import os
import csv
import re

# specify which columns to extract and their corresponding output file names
columns_to_extract = {'artist': 'artist', 'producer': 'artist', 'writer': 'artist', 'album': 'album', 'genre': 'genre', 'subgenre': 'genre', 'song': 'song'}

def create_output_files():
    # create output files and write headers
    for column, output in columns_to_extract.items():
        with open(f'data/{output}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([output])


def write_outputs(folderpath, filename):
    try:
        if filename.endswith('.csv'):
            # open the CSV file
            with open(os.path.join(folderpath, filename), 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                data = list(reader)
                # Find columns to extract
                columns = []
                # print(reader.fieldnames)
                for col, output in columns_to_extract.items():
                    if col in reader.fieldnames:
                        columns.append(col)
                # Extract columns and write them to output files
                for col in columns:
                    with open(f'data/{columns_to_extract[col]}.csv', 'a', newline='') as output_file:
                        writer = csv.writer(output_file)
                        for row in data:
                            if col in row:
                                writer.writerow([row[col]])
    except:
        pass

def remove_duplicates(folder_path, filename):
    # loop through each CSV file in the folder
    try:
        if filename.endswith('.csv'):
            with open(os.path.join(folder_path, filename), 'r') as csvfile:
                reader = csv.reader(csvfile)
                # read the header row
                header = next(reader)  
                rows = []
                for row in reader:
                    rows.append(row)
                unique_rows = list(set(tuple(row) for row in rows))
            with open(os.path.join(folder_path, f'{filename}'), 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)
                for row in unique_rows:
                    writer.writerow(row)
    except:
        pass
     
def split_multiple_genres():
    with open('data/genre.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        unique_rows = []
        header = next(reader)
        for row in reader:
            if ',' in row[0]:
                genres = [genre.strip() for genre in re.split(r"[,/]",row[0])]
                # print(genres)
                for genre in genres:
                    unique_rows.append(genre)
            else:
                unique_rows.append(row[0])
        # print(unique_rows[:50])
    # write unique rows back to file
    with open('data/genre.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in unique_rows:
            writer.writerow([row])

# set the path to the folder containing CSV files
create_output_files()

# write all columns needed from music/data
folder_path = 'data/music_data/'
for filename in os.listdir(folder_path):
    write_outputs(folder_path, filename)

# remove duplicates from exported files
folder_path = 'data/'
for filename in os.listdir(folder_path):
    remove_duplicates(folder_path, filename)

# split rows that contain multiple values in genres.csv and remove duplicates again
split_multiple_genres()
remove_duplicates(folder_path, 'genre.csv')