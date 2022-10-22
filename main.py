#!/usr/bin/python
import sys, getopt
""" script to replace strings in binary file """

def main(argv):
   inputfile = ''
   outputfile = ''
   startstring = ''
   newstring = ''
   
   try:
      opts, args = getopt.getopt(argv,"hi:o:s:n:",["ifile=","ofile=","startstr=","--newstr="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile> -s <startstring> -n <newstring>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile> -s <startstring> -n <newstring>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-s", "--startstr"):
         startstring = arg
      elif opt in ("-n", "--newstr"):
         newstring = arg         
    
   print(f'-- Input file is {inputfile}')
   print(f'-- Output file is {outputfile}')
   print(f'-- Output file is {startstring}')
   print(f'-- Output file is {newstring}')
   print('---')

   with open(inputfile, "rb") as f:
       bytes = f.read()
    
   count = bytes.count(f'{startstring}'.encode())
   f.close()

   if count > 0:
       print(f'found "{startstring}": {count} times')
       bytes = bytes.replace(f'{startstring}'.encode(),f'{newstring}'.encode())
       print(f'replaced "{startstring}" with "{newstring}"')
   else:
       print('provided start string not found')

   with open(outputfile, 'wb') as f2:
       f2.write(bytes)

   f2.close()

if __name__ == "__main__":
   main(sys.argv[1:])
   