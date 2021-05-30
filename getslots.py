from datetime import date
import requests
import time
import json

def main():
    while(True):
        t=date.today()
        from_date = str(t.strftime("%d-%m-%Y"))
        
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',"content-type":"application/json; charset=utf-8"}
        disricts=[395,392]
#         395 - Mumbai, 392 - Thane
        for district in disricts:
#             print(district)
            response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district)+"&date="+from_date,headers=headers)
#             print(response)
            Vcenters = response.json()
            checkSlots(Vcenters)
        time.sleep(60)

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
                requests.post("https://api.telegram.org/<telegram bot key>/sendMessage?chat_id=<group id/chat id>&text="+m0+m2+m1)

            if(s["available_capacity_dose2"]>=1):
            # print(center)
                m0="**** "+s["vaccine"]+" **** "
                m1=str(s["available_capacity_dose2"])+" Vaccine Slot Available at Center "+center["name"]+", "+center["block_name"]+", "+center["district_name"]+", Dose 2 for Age "+ str(s["min_age_limit"])+" & above"
                m2="|| Date "+s["date"] +"|| *** DOSE 2*** || "
            # print(message)
                requests.post("https://api.telegram.org/<telegram bot key>/sendMessage?chat_id=<group id/chat id>&text="+m0+m2+m1)

if __name__ == "__main__":
    main()
