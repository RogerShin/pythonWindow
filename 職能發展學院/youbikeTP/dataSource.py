import requests
from requests import ConnectionError,HTTPError,Timeout
import sqlite3
from sqlite3 import Error as sqlite3Error

__all__ = ['update_youbike_data']

def download_youbike_data():
    youbikeurl = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    try:
        response = requests.get(youbikeurl)
        response.raise_for_status()
    except ConnectionError as e:
        print("網路連線有問題")
        print(e)
        return
    except HTTPError as e:
        print("statusCode不是200,連線取得資料有問題")
        print(e)
        return
    except Timeout as e:
        print("伺服器忙線中")
        print(e)
        return
    except:
        print("不預期的錯誤")
        return

    allData = response.json()
    #解析資料,傳出[{:}]
    return list(allData["retVal"].values())

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3Error as e:
        print("sqlite連線錯誤")
        print(e)
        return
    return conn

def create_youbike_table(conn):
    sql = '''
    CREATE TABLE IF NOT EXISTS youbike(
    id INTEGER PRIMARY KEY,
    sno TEXT NOT NULL,
    sna TEXT NOT NULL,
    tot INTEGER,
    sbi INTEGER,
    sarea TEXT,
    mday TEXT,
    lat REAL,
    lng REAL,
    ar TEXT,
    bemp INTEGER,
    act INTEGER,
    UNIQUE (sno)
);
    '''

    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except sqlite3Error as e:
        print(e)


def update_youbike_data():
    datalist = download_youbike_data()
    conn = create_connection('youbike.db')
    with conn:
        create_youbike_table(conn)


