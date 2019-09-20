import requests 
import sys

result=requests.get("https://www.naver.com")
print(result.ok)
#print(result.text)
#print(result.json())
'''
주석
'''
def get2DBarcode(corp_id):
    url = 'http://203.250.22.33/api/get2DBarcode.php'
    data = {'corp_id':corp_id}
    result=requests.post(url,data=data)

    if not result.ok: 
        result.raise_for_status()
        sys.exit()
        pass

    #print(corp_id,result.text)
    return result.json()

theBarcodeList = [] #list()
theBarcodeDict = {} #dict()

for idx in range(50,100):
    barcodeList = get2DBarcode(idx)
  #  print(barcodeList)
    theBarcodeList.append(barcodeList)
    theBarcodeDict[idx]=barcodeList
    pass

#print(theBarcodeList)
#print(theBarcodeDict)
'''
for ithBarcode in theBarcodeList:
    print(ithBarcode)

for ithKey in theBarcodeDict:
    print(ithKey,theBarcodeDict[ithKey])
'''

for idx,ithBarcode in enumerate(theBarcodeList):
    print(idx,ithBarcode)

for idx,ithKey in enumerate(theBarcodeDict):
    print(idx,ithKey,theBarcodeDict[ithKey])
