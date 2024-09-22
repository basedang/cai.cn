from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

internet = Chrome()
time.sleep(3)
internet.get("https://data.cfi.cn/data_ndkA0A1934A1935A5015.html")

time.sleep(2)
tab_top=internet.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/table/tbody/tr[2]/td/div/table/thead/tr")

with open(r"A:a.txt","w",encoding='utf-8',errors="ignore")as a:
   txt=a.write(str(tab_top[0].text))
   time.sleep(2)

for i in range(103):
    tab_mian=internet.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/table/tbody/tr[2]/td/div/table/tbody")
    time.sleep(1)
    with open(r"A:a.txt","a",encoding='utf-8',errors="ignore")as b:
        txt=b.write("\n")
        txt=b.write(str(tab_mian[0].text))
        
    time.sleep(2)
    a_page=internet.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/table/tbody/tr[1]/td/div[4]/a[103]").click()
    time.sleep(2)


time.sleep(10)
internet.quit()