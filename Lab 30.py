# INSTRUCTOR NOTE: Run this lab first with lines 10-12 commented out
# Opens the file for writing, destroys any existing contents
# myFile = open('C:\\file_005.txt', 'w')
myFile = open('file_005.txt', 'w')
myFile.write('abc123')  # Writes a single line to the file, without the newline
myFile.write('def456\n')  # Writes more text to the file with a newline
myFile.write('ghi789\n')  # Writes additional text to the file with a newline
myFile.close()  # always close the file!

# First run this program with lines 10 - 13 commented out - then uncoment 11 and 12 seperately
# myFile = open('File_005.txt','w')   #This opens the file and destroys the contents
myFile = open ('file_005.txt','a+')  # This opens the file. Subsequent write commands append to the file
myFile.write('\nxyz123\n')  # \n can go before or after.. \ means break away and run the next character
myFile.close()  # Close the file again
