import requests
import json, ssl, urllib.request
import csv


# 下拉選單資料
def Get_FISHTYP():
    # 寫死
    FishType = {"全部": "A00", "原生種": "A02", "外來種": "A01"}
    return FishType


# 下拉選單資料
def Get_FISHYEAR():
    # 寫死
    FishYear = {
        "全部": "A00",
        "97": "C01",
        "98": "C02",
        "99": "C03",
        "100": "C04",
        "101": "C05",
        "102": "C06",
        "103": "C07",
        "104": "C08",
        "105": "C09",
        "106": "C10",
        "107": "C11",
        "108": "C12",
        "109": "C13",
        "110": "C14",
        "111": "C15",
        "112": "C16",
    }
    return FishYear


# 下拉選單資料
def Get_MAP():
    # 寫死
    FishMap = {
        "一般": "B00",
        "依數量": "B01",
    }
    return FishMap


# 下拉選單資料
def Get_FISHNAME():
    # 寫死
    FishName = {
        "全部": "A00",
        "大鱗副泥鰍": "A02",
        "極樂吻鰕虎": "A02",
        "鯉": "A02",
        "䱗": "A02",
        "鯽": "A02",
        "紅鰭鮊": "A02",
        "扁圓吻鯝": "A02",
        "大鱗鮻": "A02",
        "臺灣白甲魚": "A02",
        "長鰭馬口鱲": "A02",
        "羅漢魚": "A02",
        "中華鰍": "A02",
        "鯔": "A02",
        "鯰": "A02",
        "綠背龜鮻": "A02",
        "褐塘鱧": "A02",
        "日本瓢鰭鰕虎": "A02",
        "花鰻鱺": "A02",
        "溪鱧": "A02",
        "斑鱧": "A02",
        "半紋小䰾": "A02",
        "泥鰍": "A02",
        "蓋斑鬥魚": "A02",
        "鬍鯰": "A02",
        "高體鰟鮍": "A02",
        "唇䱻": "A02",
        "曙首厚唇鯊": "A02",
        "日本鰻鱺": "A02",
        "黃鱔": "A02",
        "太平洋雙色鰻鱺": "A02",
        "刺蓋塘鱧": "A02",
        "克氏褐蛇鰻": "A02",
        "大眼華鯿": "A02",
        "黑邊湯鯉": "A02",
        "側帶丘塘鱧": "A02",
        "珍珠塘鱧": "A02",
        "大棘雙邊魚": "A02",
        "花身鯻": "A02",
        "正叉舌鰕虎": "A02",
        "條紋狹鰕虎": "A02",
        "拜庫雷鰕虎": "A02",
        "銀紋笛鯛": "A02",
        "阿部氏鯔鰕虎": "A02",
        "高屏馬口鱲": "A02",
        "斯奈德小䰾": "A02",
        "尖頭塘鱧": "A02",
        "小眼雙邊魚": "A02",
        "潔身叉舌鰕虎": "A02",
        "金黃叉舌鰕虎": "A02",
        "兔頭瓢鰭鰕虎": "A02",
        "七星鱧": "A02",
        "盤鰭叉舌鰕虎": "A02",
        "棘星塘鱧": "A02",
        "大口湯鯉": "A02",
        "大棘鑽嘴魚": "A02",
        "翹嘴鮊": "A02",
        "布魯雙邊魚": "A02",
        "明多羅龍口蛇鰻": "A02",
        "長吻仰口鰏": "A02",
        "臺灣龍口蛇鰻": "A02",
        "黑體塘鱧": "A02",
        "似鯉黃黝魚": "A02",
        "眼斑厚唇鯊": "A02",
        "六帶鰺": "A02",
        "前鱗龜鮻": "A02",
        "紅鯽": "A02",
        "尖鰭寡鱗鰕虎": "A02",
        "黑斑脊塘鱧": "A02",
        "無棘腹囊海龍": "A02",
        "南方溝鰕虎": "A02",
        "臺灣梅氏鯿": "A02",
        "青鱂": "A02",
        "黑鰭枝牙鰕虎": "A02",
        "黏皮鯔鰕虎": "A02",
        " 寬帶裂身鰕虎": "A02",
        "黑紫枝牙鰕虎": "A02",
        "羅氏裸身鰕虎": "A02",
        "斑點竿鰕虎": "A02",
        "科勒氏鰍鮀": "A02",
        "大海鰱": "A02",
        "環球海鰶": "A02",
        "臺江擬鰕虎": "A02",
        "虱目魚": "A02",
        "橫帶沙鱚": "A02",
        "點帶叉舌鰕虎": "A02",
        "短鑽嘴魚": "A02",
        "勒氏笛鯛": "A02",
        "短棘鰏": "A02",
        "黑棘鯛": "A02",
        "黃鰭棘鰓塘鱧": "A02",
        "四帶牙鯻": "A02",
        "曳絲鑽嘴魚": "A02",
        "齊氏石鮒": "A02",
        "粗首馬口鱲": "A02",
        "臺灣石𩼧" :"A02",
        "臺灣鬚鱲": "A02",
        "短吻小鰾鮈": "A02",
        "臺灣石鮒": "A02",
        "斑帶吻鰕虎": "A02",
        "臺灣間爬岩鰍": "A02",
        "纓口臺鰍": "A02",
        "短臀瘋鱨": "A02",
        "埔里中華爬岩鰍": "A02",
        "陳氏鰍鮀": "A02",
        "高身小鰾鮈": "A02",
        "明潭吻鰕虎": "A02",
        "大吻鰕虎": "A02",
        "高身白甲魚": "A02",
        "短吻紅斑吻鰕虎": "A02",
        "臺灣吻鰕虎": "A02",
        "臺灣䱀": "A02",
        "陽明山吻鰕虎": "A02",
        "長脂瘋鱨": "A02",
        "何氏棘䰾": "A02",
        "菊池氏細鯽": "A02",
        "屏東鬚鱲": "A02",
        "高屏花鰍": "A02",
        "蘭嶼吻鰕虎": "A02",
        "大鱗梅氏鯿": "A02",
        "臺東間爬岩鰍": "A02",
        "韌鰕虎": "A02",
        "南臺吻鰕虎": "A02",
        "細斑吻鰕虎": "A02",
        "南臺中華爬岩鰍": "A02",
        "臺灣棘鯛": "A02",
        "飯島氏銀鮈": "A02",
        "恆春吻鰕虎": "A02",
        "粉紅副尼麗魚": "A01",
        "雜交口孵非鯽": "A01",
        "蛙副雙邊魚": "A01",
        "線鱧": "A01",
        "雜交翼甲鯰": "A01",
        "蟾鬍鯰": "A01",
        "橘色雙冠麗魚": "A01",
        "食蚊魚": "A01",
        "絲鰭毛足鬥魚": "A01",
        "鱅": "A01",
        "大口黑鱸": "A01",
        "鯁": "A01",
        "草魚": "A01",
        "雜交非鯽": "A01",
        "巴西珠母麗魚": "A01",
        "橘尾窄口䰾": "A01",
        "龍鯉": "A01",
        "斑駁尖塘鱧": "A01",
        "高身鯽": "A01",
        "錦鯉": "A01",
        "短攀鱸": "A01",
        "雙斑伴麗魚": "A01",
        "黑帶嬌麗魚": "A01",
        "孔雀花鱂": "A01",
        "青魚": "A01",
        "香魚": "A01",
        "小盾鱧": "A01",
        "鬍子異形": "A01",
        "花身副麗魚": "A01",
        "黃頰副麗魚": "A01",
        "劍尾魚": "A01",
        "朱文錦": "A01",
        "厚唇雙冠麗魚": "A01",
        "銀高體䰾": "A01",
        "雜交小䰾": "A01",
        "吉利非鯽": "A01",
        "平頜鱲": "A01",
        "鰱": "A01",
        "血鸚鵡": "A01",
        "畫眉口孵非鯽": "A01",
        "網紋穗唇䰾": "A01",
        "丹尼氏小䰾": "A01",
        "四帶小䰾": "A01",
        "布氏非鯽": "A01",
        "飾妝鎧弓魚": "A01",
        "雜交副尼麗魚": "A01",
        "珍珠鮐": "A01",
        "小皮頦鱵": "A01",
        "花斑劍尾魚": "A01",
        "縱帶黑麗魚": "A01",
        "莫三比克口孵非鯽": "A01",
        "神仙魚": "A01",
        "眼點麗魚": "A01",
        "麥奇鈎吻鮭": "A01",
        "珍珠毛足鬥魚": "A01",
        "恆河鱯": "A01",
        "條紋鴨嘴鯰": "A01",
        "團頭魴": "A01",
        "長絲𩷶": "A01",
        "圖麗魚": "A01",
        "帆鰭花鱂": "A01",
        "臺灣副細鯽": "A01",
        "大鱗龜鮻": "A02",
        "彈塗魚": "A02",
        "大眼海鰱": "A02",
        "長鰭莫鯔": "A02",
        "黃鰭棘鯛": "A02",
        "漢氏稜鯷": "A02",
        "斷線雙邊魚": "A02",
        "圈頸鰏": "A02",
        "仰口鰏": "A02",
        "大彈塗魚": "A02",
        "高體斑鮃": "A02",
        "斑海鯰": "A02",
        "薛氏莫鯔": "A02",
        "斑雞魚": "A02",
        "鬚鰻鰕虎": "A02",
        "谷津氏絲鰕虎": "A02",
        "金錢魚": "A02",
        "長吻管嘴魚": "A02",
        "星雞魚": "A02",
        "布氏鯧鰺": "A02",
        "六斑二齒魨": "A02",
        "太平洋棘鯛": "A02",
        "中國小沙丁魚": "A02",
        "尖吻蛇鰻": "A02",
        "日本銀身䱛": "A02",
        "項斑項鰏": "A02",
        "中華烏塘鱧": "A02",
        "鈍吻叉舌鰕虎": "A02",
        "黃姑魚": "A02",
        "尖頭曲齒鯊": "A02",
        "汙翅真鯊": "A02",
        "路易氏雙髻鯊": "A02",
        "鮻": "A02",
        "紅牙䱛": "A02",
        "銀雞魚": "A02",
        "布氏鬚鰨": "A02",
        "白帶魚": "A02",
        "日本海鰶": "A02",
        "日本花鱸": "A02",
        "浪人鰺": "A02",
        "奧奈鑽嘴魚": "A02",
        "四點似青鱗魚": "A02",
        "黑邊布氏鰏": "A02",
        "逆鈎鰺": "A02",
        "多鱗沙鮻": "A02",
        "四指馬鮁": "A02",
        "多鱗四指馬鮁": "A02",
        "吉打副葉鰺": "A02",
        "尾紋雙邊魚": "A02",
        "黑尾小沙丁魚": "A02",
        "赤鼻稜鯷": "A02",
        "花錐脊塘鱧": "A02",
        "細紋鰏": "A02",
        "半紋鋸鱗鰕虎": "A02",
        "裸頰鋸鱗鰕虎": "A02",
        "前鰭多環海龍": "A02",
        "爪哇擬鰕虎": "A02",
        "清尾鯔鰕虎": "A02",
        "革條田中鰟鮍": "A02",
        "雜交吉利非鯽": "A01",
        "高體高鬚魚": "A01",
    }
    return FishName
