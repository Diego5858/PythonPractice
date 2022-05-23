
Cup = {
  "India"  : {"Cricket" : ["Sumit", "Sudip"], "Football" : ["Sonu", "Monu" ," ssd" , "sdsds"] },
  "Australia" : {"Pool": ["Ayaz" , "Suraj"] , "Swimming" : "Rajjo"},
   }

Countrylist = Cup.keys()
for x in Countrylist:
    print(x)


Choose_Country = input("Country Name : " )
Countryname = Cup.get(Choose_Country).keys()
for y in Countryname:
    print(y)

Choose_Sports = input("Choose Sports : ")
Playername = Cup.get(Choose_Country).get(Choose_Sports)
for z in Playername:
    if z == "Monu":
        # break # u can use break or continue 
        continue
    print(z)

# ---------------------------------------------------------
