import time
from selenium import webdriver
from bs4 import BeautifulSoup
import collections
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable


options = webdriver.EdgeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)



driver = webdriver.Edge(options=options)
driver.get('https://www.coffeebeankorea.com/store/store.asp')


driver.execute_script("storePop2('334')")

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

store_name = soup.select('div.store_txt > p.name > span')
store_name_list = []
for name in store_name:
    store_name_list.append(name.get_text())

print("매장 갯수: ", len(store_name_list))
print(store_name_list)


store_Addresses = soup.select('p.addr > span')
store_Addresses_list = []
for addr in store_Addresses:
    print(addr.get_text())
    store_Addresses_list.append(addr.get_text())

driver.quit()