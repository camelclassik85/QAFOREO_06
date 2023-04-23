import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url
    driver.implicitly_wait(10)


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_fill_search_field(driver):
    driver.get('https://openweathermap.org/')
    search_field_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_field_field.send_keys('New York')
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']").click()
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1)>span:nth-child(1)").click()
    driver.implicitly_wait(2)
    displayed_city_text = driver.find_element(By.CSS_SELECTOR, ".grid-container.grid-4-5 h2").text
    expected_city = 'New York City, US'
    assert expected_city == displayed_city_text


def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    expected_city = 'New York City, US'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city

