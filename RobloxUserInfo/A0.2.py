import requests
import json
import time

print('db    db .d8888. d88888b d8888b.   d888888b d8b   db d88888b  .d88b. ')
print("88    88 88'  YP 88'     88  `8D     `88'   888o  88 88'     .8P  Y8.")
print("88    88 `8bo.   88ooooo 88oobY'      88    88V8o 88 88ooo   88    88")
print("88    88   `Y8b. 88~~~~~ 88`8b        88    88 V8o88 88~~~   88    88")
print("88b  d88 db   8D 88.     88 `88.     .88.   88  V888 88      `8b  d8'")
print("~Y8888P' `8888Y' Y88888P 88   YD   Y888888P VP   V8P YP       `Y88P'  Alpha V0.2")
print("---------------------------------------------------------------------")

print("testing git")

vcheck = requests.get("https://versioncheck.iemon.repl.co/")
vcheck_text = vcheck.text

if vcheck_text == "A0.2":
    pass
else:
    print("Version outdated, updating now.")
    currentver = requests.get("https://latestsrc.iemon.repl.co/")
    f = open(vcheck_text+".py", "w")
    f.write(currentver.text)
    f.close()
    print("Installing complete, check for a file named "+vcheck_text+".py")
    time.sleep(3)
    quit()




while True:
    userid = input('Type users ID: ')
    useridstr = str(userid)

    url = 'https://users.roblox.com/v1/users/' + useridstr
    statusurl = 'https://users.roblox.com/v1/users/' + useridstr + '/status'
    locateurl = 'https://www.roblox.com/users/' + useridstr + '/profile'

    b = requests.get(url)
    c = requests.get(statusurl)

    c_json = json.loads(c.text)
    b_json = json.loads(b.text)

    if b.ok == True:
        print('')
        print("Player data found.")
        print('')
        b_json['id'] = str(b_json['id'])
        print('Id: ' + b_json['id'])
        print('Name: ' + b_json['name'])
        print('Display name: ' + b_json['displayName'])
        print('Status: ' + c_json['status'])
        print('description: ' + b_json['description'])
        b_json['isBanned'] = str(b_json['isBanned'])
        print('Is banned: ' + b_json['isBanned'])
        print('Date created: ' + b_json['created'])
        locate = str(locateurl)

        if b_json['isBanned'] == 'False':
            print('Player URL: https://www.roblox.com/users/'+useridstr+'/profile')

        else:
            print("Wont send player URL (player is banned)")
        print('')

        add = open("history.txt", "a")
        add.write("\n"+b_json['name']+' Player URL: https://www.roblox.com/users/'+useridstr+'/profile')
        add.close()

    else:
        print("Unable to locate player data.")


