def main(ReceiverAddress,DuckSenderAddress):
    if '@' in ReceiverAddress :

        if '@' in DuckSenderAddress :
        
            if '@duck.com' in DuckSenderAddress :
            
                print("\n\nYour duck.com address: ")
                print(DuckSenderAddress)
                DuckSenderAddress = DuckSenderAddress.split('@')
        
                print("\nReceivers Email Adress: ")
                print(ReceiverAddress)
                ReceiverAddress = ReceiverAddress.split('@')

                print("\nReversAlias:") 
                print(ReceiverAddress[0]+"_at_"+ReceiverAddress[1]+"_"+DuckSenderAddress[0]+"@"+DuckSenderAddress[1]+"\n\n\n")
            
            else:
            
                print("""
                Please type in a valid @duck.com Address!
            
                example: abcdef@duck.com or just abcdef
                """)
        
        else:
        
            print("\n\nYour duck.com address: ")
            print(DuckSenderAddress+"@duck.com")
        
            print("\nReceivers Email Adress: ")
            print(ReceiverAddress)
        
            ReceiverAddress = ReceiverAddress.split('@')
        
            print("\nReversAlias:") 
            print(ReceiverAddress[0]+"_at_"+ReceiverAddress[1]+"_"+DuckSenderAddress+"@duck.com\n\n\n")

    else:
        print("""
        Please type in a valid Email Address!
            
        example: abcdef@domain.com
        """)  

if (__name__ == "__main__"):
    
    while 42:
	    DuckSenderAddress = input("Type your duck.com address: ")
	    ReceiverAddress = input("Type the receivers address: ")
	    DuckSenderAddress = DuckSenderAddress.lower()
	    
	    if DuckSenderAddress == 'q':
	    	exit
	    else:
	     main(ReceiverAddress,DuckSenderAddress)

