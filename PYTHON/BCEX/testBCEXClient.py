# coding: utf-8

import requests
import json
import time
import hashlib
requests.packages.urllib3.disable_warnings()

gateway='https://www.bcex.top'
configFile='config.txt'

def getConfig():
    rate=0
    vol=0
    try:
        with open(configFile,'r') as confFile:
            #print(confFile.readlines())
            for line in confFile:
                lineValue=line.split('=')
                if lineValue[0]=='VOL':
                    vol = lineValue[1].strip().replace('\\n','')
                if lineValue[0]=='RATE':
                    rate = lineValue[1].strip().replace('\\n','')
    except:
        print('getConfig Error! Stop ----')
    else:
        return float(rate),float(vol)


def autoLoop():
    loop=True
    count=1
    #get config, rate vol
    rate, vol = getConfig()
    if rate<=0.0 or vol<=0.0:
        print(rate,vol)
        print('getConfig Error! rate,vol<0 Stop ----')
        return
    print('rate=',rate,'vol=',vol)

    while loop:
        try:
            print('************The ',count,'times Start************')
            buy,sale=getTicker('btc','eth')
            print(buy,sale)

        except:
            print('autoLoop Error! Stop ----')
            loop=False
        else:
            #print('************The ',count,'times Finish Success************')
            count+=1
            time.sleep(1)
def getTicker(part,coin):
    """
    :param part: 币种所在交易区(如btc,ckusd,cnet,eth)
    :param coin: 币名(如eth)
    :return:
    # Request
    POST  https://www.bcex.ca/Api_Market/getCoinTrade
    # Response
    {
    	"name": "ETH",
    	"logo": "https://www.bcex.ca/images/coin/coin_eth.png",
    	"price": "0.03000000",
    	"max": 0,
    	"min": 0,
    	"buy": "0.04000000",
    	"sale": "0.04001000",
    	"available_supply": 91563407,
    	"market_cap": 2746902.21,
    	"volume_24h": 0,
    	"change_24h": 0,
    	"Website": false,
    	"Markets": "https://www.bcex.ca/trade/eth2btc/index"
    }

    """
    url = gateway + '/Api_Market/getCoinTrade'+'?part='+part+'&coin='+coin
    # req = requests.get(url, timeout=10000, proxies=proxies)
    try:
        req = requests.get(url, verify=False)
        req.encoding = 'utf-8'
        # print(req.status_code)
        dataJson = json.loads(req.content)
        # printPrettyJson(req.content)
        now = time.strftime('%m-%d %H:%M:%S')
    except:
        print('getTicker Error! Continue ----')
    else:
        print(now + '----coin:' + dataJson['name'] + '----buy:' + dataJson['buy'] + '----sale:' + dataJson['sale'])
        return float(dataJson['buy']),float(dataJson['sale'])
def getPriceList():
    url = gateway+'/Api_Market/getPriceList'
    # req = requests.get(url, timeout=10000, proxies=proxies)
    req = requests.get(url, verify=False)
    req.encoding = 'utf-8'
    print(req.status_code)
    dataJson = json.loads(req.content)
    print(dataJson['btc'][0]['display'])
def getTrustList(symbol,coin):
    """
    :param part: 币种所在交易区(如btc,ckusd,cnet,eth)
    :param coin: 币名(如eth)
    :return:
    # Request
    POST  https://www.bcex.ca/Api_Market/getCoinTrade
    # Response
    {
    	"name": "ETH",
    	"logo": "https://www.bcex.ca/images/coin/coin_eth.png",
    	"price": "0.03000000",
    	"max": 0,
    	"min": 0,
    	"buy": "0.04000000",
    	"sale": "0.04001000",
    	"available_supply": 91563407,
    	"market_cap": 2746902.21,
    	"volume_24h": 0,
    	"change_24h": 0,
    	"Website": false,
    	"Markets": "https://www.bcex.ca/trade/eth2btc/index"
    }

    """
    url = gateway + '/Api_Order/trustList'+'?part='+part+'&coin='+coin
    # req = requests.get(url, timeout=10000, proxies=proxies)
    try:
        req = requests.get(url, verify=False)
        req.encoding = 'utf-8'
        # print(req.status_code)
        dataJson = json.loads(req.content)
        # printPrettyJson(req.content)
        now = time.strftime('%m-%d %H:%M:%S')
    except:
        print('getTicker Error! Continue ----')
    else:
        print(now + '----coin:' + dataJson['name'] + '----buy:' + dataJson['buy'] + '----sale:' + dataJson['sale'])
        return float(dataJson['buy']),float(dataJson['sale'])

def printPrettyJson(text):
    print(json.dumps(json.loads(text),indent=4,sort_keys=False,ensure_ascii=False))
def md5(text):
    md5Value=hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5Value
if __name__ == '__main__':
    print("--------BCEXClient start--------")
    #getPriceList()
    print(md5('hello'))

