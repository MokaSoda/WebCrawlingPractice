from urllib.request import  urlopen
from urllib.request import   Request
from bs4 import BeautifulSoup as bs


def printResult(locationTxt, currTempTxt, currWeatherTxt, currAirDetails, weatherTxtList):
    print("현재 위치:", locationTxt)
    print("현재 온도:", currTempTxt)
    print("날씨 상태:", currWeatherTxt)
    print("공기 상태:")
    print("\n".join(currAirDetails))
    print("-" * 20)
    print("시간대별 날씨 및 온도")
    for idx, data in enumerate(weatherTxtList):
        if idx < 12:
            print(f"{data[0]:4s}{data[1]:6s}{data[2]:6s}")

def parseWeather(soup):

    locationinfo = soup.select_one('div.title_area > h2.title')
    weatherinfo = soup.select_one('div.weather_info')
    currTemp = weatherinfo.select_one('div.temperature_text')
    currWeather = weatherinfo.select_one('span.weather.before_slash')
    currAir = weatherinfo.select('ul.today_chart_list li.item_today')
    weathertimes = soup.select("div.graph_inner._hourly_weather dt.time em")
    weatherstatus = soup.select("div.graph_inner._hourly_weather dd.weather_box span.blind")
    weathertemps = soup.select("div.graph_inner._hourly_weather dd.degree_point span.num")

    locationTxt = locationinfo.getText().strip()
    currTempTxt = currTemp.getText().strip()
    currWeatherTxt =  currWeather.getText().strip()
    currAirDetails = [air.getText().strip() for air in currAir]
    weathertimeTxt = [time.getText().strip() for time in weathertimes]
    weatherstatustxt = [status.getText().strip() for status in weatherstatus]
    weathertempstxt = [temp.getText().strip() for temp in weathertemps]
    weatherTxtList = list(zip(weathertimeTxt, weatherstatustxt, weathertempstxt))

    return locationTxt, currTempTxt, currWeatherTxt, currAirDetails, weatherTxtList
def main():
    url = 'https://search.naver.com/search.naver?query=%EB%8C%80%EA%B5%AC%EB%B3%B5%ED%98%84%EB%8F%99%EB%82%A0%EC%94%A8'
    header =  {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    req = Request(url, headers=header)
    html = urlopen(req)
    soup = bs(html, 'lxml')

    printResult(*parseWeather(soup))


if __name__ == '__main__':
    main()
