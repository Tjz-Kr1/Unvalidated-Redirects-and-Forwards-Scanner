import requests,sys,time,os, argparse

def main():
    os.system('clear')

    print(top)

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', help='path to file of domain list', nargs=1, dest='domain', required=True)
    parser.add_argument('-w', help='payload wordlist', nargs=1, dest='payload', required=True)

    args = parser.parse_args()


    file = args.domain[0]


    payloads = args.payload[0]

 
    with open(file) as f:

		print ""
		print "Testing.."
		print ""
		time.sleep(4)


                for line in f:
		    with open(payloads) as p:
			for payload in p:
                    	    try:

                        	line2 = line.strip()

                        	line3 = 'https://' + line2 + payload

                        	print line3

                        	response = requests.get(line3, verify=True)    

                        	print response

                        	try:

                            	    if response.history:
                             
                                	print "It has been was redirected"
                             
                                	for resp in response.history:

                                    	    print "|"
                                    	    print resp.status_code, resp.url
                                    

                                	print "Final destination:"

                                	print "+"
                                	print response.status_code, response.url

                                
                           	    else:

                                	print "Request was not redirected"

                            
                        	except:
                            	    print "Error"

                   	    except:

                        	print "Exit"

try:
	main()
except IndexError:
	print(" Usage: python "+sys.argv[0]+" [subdomains.file] [redirect.payload]\n")
        print(" Example python "+sys.argv[0]+" uber.list '//yahoo.com/%2F..'\n")
