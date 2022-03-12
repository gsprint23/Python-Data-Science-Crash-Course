# FILE IO
# a file stores data on your file system ("on disk")
# 3 step file processing template
# 1. open the file
# 2. process the file (reading contents OR writing contents)
# 3. close the file

# goal: open data.csv, read its contents into a list,
# and convert that list into a 2D list (like a table)

def read_table(filename):
    # filename is a string represents a path to a file we want to open
    # ASIDE
    # path: absolute or a relative
    # absolute path: start with root (/) or Mac/Linux; start with drive (C:\) on Windows
    # uniquely identify a location on your filesystem
    # relative path: they are relative to a current working directory (CWD)
    # 1. 
    infile = open(filename, "r") # "r" is for reading
    # 2.
    lines = infile.readlines()
    print(lines)
    # we want to cleanup the newlines and restructure lines into a 2D list (table)
    table = []
    for line in lines:
        line = line.strip()
        values = line.split(",")
        print(values)
        table.append(values)
    # 3.
    infile.close()
    return table 

def convert_to_numeric(table, header, col_name):
    # figure out what index col_name corresponds to
    col_index = header.index(col_name)
    for row in table:
        try:
            row[col_index] = float(row[col_index])
        except ValueError:
            print("could not convert:", row[col_index])
    
def write_table(filename, table, header=None):
    # 1. 
    outfile = open(filename, "w") # "w" for writing
    # 2.
    # write out header
    if header is not None:
        for i in range(len(header) - 1):
            outfile.write(header[i] + ",")
        outfile.write(header[-1] + "\n")
    # write out data
    for i in range(len(table) - 1):
        row = table[i]
        for j in range(len(row) - 1):
            value = row[j]
            outfile.write(str(value) + ",")
        outfile.write(str(row[-1]) + "\n")
    row = table[-1]
    for j in range(len(row) - 1):
        value = row[j]
        outfile.write(str(value) + ",")
    outfile.write(str(row[-1]))
    # 3.
    outfile.close()

table = read_table("data.csv")
# store header separately
header = table.pop(0)
# convert column1 to a numeric type
convert_to_numeric(table, header, "column1")
print("header:", header)
print("table:")
print(table)
# write the table header + data to a file
write_table("data_copy.csv", table, header)