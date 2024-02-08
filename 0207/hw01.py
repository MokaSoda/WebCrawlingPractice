from urllib.request import  urlopen
from urllib.request import   Request
from bs4 import BeautifulSoup as bs

def scraping_use_select(html):
    soup = bs(html, 'html.parser')
    forecasts = (soup.select('li.forecast-tombstone div.tombstone-container'))
    print(f"총 tomestone-container 검색 개수: {len(forecasts)}")

    for tmp in forecasts:
        print("-"*90)
        period = tmp.select_one('p.period-name')
        shortdesc =  tmp.select_one('p.short-desc')
        temp = tmp.select_one('p.temp')
        imagealt = tmp.select_one("img")['alt']
        results = [period, shortdesc, temp, imagealt]
        resultname =  ['Period', 'Short desc', 'Temperature', 'Image desc']
        for idx, result in enumerate(results):
            if result:
                resultType = type(result)
                if resultType != type(' '):
                    resulttoprint = result.getText().strip()
                else:
                    resulttoprint ="\n" + ".\n".join([x.strip() for x in result.split('.')])
                print(f"[{resultname[idx]}]: {resulttoprint}")
            else:
                print(f"[{resultname[idx]}]: 내용이 없습니다.")
    print("-" * 90)



def scraping_use_find(html):
    soup = bs(html, 'html.parser')
    forecastmid = (soup.find_all('li',class_ = 'forecast-tombstone'))
    forecasts = [oneday.find('div',class_ = 'tombstone-container')for oneday in forecastmid]

    print(f"총 tomestone-container 검색 개수: {len(forecasts)}")
    for tmp in forecasts:
        print("-" * 90)
        period = tmp.find('p', class_ = 'period-name')
        shortdesc =  tmp.find('p', class_ = 'short-desc')
        temp = tmp.find('p', class_ = 'temp')
        imagealt = tmp.find("img")['alt']
        results = [period, shortdesc, temp, imagealt]
        resultname =  ['Period', 'Short desc', 'Temperature', 'Image desc']
        for idx, result in enumerate(results):
            if result:
                resultType = type(result)
                if resultType != type(' '):
                    resulttoprint = result.getText().strip()
                else:
                    resulttoprint ="\n" + ".\n".join([x.strip() for x in result.split('.')])
                print(f"[{resultname[idx]}]: {resulttoprint}")
            else:
                print(f"[{resultname[idx]}]: 내용이 없습니다.")
    print("-" * 90)

def main():
    url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY'
    header =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    req = Request(url, headers=header)

    print("National Weather Service Scraping")
    print("-" * 35)

    webpage = urlopen(req)
    print("[find 함수 사용]")
    scraping_use_select(webpage)

    webpage = urlopen(req)
    print("[select 함수 사용]")
    scraping_use_find(webpage)


if __name__ == '__main__':
    main()
