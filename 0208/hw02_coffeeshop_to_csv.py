# %% [markdown]
# ## 데이터 수집

# %%
import aiohttp
import asyncio
import pandas as pd
from bs4 import BeautifulSoup

# %%


baseurl = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={}&sido=&gugun=&store='


async def getWebsite(session: aiohttp.ClientSession, url):
    result = await session.get(url)
    content = await result.content.read()
    return content


async def limitWithAiohttp(urls):
    result = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(getWebsite(session, url))
        result = await asyncio.gather(*tasks)
        # for task in tasks:
        #     result.append(await task)
    return result


async def main():
    urls = [baseurl.format(i) for i in range(1, 52)]
    result = await limitWithAiohttp(urls)

    location_total = []
    location_detail_total = []
    address_total = []
    phoneNum_total = []

    for test in [BeautifulSoup(oneresult, 'lxml') for oneresult in result]:
        for save in test.select('table.tb_store tbody tr'):
            location = save.select_one('td.noline.center_t').get_text().strip()
            location_detail = save.select_one('td.center_t a').get_text().strip()
            address = save.select('td.center_t')[3].select_one('a').get_text()
            phoneNum = save.select('td.center_t')[5].get_text().strip()

            location_total.append(location)
            location_detail_total.append(location_detail)
            address_total.append(address)
            phoneNum_total.append(phoneNum)

    header = ['매장이름', '지역', '주소', '전화번호']
    beforeDF = zip(location_detail_total, location_total, address_total, phoneNum_total)

    df = pd.DataFrame(beforeDF, columns=header)
    for idx, x in enumerate(df.values, 1):
        print(f"[{idx:>3d}]: 매장이름: {x[0]}, 지역: {x[1]}, 주소:{x[2]}, 전화번호: {x[3]}")
    print(f"전체 매장 수: {df.shape[0]}")

    # %%
    filename = 'hollys_branches.csv'
    df.to_csv(f'{filename}', encoding='utf-8', index=False)
    print(f"{filename} 파일 저장 완료")


if __name__ == '__main__':
    asyncio.run(main())
