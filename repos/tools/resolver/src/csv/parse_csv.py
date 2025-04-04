import csv
from pathlib import Path
from pprint import pprint

file_path = Path.home() / "workspace.me/__temp__/csv/testmo2.csv"

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    folders = set()
    infomap = dict()
    count=0

    print(next(reader).keys())
    print()
    for row in reader:
        count+=1
        folder = row['Folder']
        case_name = row['\ufeff"Case"']
        case_id = row["Case ID"]
        folders.add(folder)
        info = f"{case_name}"
        if not infomap.get(folder):
            infomap[folder] = list()
        infomap[folder].append(info)
    
    for folder in infomap.keys():
        print(folder)
        try:
            infolist = infomap[folder]
            for info in infolist:
                print(info)
        except:
            continue
    
    print(f"[총 TC 개수]:{count}")