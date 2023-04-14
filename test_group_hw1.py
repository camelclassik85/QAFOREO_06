import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def open_page():
    driver.get("http://ts.red-promo.ru/")
    time.sleep(1)


"""Задания делать на сайте http://ts.red-promo.ru/
1 Сделать поиск со словом "Стейк". Проверить что в карточках присутствует слово «Стейк»"""

def test_staik_is_present():
    open_page()
    driver.find_element(By.XPATH, "//input[@name='keyword']").send_keys("Стейк", Keys.ENTER)
    time.sleep(2)
    search_list = [i.text.lower() for i in
                   driver.find_elements(By.XPATH, "//div[@class='pi-title fz-16 clr-text-alt m-b-10']")]
    if driver.find_element(By.XPATH, "//li[@class='next']"):
        driver.find_element(By.XPATH, "//li[@class='next']").click()
        search_list += [i.text.lower() for i in
                        driver.find_elements(By.XPATH, "//div[@class='pi-title fz-16 clr-text-alt m-b-10']")]
    for j, i in enumerate(search_list):
        assert "стейк" in i, f"element {j + 1} do not have стейк in"

    driver.quit()

'''2 Проверить наличие этого свап контейнера'''


def test_swap_container_is_presents():
    open_page()
    assert driver.find_element(By.XPATH,
                               "//div[@class='slick-slider slider-visibility slick-initialized slick-dotted']")
    driver.quit()


'''3 Написать разнообразные проверки на форму регистрации (для проверки сообщений о
правильности заполнении полей формы)'''


def test_empty_fields_alert_text_correct():
    open_page()
    driver.find_element(By.XPATH, "(//span[@class='sci-amount'])[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "(//a[@data-toggle='modal-alt'])[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@class='btn btn-default signup-form-modal__btn w-100']").click()
    time.sleep(1)
    text_name_exp = 'Необходимо заполнить «Имя пользователя».'
    text_name_fact = driver.find_element(By.XPATH, "//div[@class='form-group field-signupform-username required "
                                                   "has-error']/div").text
    text_email_exp = 'Необходимо заполнить «Email».'
    text_email_fact = driver.find_element(By.XPATH, "//div[@class='form-group field-signupform-email required "
                                                    "has-error']/div").text
    text_password_exp = 'Необходимо заполнить «Пароль».'
    text_password_fact = driver.find_element(By.XPATH, "//div[@class='form-group field-signupform-password required "
                                                       "has-error']/div/div[@class='help-block']").text
    text_repeat_password_exp = 'Необходимо заполнить «Повторите пароль».'
    text_repeat_password_fact = driver.find_element(By.XPATH, "//div[@class='form-group field-signupform-repeat_password "
                                                              "required has-error']/div/div[@class='help-block']").text
    assert text_name_fact == text_name_exp, f'неправильный текст для не введенного имя пользователя'
    assert text_email_fact == text_email_exp, f'неправильный текст для не введенного email'
    assert text_password_fact == text_password_exp, f'неправильный текст для не введенного пароля'
    assert text_repeat_password_fact == text_repeat_password_exp, f'неправильный текст для не введенного повторного пароля'
    driver.quit()

'''4 Решить логическую задачку: Я кладу на стол 101 монету орлами вверх, и завязываю
вам глаза. Я переворачиваю случайные 30 монет решками вверх.
Ваша задача: разделить эти монеты на две части так, чтобы в одной части было столько
же решек сколько и в другой.'''
# разделить на две кучки в 30 и 71 монету. перевернуть все монеты в кучке с 30 штуками
