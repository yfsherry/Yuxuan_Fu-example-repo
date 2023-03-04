
# import csv
# with open('inputfile.csv', 'r') as infile:
#     r = csv.reader(infile)
# mydata = load_csv('inputfile.csv')

n = int(input().strip())
flag = True
errorCodes = []
for i in range(n):
    line = input()
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
