import csv

with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_obj = csv.reader(csv_file)

    for line in csv_obj:
        print(line[1])

    
