from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://jqueryui.com/droppable/')
frame = driver.find_element(By.CLASS_NAME,'demo-frame')
driver.switch_to_frame(frame)
drag = driver.find_element(By.XPATH,"//div[@id='draggable']")
drop= driver.find_element(By.XPATH,"//div[@id='droppable']")
act = ActionChains(driver)
#act.drag_and_drop(drag,drop).perform()
act.click_and_hold(drag).move_to_element(drop).release().perform()