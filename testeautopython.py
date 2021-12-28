from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from TikTokApi import TikTokApi

name - input("Qual o nome do contato?")
api = TikTokApi.get_instance()
urls =[]
results = 1000
trending = api.by_trending(count=results, custom_verifyFp="verify_kxpgzzrt_BnZIdgOX_cGLs_42kY_Bebp_kagiiarzmRys")
for x in trending:
    aux = x['video']
    urls.append(aux['playAddr'])
options = webdriver.ChromeOptions()
options.add_argument('--profile-directory=Person 1')
options.add_argument('--user-data-dir=C:\\Users\\e.barbieri\\AppData\\Local\\Google\\Chrome\\User Data\\Person 1')
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
browser.maximize_window()
browser.get('https://web.whatsapp.com/')
WebDriverWait(browser, 22).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]')))
browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div[2]/div[1]').click() 
browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys('Luiz Henrique Barbeta')
WebDriverWait(browser, 22).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[10]/div/div/div[2]/div[1]')))
browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[10]/div/div/div[2]/div[1]').click()
WebDriverWait(browser, 22).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')))
browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').click()
for url in urls:
    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(url)   
    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
