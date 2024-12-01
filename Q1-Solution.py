
import csv
print('*' * 30)
print (f"AdventOfCode - Q1 - Solution")
print('*' * 30)

input_file_path = "C:\\Sethu\\Work\\Practice\\AdventOfCode\\2024\\Questions\\Day-1\\Q1-Input.txt"
x = []
y = []

# Reading data from file and create two lists
def Read_Two_Column_File(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            if (len(p) == 2):
                if ( not ("" == p[0].strip())):
                    x.append(int(p[0].strip()))
                if ( not ("" == p[1].strip())):
                    y.append(int(p[1].strip()))

    return x, y

x, y = Read_Two_Column_File(input_file_path)
x.sort()
y.sort()

x_length = len(x)
y_length = len(y)

final_distance = []

# for i in range(x_length):
#     print(i)

if ( x_length <= y_length) :
    #
    for i in range(x_length):
        if (x[i] > y[i]) :
            final_distance.append(x[i] - y[i]) 
        else:
            final_distance.append( y[i] - x[i]) 
    diff_index = y_length - x_length
    if ( diff_index >  0 ) :
        for index, val in enumerate(y, start = diff_index):
            final_distance.append( val - 0) 
else:
    #
    for i in range(y_length):
        if (x[i] > y[i]) :
            final_distance.append(x[i] - y[i]) 
        else:
            final_distance.append( y[i] - x[i]) 
    diff_index = x_length - y_length
    if ( diff_index >  0 ) :
        for index, val in enumerate(y, start = diff_index):
            final_distance.append( val - 0) 

print("Distance = ", sum(final_distance))