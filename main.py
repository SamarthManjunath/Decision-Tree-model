from c45 import C45
import sys

args = sys.argv #command line input is put to args
if (len(args) != 3):
    print("Input is not proper, please provide proper input")
    exit()
data_file = args[1] #.data file which has the dataset which has to be the second parameter is put onto data_file 
name_file = args[2] #.names file which has the attributes of the dataset which has to be the third parameter is put onto name_file
c123 = C45(data_file,name_file) #goes to the c45 class and passses on the command line arguments, data_file and name_file
c123.data_retrieve() #fetch data from the input file
c123.ppd() # preprocess the file so that tree can be created
c123.gt() # Create the tree from the preprocessed data
c123.pt() # Print the generated tree. 

# print ("result of test")
# c123.testNode()