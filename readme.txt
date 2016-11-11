Name : Abhishek Rajshekhar Rao

ASU ID : 1210425135

Description :

	The backdoor webservice is created which listens on a given port to accept HTTP requests and respond accordingly
 after execution of the command. mysocket.py is the script where initially socket is initailized and binded to the given port.
 If the HttP request supports gzip , the response is compressed using gzip library and is sent in the response.The service responds 
appropriately for all the invalid and valid requests sending 404 and 200 as status code for invalid and valid requests respectively.
