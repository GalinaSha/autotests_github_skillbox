import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from autotests_githab_skillbox.src.actions.forms import title_bug, search_author, stars, courses


@allure.feature('Проверки сайта гитхаб')
@allure.story('Тест-сьют содержит проверки из модуля № 5 на сайт гитхаб и один кейс на скилбокс')
class TestGithub:
    @allure.title('Проверка задач со словом "bug"')
    def test_title(self, selenium):

        with allure.step('Открытие страницы https://github.com/microsoft/vscode/issues'):
            selenium.get("https://github.com/microsoft/vscode/issues")
        title_bug(selenium)

        with allure.step('Проверка, что каждая задача содержит слово "bug"'):
            issue_titles = selenium.find_elements(By.CSS_SELECTOR, "a[data-hovercard-type='issue']")
            for title in issue_titles:
                assert "bug" in title.text.lower()

    @allure.title('Проверка авторства задач')
    def test_author(self, selenium):
        with allure.step('Открытие страницы https://github.com/microsoft/vscode/issues'):
            selenium.get("https://github.com/microsoft/vscode/issues")
        search_author(selenium)

        # Получаем все задачи и проверяем авторство
        with allure.step('Проверка, что во всех задачах автор "bpasero"'):
            authors = selenium.find_elements(By.CSS_SELECTOR, "div.hx_Box--firstRowRounded0  a[title*='bpasero']")
            for author in authors:
                assert author.text.lower() == "bpasero"

    @allure.title('Проверка количества звезд у каждого репозитория')
    def test_stars(self, selenium):
        with allure.step('Открытие страницы https://github.com/search/advanced'):
            selenium.get("https://github.com/search/advanced")
        stars(selenium)

        with allure.step('Проверка, что у каждого репозитория >20000 звезд'):
            repos = selenium.find_elements(By.CSS_SELECTOR, "h3 a")
            for repo in repos:
                selenium.get(repo.get_attribute("href"))
                star_count = selenium.find_element(By.CSS_SELECTOR, ".social-count.js-social-count").text
                star_count = int(star_count.replace(",", ""))
                assert star_count > 20000

    @allure.title('Проверка тултипа графика')
    def test_graph(self, selenium):
        with allure.step('Открытие страницы https://github.com/microsoft/vscode/graphs/commit-activity'):
            selenium.get("https://github.com/microsoft/vscode/graphs/commit-activity")

        with allure.step('Наведение мышки на первый элемент графика'):
            action_chains = webdriver.ActionChains(selenium)
            action_chains \
                .move_to_element(selenium.find_element(By.CSS_SELECTOR, "g.bar.mini")) \
                .perform()

        with allure.step('Проверка текста в тултипе графика'):
            # Получаем текст из тултипа по первому элементу
            tooltip_text = selenium.find_element(By.CLASS_NAME, "svg-tip").text
            # Проверяем, что текст соответствует ожидаемому значению
            assert tooltip_text == "140 commits the week of May 15"
