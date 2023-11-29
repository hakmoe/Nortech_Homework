import os
import csv
import json
import sys

def find_all_dir_in_dir(dir_path:str):
    """
    Finds all the directories in a directory
    and returns them as a list.
    
    Args:
        dir_path (str): the path to the directory
    Return:
        directories ([]): an array with all the directories
    """
    directories = []
    # listdir gives all the directories and the files in the directory
    for items in os.listdir(dir_path):
        full_path = os.path.join(dir_path,items)
        if os.path.isdir(full_path):
            directories.append(full_path)
    return directories

def find_all_txt_or_json(dir_paths:str):
    """
    finds either the requirements.txt file or
    the package.json file.
    Args:
        dir_path (str): the path to the repository
    Return:
        dir_path_item (os.path): the path to the file
    """
    paths = []
    for dir_path in dir_paths:
        for item in os.listdir(dir_path):
            if item == "requirements.txt":
                paths.append(os.path.join(dir_path, item))
            elif item  == "package.json":
                paths.append(os.path.join(dir_path, item))
    return paths

def makes_csv_file(file_paths:str):
    """
    Takes an array with the paths to the
    requirement files and makes a sbom csv-file
    form it. The csv file has the columns
    ['name','version','type','path'] and each
    of the rows equals on directory.
    Args:
        file_paths(str): the path to the repository
    Return:
        None
    """
    columns = ['name','version','type','path']
    csv_array = [columns]
    for path in file_paths:
        if path.endswith('.txt'):
            text = open(path).read().split('==')
            csv_array.append([text[0],text[1].replace("\n",""),'pip',path])
        elif path.endswith('.json'):
            json_data = json.loads(open(path).read())
            name = json_data.get('name')
            version = json_data.get('version')
            csv_array.append([name,version,'npm',path])
    with open('sbom.csv', mode='w',newline="") as file:
        writer = csv.writer(file)
        for row in csv_array:
            writer.writerow(row)
    print(f"Saved SBOM in csv format to {os.getcwd()}/sbom.csv")



def csv_to_json(csv_path):
    """
    Makes json files from a csv, where
    the number of variables in each of 
    the json file equals the number of
    columns in the csv file. Each of the
    variables in the json file is the same
    name as the column name. One line in the
    csv file equals on json file.
    Args:
        csv_path (str): the path to the csv file
    Returns:
        None
    """
    with open(csv_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            absolute_path = row["path"]
            path = os.path.dirname(row['path'])
            json_file_path = os.path.join(path,"sbom.json")
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(row, json_file, ensure_ascii=False, indent=4)
            print(f"Saved SDOM in JSON format to {json_file_path}")




def main():
    all_dirs = find_all_dir_in_dir(sys.argv[1])
    print(f"Found {len(all_dirs)} repositories")
    find_all = find_all_txt_or_json(all_dirs)
    makes_csv_file(find_all)
    csv_to_json("sbom.csv")

if __name__ == '__main__':
    main()