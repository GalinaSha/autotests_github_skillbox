import logging
import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def title_bug(selenium):
    logging.info('Ввод значений в поле поиска')

    # Находим поле поиска и вводим значения
    with allure.step('Ввод в поле поиска "in:title bug"'):
        search_input = selenium.find_element(By.ID, "js-issues-search")
        search_input.send_keys("in:title bug" + Keys.ENTER)

    logging.info('Ожидание результатов поиска')


def search_author(selenium):
    logging.info('Ввод значений в поле поиска')

    # Находим кнопку Автор кликаем и вводим значения
    with allure.step('Ввод в поле поиска по автору "bpasero"'):
        selenium.find_element(By.XPATH, "//summary[@title='Author']").click()
        selenium.find_element(By.ID, "author-filter-field").send_keys("bpasero")
        selenium.find_element(By.XPATH, "//button[@name='author']").click()

    logging.info('Ожидание результатов поиска')


def stars(selenium):
    logging.info('Ввод значений в поля формы')

    with allure.step('Заполнение формы'):
        with allure.step('Выбор языка "Python"'):
            selenium.find_element(By.ID, "search_language").click()
            selenium.find_element(By.XPATH, "//option[@value='Python'][1]").click()
        with allure.step('Ввод количества звезд ">20000"'):
            selenium.find_element(By.ID, "search_stars").send_keys(">20000")
        with allure.step('Ввод названия файла "environment.yml"'):
            selenium.find_element(By.ID, "search_filename").send_keys("environment.yml")
            selenium.find_element(By.CSS_SELECTOR, "div.form-group>div>button.btn").click()

    logging.info('Ожидание результатов поиска')


def courses(selenium):
    logging.info('Ввод значений в поля формы')

    with allure.step('Заполнение формы'):
        with allure.step('Выбор типа обучения «Профессия»'):
            selenium.find_element(By.CSS_SELECTOR, "input[value='profession'] + span").click()
        with allure.step('Указание длительности обучения от 6 до 12 месяцев'):
            duration1 = selenium.find_element(By.CSS_SELECTOR, "div[aria-valuetext='1']>button")
            action_chains = webdriver.ActionChains(selenium)
            action_chains \
                .click_and_hold(duration1) \
                .move_by_offset(xoffset=40, yoffset=0) \
                .perform()
            action_chains.release().perform()  # чтобы отпустить мышку

            duration2 = selenium.find_element(By.CSS_SELECTOR, "div[aria-valuetext='24']>button")
            action_chains = webdriver.ActionChains(selenium)
            action_chains \
                .click_and_hold(duration2) \
                .move_by_offset(xoffset=-40, yoffset=0) \
                .perform()
            action_chains.release().perform()  # чтобы отпустить мышку
        with allure.step('Выбор тематики "Backend-разработка"'):
            selenium.find_element(By.XPATH, "//span[contains(text(), 'Backend-разработка')]").click()

    logging.info('Ожидание результатов поиска')
