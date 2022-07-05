import csv

file2 = open("improved.csv", "w")
with open('ex2.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    found_section = False
    dates = []

    for row in reader:
        if row[0] == "T":
            header = next(reader)
            for item in header:
                file2.write(f"{item},")
        elif len(row)<0:
            break
        file2.close()
        if not found_section:
            if row[0] == "yy/mm/dd hh:mm:ss":
                header = next(reader)
                print(header)
                itemp_index = header.index("ITEMP")
                found_section = True

        else:
            dates.append(row[itemp_index])
    print(dates)

    with open("improved.csv", "r") as f2:
        reader = csv.reader(f2, delimiter=",")
        header = next(reader)
        print(header)


