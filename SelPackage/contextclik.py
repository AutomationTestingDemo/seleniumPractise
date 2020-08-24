from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
# driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
# rightclick = driver.find_element(By.XPATH,"//span[text()='right click me']")
# act = ActionChains(driver)
# act.context_click(rightclick).perform()
# options = driver.find_elements(By.CSS_SELECTOR,"li.context-menu-icon span")
# print(len(options))
# for l in options:
#     if l.text !='Quit':
#         l.click()
#         print(driver.switch_to.alert.text)
#         driver.switch_to.alert.accept()
#         act.context_click(rightclick).perform()
#     else:
#         l.click()
#         driver.switch_to.alert.accept()
#         break


#alerts concept


driver.get('http://the-internet.herokuapp.com/javascript_alerts')
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
driver.switch_to.alert.send_keys('Kalyan')
driver.switch_to.alert.accept()
driver.switch_to.default_content()
print(driver.find_element(By.ID,'result').text)
# driver.get('https://classic.crmpro.com/')
# username = driver.find_element(By.NAME,'username')
# actions = ActionChains(driver)
# actions.click(on_element=username)
# actions.send_keys_to_element(username,'Kalyan')