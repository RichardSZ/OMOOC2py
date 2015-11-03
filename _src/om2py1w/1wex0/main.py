prompt=">"

filename=raw_input(prompt)

Mydairy=open(filename)
print("Historic dairy:" )
print Mydairy.read()
print "\n"

print"Dairy now..."

targetline = raw_input(">>>") 
Mydairy=open(filename,'a+')
Mydairy.write("\n")
Mydairy.write(targetline)
