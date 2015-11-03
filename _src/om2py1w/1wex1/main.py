prompt=">"

filename=raw_input(prompt)

Mydairy=open(filename)
print("Historic dairy:" )
print Mydairy.read()
print "\n"

print"Dairy now..."
strq = "q"
strh = "h"
typein = raw_input(">>>")
while typein <> strq: 
    if typein <> strh:
	    Mydairy=open(filename,'a+')
	    Mydairy.write("\n")
	    Mydairy.write(typein)
    else: 	
	    print("h for help")
	    print("q for abort")
    typein = raw_input(">>>")
print "goodbye"
