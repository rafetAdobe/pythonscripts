

def spend_money(totalmoney,spentmoney):
    money=totalmoney - spentmoney
    return money

def make_money(totalmoney,earnmoney):
    money=totalmoney+earnmoney
    return money


print("ROCKSTAR GAME")
print("Setup a band and win prize")

bandname = input("Lets setup a band. What is Band Name:")

print("You have 100K to spend")
moneyleft=100000
print("----------------------------------------------------")
print("Lets pick vocalist.....")
vocalistsfile = open("../data/vocalists.txt","r")
vocalistlist = (vocalistsfile.readlines())
 
for i in range(0, len(vocalistlist)):
    liststring=vocalistlist[i].split(',')
    print("list number: ",liststring[0])
    print("Vocalist name:",liststring[1])
    print("Vocalist rating:",liststring[2])
    print("Pay/price: ",liststring[3])
        
vocalistselected=input("Pick your vocalist: ")
vocalistselect=int(vocalistselected)-1
vocalistselectedlist=vocalistlist[vocalistselect].split(',')
moneyleft=spend_money(moneyleft,int(vocalistselectedlist[3]))
print("You have left money:",moneyleft)
vocalistsfile.close()

print("----------------------------------------------------")
print("Lets pick guitarist.....")
guitaristsfile = open("../data/guitarist.txt","r")
guitaristlist = (guitaristsfile.readlines())
 
for i in range(0, len(guitaristlist)):
    liststring=guitaristlist[i].split(',')
    print("list number: ",liststring[0])
    print("Vocalist name:",liststring[1])
    print("Vocalist rating:",liststring[2])
    print("Pay/price: ",liststring[3])
        
guitaristselected=input("Pick your vocalist: ")
guitaristselect=int(guitaristselected)-1
guitaristselectedlist=guitaristlist[guitaristselect].split(',')
moneyleft=spend_money(moneyleft,int(guitaristselectedlist[3]))
print("You have left money:",moneyleft)
guitaristsfile.close()

print("----------------------------------------------------")
print("Lets pick Base Guitarist.....")

bassguitarsistsfile = open("../data/bassguitarists.txt","r")
bassguitaristlist = (bassguitarsistsfile.readlines())
 
for i in range(0, len(bassguitaristlist)):
    liststring=bassguitaristlist[i].split(',')
    print("list number: ",liststring[0])
    print("guitar model:",liststring[1])
    print("guitar rating:",liststring[2])
    print("price: ",liststring[3])
        
bassguitaristselected=input("Pick your bass guitarist: ")
bassguitaristselect=int(bassguitaristselected)-1
bassguitaristselectedlist=bassguitaristlist[bassguitaristselect].split(',')
moneyleft=spend_money(moneyleft,int(bassguitaristselectedlist[3]))
print("You have left money:",moneyleft)
bassguitarsistsfile.close()

print("----------------------------------------------------")
print("Lets pick Batterist.....")

batteristsfile = open("../data/batterists.txt","r")
batteristslist = (batteristsfile.readlines())
 
for i in range(0, len(batteristslist)):
    liststring=batteristslist[i].split(',')
    print("list number: ",liststring[0])
    print("Drum model:",liststring[1])
    print("Drum rating:",liststring[2])
    print("price: ",liststring[3])
        
batteristselected=input("Pick your Batterists: ")
batteristselect=int(batteristselected)-1
batteristselectedlist=batteristslist[batteristselect].split(',')
moneyleft=spend_money(moneyleft,int(batteristselectedlist[3]))
print("You have left money:",moneyleft)
batteristsfile.close()

print("----------------------------------------------------")
print("Lets pick Drum Set....")

batteriesfile = open("../data/batteries.txt","r")
batterieslist = (batteriesfile.readlines())
 
for i in range(0, len(batterieslist)):
    liststring=batterieslist[i].split(',')
    print("list number: ",liststring[0])
    print("guitar model:",liststring[1])
    print("guitar rating:",liststring[2])
    print("price: ",liststring[3])
        
batteriesselected=input("Pick your Drum Set: ")
batteriesselect=int(batteriesselected)-1
batteriesselectedlist=batterieslist[batteriesselect].split(',')
moneyleft=spend_money(moneyleft,int(batteriesselectedlist[3]))
print("You have left money:",moneyleft)
batteriesfile.close()


print("----------------------------------------------------")
print("Lets pick Base guitar.....")

bassguitarsfile = open("../data/bass.txt","r")
bassguitarlist = (bassguitarsfile.readlines())
 
for i in range(0, len(bassguitarlist)):
    liststring=bassguitarlist[i].split(',')
    print("list number: ",liststring[0])
    print("guitar model:",liststring[1])
    print("guitar rating:",liststring[2])
    print("price: ",liststring[3])
        
bassguitarselected=input("Pick your bass guitar: ")
bassguitarselect=int(bassguitarselected)-1
bassguitarselectedlist=bassguitarlist[bassguitarselect].split(',')
moneyleft=spend_money(moneyleft,int(bassguitarselectedlist[3]))
print("You have left money:",moneyleft)
bassguitarsfile.close()

print("----------------------------------------------------")
print("Lets pick Rythm guitar.....")

guitarsfile = open("../data/guitars.txt","r")
guitarlist = (guitarsfile.readlines())
 
for i in range(0, len(guitarlist)):
    liststring=guitarlist[i].split(',')
    print("list number: ",liststring[0])
    print("guitar model:",liststring[1])
    print("guitar rating:",liststring[2])
    print("price: ",liststring[3])
        
guitarselected=input("Pick your bass guitar: ")
guitarselect=int(guitarselected)-1
guitarselectedlist=guitarlist[guitarselect].split(',')
moneyleft=spend_money(moneyleft,int(guitarselectedlist[3]))
print("You have left money:",moneyleft)
guitarsfile.close()

##################################
### put the selections in a profile file in JSON format.
profilefilename=open("bandprofile.json","w+")
vocalistname = vocalistselectedlist[1]
vocalistrating = vocalistselectedlist[2]
vocalistpay = vocalistselectedlist[3]
guitaristname = guitaristselectedlist[1]
guitaristrating = guitaristselectedlist[2]
guitaristpay = guitaristselectedlist[3]
bassguitaristname = bassguitaristselectedlist[1]
bassguitaristrating = bassguitaristselectedlist[2]
bassguitaristpay = bassguitaristselectedlist[3]
batteristname = batteristselectedlist[1]
batteristrating = batteristselectedlist[2]
batteristpay = batteristselectedlist[3]
guitarname = guitarselectedlist[1]
bassguitarname = bassguitarselectedlist[1]
drumsname = batteriesselectedlist[1]

    
datajson="{ \"bandname\": \""+bandname+"\", features: { \"vocalist\" : \""+vocalistname+"\", "
datajson+="\"vocalistrating\":\""+vocalistrating+"\", \"vocalistpay\" : "+vocalistpay+"\","
datajson+="\"guitarist\":\" "+guitaristname+"\", \"guitaristrating\":\""+guitaristrating+"\","
datajson+="\"guitaristpay\": \""+guitaristpay+"\", \"bassguitaristname\": \""+bassguitaristname+"\","
datajson+="\"bassguitaristrating\" : \""+bassguitaristrating+"\","
datajson+="\"bassguitaristpay\" : \""+bassguitaristpay+"\","
datajson+="\"batteristname\" : \""+batteristname+"\","
datajson+="\"batteristrating\" : \""+batteristrating+"\","
datajson+="\"batteristpay\" : \""+batteristpay+"\","
datajson+="\"Guitarmodel\" : \""+guitarname+"\","
datajson+="\"Bassguitarmodel\" : \""+bassguitarname+"\","
datajson+="\"Batteriesmodel\" : \""+drumsname+"\","
datajson+="\"Money Left\" : \""+str(moneyleft)+"\"} }"

print(datajson)
profilefilename.write(datajson)
profilefilename.close()        