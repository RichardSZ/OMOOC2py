prompt=">"

#filename=raw_input(prompt)
message = raw_input(prompt)

Mydairy=open('mydairy.txt','r')
print("dairy log:" )
print Mydairy.read()
print "\n"

print"Dairy now..."

target = raw_input(">>>") 
Mydairy=open('mydairy.txt','a+')
Mydairy.write("\n")
Mydairy.write(target)
