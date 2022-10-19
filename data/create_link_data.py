import json

def proprecessing():

    with open("incheon.geojson", 'w') as i:
        with open("2019_09_20.geojson", "r") as f:
            while True :
                check = True
                line = f.readline()
                if not line: break
                if "LINK_ID" in line:
                    try:
                        j = json.loads(line[:-2])
#                       print(j)
                    except:
                        j = json.loads(line)
#                       print(j)
                    link = j["properties"]["LINK_ID"]
                    coordinates = j["geometry"]["coordinates"]
                    for gps in coordinates[0]:
                        if(((gps[1]<37.389947) | (gps[1]>37.576397)) | ((gps[0]<126.589849) | (gps[0]>126.754442))):
                            check = False
                            break
                    if check:
#                        print(link)
                        i.write(line)
                else: i.write(line)
    return 0

proprecessing()    
#37.389947, 126.589849   37.576397, 126.754442
