prompt=">"

#filename=raw_input(prompt)

log = 'mydairy.txt'
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
         Mydairy=open(log,'a')
         print("dairy log record:" )
         Mydairy=open(log,'r')
         print Mydairy.read()
         print"Dairy input now..."
         Mydairy=open('mydairy.txt','a+')
         Mydairy.write("\n")
         Mydairy.write(message)
