fileinput = open ("/home/saleemuddin1/PythonSS/ceaser2.txt", "r")
print (fileinput)
value = ""
for lineIn in fileinput:
	value = value +lineIn
print("The File Contents Are: ")
print value
key = input("Please Enter Key: ")
result = ""
for charHolder in value:
	result = result +( chr (((ord(charHolder.lower())- 97 +key) %26) +97) if charHolder.isalpha() else charHolder )
print (result)	
outer = open("out2.txt", "w")
outer.write(result)
outer.close()
print("The decrypted contents are in out2.txt as well!")
