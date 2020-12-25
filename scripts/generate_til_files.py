import os
from datetime import datetime, timedelta
LOC = './_tils'
ORIGIN_DATE = '2020-11-22'
max_date = datetime.strptime(ORIGIN_DATE.split('.')[0],"%Y-%m-%d")
for i in os.listdir(LOC):
    max_date = max(max_date,datetime.strptime(i.split('.')[0],"%Y-%m-%d"))
# print(max_date)

curr_date = datetime.now()

delta = (curr_date-max_date).days
for i in range(1,delta+1):
    date = (max_date+timedelta(days=i)).strftime("%Y-%m-%d")
    title = date+'.md'
    with open(os.path.join(LOC, title),'w') as f:
        f.write(f"---\nlayout: til\ndate: {date}\n---\n-")
    print(title)
