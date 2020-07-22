fileinput = open ("/home/saleemuddin1/PythonSS/message1.txt", "r")
print (fileinput)
value = ""
for lineIn in fileinput:
	value = value +lineIn
print ("The File Contents Are::")
print value
key = input("Please Enter Key: ")
result = ""
for charHolder in value:
	result = result +( chr (((ord(charHolder.lower())- 97 +key) %26) +97) if charHolder.isalpha() else charHolder )
print (result)	
out = open("out1.txt", "w")
out.write(result)
out.close()
print("File Outputs Also Located in out1.txt")
