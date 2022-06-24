# -*- coding: utf-8 -*-
from multiprocessing import Pool
from time import sleep
import urllib.request
import pandas as pd

def checker(tup): 
    uuid, url = tup
    try:
        alive = urllib.request.urlopen(url, timeout = 3).code == 200
        return (uuid, str(alive))
    except:
        alive = "False"
        return (uuid, alive)
    
      



if __name__ == "__main__":
    df = pd.read_csv("/home/constantz/Загрузки/bulk_export/organizations_202206221945.csv", nrows = 20)
    pairs = zip(df["uuid"], df["homepage_url"])
    
    p = Pool(10)
    for result in p.imap(checker, pairs):
        with open("sanity.txt","a") as fo:
            fo.write("\t".join(result) + "\n")
    p.terminate()
    p.join()
