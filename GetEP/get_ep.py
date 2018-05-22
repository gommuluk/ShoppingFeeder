# -*- coding: utf-8 -*-

import os
import pymongo
import csv
import urllib.request


# Connect to MongoDB
# You sholud have to save environmental variable named 'PRODUCTS_USER'
connection = pymongo.MongoClient(os.environ['PRODUCTS_USER'])
db = connection.EP_DATA

# file download
url = 'https://leocomfile.blob.core.windows.net/navershopping/navershopping.tsv'

# You sholud have to save environmental variable named 'OUT_PATH' to set save path
outpath = os.environ['OUT_PATH']
outfile = "out_test.tsv"

# Create when directory does not exist
if not os.path.isdir(outpath):
    os.makedirs(outpath)

# download
urllib.request.urlretrieve(url, outpath+outfile)


# read tsv file
with open(outpath + outfile,  encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter='\t')

    # get header
    headers = next(reader)

    for row in reader:
        dmp = {} #empty
        for i in range(0, len(headers)):
            # save as JSON
            dmp[headers[i]] = row[i]
        dmp["is_updated"] = "Y"
        #print("출력: " + dmp["is_updated"] + ", " + db.products.find({"id" : dmp["id"]})[0]["is_updated"])

        # get one item from tsv file with id
        cur = db.products.find({"id": dmp["id"]})
        try:
            cur_tmp = cur[0]
            del cur_tmp['_id'] # delete serial number

            #if sorted(cuttt.items()) != sorted(dmp.items()):
            for j in range(0, len(headers)):
                str = headers[j]

                # check whether 'need to update' or not
                if cur_tmp[str] != dmp[str]:
                    # set old value to new value
                    db.products.update({"id": cur_tmp["id"]}, {'$set': {str: dmp[str]}})

        except IndexError:
            print('It is new item')
            db.products.insert_one(dmp)


# if 'is_updated' is "N", delete that instance.
db.products.remove({"is_updated": "N"})

# initialize
is_it_possible = db.products.find()
for i in range(0, db.products.count()):
    if is_it_possible[i]["is_updated"] == 'Y':
        db.products.update({"id": is_it_possible[i]["id"]}, {'$set': {"is_updated": "N"}}, upsert=False, multi=False)

