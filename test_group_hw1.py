"""Задания делать на сайте http://ts.red-promo.ru/
1 Сделать поиск со словом "Стейк". Проверить что в карточках присутствует слово «Стейк»"""
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path="driver\\chromedriver.exe")
# driver.get("http://ts.red-promo.ru/")
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@name='keyword']").send_keys("Стейк", Keys.ENTER)
# time.sleep(2)
# search_list = [i.text.lower() for i in driver.find_elements(By.XPATH, "//div[@class='pi-title fz-16 clr-text-alt m-b-10']")]
# if driver.find_element(By.XPATH, "//li[@class='next']"):
#     driver.find_element(By.XPATH, "//li[@class='next']").click()
#     search_list += [i.text.lower() for i in driver.find_elements(By.XPATH, "//div[@class='pi-title fz-16 clr-text-alt m-b-10']")]
# for i in search_list:
#     assert "стейк" in i
# driver.quit()

'''2 Проверить наличие этого свап контейнера'''
# driver = webdriver.Chrome(executable_path="driver\\chromedriver.exe")
# driver.get("http://ts.red-promo.ru/")
# time.sleep(1)
# try:
#     assert driver.find_element(By.XPATH, "//div[@class='slick-slider slider-visibility slick-initialized slick-dotted']")
#     print('found')
# except NoSuchElementException:
#     print('No elements found')
#
# driver.quit()


'''3 Написать разнообразные проверки на форму регистрации (для проверки сообщений о
правильности заполнении полей формы)'''
driver = webdriver.Chrome(executable_path="driver\\chromedriver.exe")
driver.get("http://ts.red-promo.ru/")
time.sleep(1)


'''4 Решить логическую задачку: Я кладу на стол 101 монету орлами вверх, и завязываю
вам глаза. Я переворачиваю случайные 30 монет решками вверх.
Ваша задача: разделить эти монеты на две части так, чтобы в одной части было столько
же решек сколько и в другой.'''
#разделить на две кучки в 30 и 71 монету. перевернуть все монеты в кучке с 30 штуками
