from datetime import date
import requests
import time
import json

def main():
    i=0
    while(True):
        t=date.today()
        from_date = str(t.strftime("%d-%m-%Y"))
        print(from_date)
        headers={"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
        disricts=[359,392]
        for district in disricts:
            print(district)
            response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district)+"&date="+from_date,headers=headers)
            print(response.json())
            Vcenters = response.json()
            checkSlots(Vcenters)
        time.sleep(6000)

def checkSlots(centers):
    for center in centers["centers"]:
        # print (c["sessions"])
        for s in center["sessions"]:
        # print (s["available_capacity_dose2"])
            if(s["available_capacity_dose1"]>=1):
            # print(center)
                m0="**** "+s["vaccine"]+" **** "
                m1=str(s["available_capacity_dose1"])+" Vaccine Slot Available at Center "+center["name"]+", "+center["block_name"]+", "+center["district_name"]+", Dose 1 for Age "+ str(s["min_age_limit"])+" & above"
                m2="|| Date "+s["date"] +"|| *** DOSE 1*** || "
            # print(message)
                requests.post("https://api.telegram.org/bot1812087446:AAGMKkvTmyCIIcTfdFVEu1iKJA0R5zCeaeI/sendMessage?chat_id=-560862782&text="+m0+m2+m1)

            if(s["available_capacity_dose2"]>=1):
            # print(center)
                m0="**** "+s["vaccine"]+" **** "
                m1=str(s["available_capacity_dose2"])+" Vaccine Slot Available at Center "+center["name"]+", "+center["block_name"]+", "+center["district_name"]+", Dose 2 for Age "+ str(s["min_age_limit"])+" & above"
                m2="|| Date "+s["date"] +"|| *** DOSE 2*** || "
            # print(message)
                requests.post("https://api.telegram.org/bot1812087446:AAGMKkvTmyCIIcTfdFVEu1iKJA0R5zCeaeI/sendMessage?chat_id=-560862782&text="+m0+m2+m1)

if __name__ == "__main__":
    main()
