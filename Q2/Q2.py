
# import csv
# with open('inputfile.csv', 'r') as infile:
#     r = csv.reader(infile)
# mydata = load_csv('inputfile.csv')
with open(inputfile) as file:
    lines = [line.rstrip() for line in file]

flag = True
errorCodes = []
n = int(lines[0])
for line in lines[1:]:
    data= line.split(' ') 
    if data[1] == 'true': # 'isValid' variable
        continue
    else:
        flag = False
        errorCodes.append(data[3])
if flag:
    print('Yes')
else:
    print('No')
print(errorCodes)