import csv

with open("test.csv", 'w',newline='') as f:
    writer = csv.writer(f)
    H=['Name', 'Cell', 'Profession', 'Email']
    writer.writerow(H)
    writer.writerow(['Donatien', '677492781', 'Devops Engineer', 'donaskt@gmail.com'])
