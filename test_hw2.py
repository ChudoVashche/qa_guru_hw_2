import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def size_browser():
    browser.open('https://google.com')
    browser.driver.set_window_size(720, 480)


def test_search(size_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_not_found(size_browser):
    browser.element('[name="q"]').should(be.blank).type('hsgfmdfdsgfhd').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Поиск не дал результатов')