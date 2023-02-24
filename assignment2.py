# Could you please write a Python script, which is :
# accepting user input (first question -> how many lines to accept , let's say N)
# -> Then store lines that user has written ( the amount of line is equal to N)
# Each of entered lines make "UPPERCASE" and write it as a JSON file in a format:
# {
#      "N": "2",
#      "1" : "LINE1",
#      "2" : "LINE2"
# } 
import os
import sys
from argparse import ArgumentParser

if __name__ == "__main__":
    arg_parser = ArgumentParser(description="This script read text file and generates json files)")
    arg_parser.add_argument("-o","--output",action ="store",help="Specify a path to read json file")
    #arg_parser.add_argument("-o","--output_dir",action="store",help="output dir")
    arguments = arg_parser.parse_args()
    with open(arguments.output, "w") as file:
    
        size = input("Enter number of lines to accept: ")
        file.write("{\n")
        file.write(f'\t"N" : "{size}",\n')
        len = ord(size) - ord('0') + 1
        for i in range(1, len):
            lines = input(f"{i}. ")
            file.write(f'\t"{i}" : "')
            if (i > len - 2):
                for j in lines:
                    file.write(j.upper())
                file.write('"\n')
            else:
                for j in lines:
                    file.write(j.upper())
                file.write('",')
                file.write('\n')
        #file.write(lines.replace(",",""))
        file.write("}")
    
