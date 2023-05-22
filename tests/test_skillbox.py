import allure
from selenium.webdriver.common.by import By
from autotests_githab_skillbox.src.actions.forms import courses


@allure.title('Проверка вывода курсов по длительности и заголовку')
def test_courses(self, selenium):
    with allure.step('Открытие страницы https://skillbox.ru/code/'):
        selenium.get("https://skillbox.ru/code/")
    courses(selenium)

    with allure.step(
            'Проверка, что все курсы: от 6 до 12 месяцев, профессия и в каждом заголовке есть слово "разработчик"'):
        course_list = selenium.find_elements(By.CLASS_NAME, "ui-product-card")
        for course in course_list:
            # если не добавить эту строку, то падает с ошибкой stale element reference
            course = selenium.find_element(By.CLASS_NAME, "ui-product-card")

            duration = course.find_element(By.CLASS_NAME, "card__count").text
            duration_num = int(duration)
            assert 6 <= duration_num <= 12
            assert any(word in course.find_element(By.CLASS_NAME, "ui-product-card-main__title").text.lower()
                       for word in ["разработчик", "developer"])
            assert "профессия" in course.find_element(By.CSS_SELECTOR,
                                                      "span.ui-product-card-main__label").text.lower()