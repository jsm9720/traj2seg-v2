import csv
import json

def traj_preprocess(data_path):
    csv.field_size_limit(1000000000)
    data = {}
    count = 0
    with open(data_path,"r") as f:
        csv_data = csv.reader(f)
        while True:
            traj = []
            check = True
            try:
                next_csv_data = next(csv_data)[2:]
                r_data = ','.join(next_csv_data)
            except StopIteration:
                print("file read end")
                return data
            json_data = json.loads(r_data)
            for gps in json_data:
                traj.append([gps["lat"],gps["lng"]])
                if(((gps["lat"]<37.389947) | (gps["lat"]>37.576397)) | ((gps["lng"]<126.589849) | (gps["lng"]>126.754442))):
                    check = False
                    break
            if check:
                data[count] = traj
#                path = "traj/traj%s.csv" % count
#                with open(path, 'w', newline='') as f:    # 파일 저장하기
#                    writer = csv.writer(f)
#                    writer.writerow(["lat","lng"])
#                    for i in data[count]:
#                        writer.writerow(i)
                count = count + 1
                if count == 10:  # data 25개만 뽑기 위해
                    return data
    return data


a = traj_preprocess()
