"""Creates a list of number of backers within bins of 10"""
import csv

#assign csv file to a readable object
with open('DSI_kickstarterscrape_dataset.csv','r', encoding='mac_roman') as csv_file:
    csv_obj = csv.reader(csv_file)
    
    #skip variable title
    next(csv_obj)

    #variable initialization
    backers = [] 
    num_camps = 0

    #count total pledge for each project and number of projects
    for line in csv_obj:
        if line[10] is not '':
            backers.append(int(line[10]))
            num_camps = num_camps + 1

print('Max backers for single campaign:', max(backers))

frq = 0
last_camp = 0

bin_ct = 10 

a = 0
b = bin_ct


while (b-bin_ct) <= max(backers):
    rng = list(range(a,b+1))

    for line in backers:
        if rng[0] <= line <= rng[-1]:
            frq = frq + 1

    print(str(b) + ':',str(frq))
    frq = 0
    
    if a == 0:
        a = a + bin_ct + 1
        b = b + bin_ct
    elif a != 0:
        a = a + bin_ct
        b = b + bin_ct
    
    last_camp = last_camp +1 
