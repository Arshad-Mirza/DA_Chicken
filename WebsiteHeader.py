########
#Import Requests Library
########
import requests

########
#Class WebsiteHeader
#Performing get request and display web header
########
class WebsiteHeader:
    def __init__(self):
        #Call function to perform 'get' request
        GetRequest()
        #Call function to display website header
        Header()

############
#Function Getrequest
#Perform 'get' request on given website
############
def GetRequest():
    #perform 'get' request
    r = requests.get(website, headers=useragent)

    #Display return status
    print("Status code:")
    print("\t *", r.status_code)

    if r.status_code == 200:
        print('Status code: OK')
    else:
        print('ERROR')

############
#Function Header
#Display Header
############
def Header():
    #Perform header response from webiste
    h = requests.head(website, headers=useragent)

    #Display website header
    print("Header:")
    print("############")

    #Loop response to display output line by line
    for x in h.headers:
        print("\t",x,":",h.headers[x])
    print('############')

##################
#Main function
##################

if __name__ == '__main__':

    #Modify User Agent
    useragent = {
        'User-Agent':'Mobile'
    }

    #Define website to retireve data
    website = "http://192.168.186.141/spicyx"

    #Call function GetRequest
    GetRequest()

    #Call function Header
    Header()