prompt=">"

#filename=raw_input(prompt)


h = ['h','H','help','HELP','?']
q = ['q','quit','abort']

while True:
    message = raw_input(prompt)
    if message in h:
        print""" 
	     help: h/H/help/Help/?
             quit: q/quit/abort
		 """
    elif message in q:
	     print "goodbye"
	     break
    else:
         Mydairy=open('mydairy.txt','r')
         print("dairy log:" )
         print Mydairy.read()
         print "\n"
         print"Dairy now..."
         #target = raw_input(">>>") 
         target = message
         Mydairy=open('mydairy.txt','a+')
         Mydairy.write("\n")
         Mydairy.write(target)
