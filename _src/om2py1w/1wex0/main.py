from sys import argv

script,filename = argv

targetline = raw_input("Please type in your dairy here: \n")
print("\nyour recent typing is:\n%s\n")%targetline 

Mydairy=open(filename,'a+')
Mydairy.write("\n")
Mydairy.write(targetline)

Mydairy=open(filename)
print("Your dairy record is:" )
print Mydairy.read()
