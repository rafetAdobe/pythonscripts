import json

instruments = {
    "guitars" : {
        "gibson" :{ 
            "quality" : "95",
            "price" : "1000.00",
            "typeofit" : "electro",
            "color" : "white"
        }
        }
    }


with open('instrumentdata.json','a') as instrumentsfile:
    instrumentsfile.write(json.dumps(instruments,ensure_ascii=False,indent=4))
    
    