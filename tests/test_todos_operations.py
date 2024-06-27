from selene import browser as selene_browser, have, be, query, command


def test_complete_todo():
    selene_browser.open('/')
    selene_browser.element('#new-todo').should(be.blank)

    selene_browser.element('#new-todo').type('a').press_enter()
    # selene_browser.element('#new-todo').perform(command.select_all)
    selene_browser.element('#new-todo').type('b').press_enter()
    selene_browser.element('#new-todo').type('c').press_enter()
    # selene_browser.all('#todo-list>li').with_(
    #     timeout=selene_browser.config.timeout * 2,
    # ).should(have.size(3))

    # selene_browser.all('#todo-list>li').should(have.size(3))
    #
    # selene_browser.all('#todo-list>li').first.should(have.exact_text('a'))
    # selene_browser.all('#todo-list>li').second.should(have.exact_text('a'))
    # selene_browser.all('#todo-list>li')[3].should(have.exact_text('a'))

    selene_browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
    # selene_browser.all('#todo-list>li').second.element('.toggle').click()
    selene_browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()
    selene_browser.all('#todo-list>li').by(have.css_class('completed')).should(have.exact_texts('b'))
    selene_browser.all('#todo-list>li').by(have.no.css_class('completed')).should(have.exact_texts('a','b'))




    '''
    # It's more about meeting some conditions
    browser.all('#todo-list>li').should(have.size(3))
    # It's more about waiting for something to be completed
    browser.all('#todo-list>li').wait.for_(have.size(3))
    '''

    '''
    # if we want to use selenium.webdriver. But this commands won't be effective for slow browsers.
    # They can't wait in comparison with "should" in selene
    # The first way -->
    from selene import by
    assert browser.driver.find_elements(*by.css('#todo-list>li')).__len__ == 3
    # The second way
    from selenium.webdriver.common.by import By
    assert browser.driver.find_elements(By.CSS_SELECTOR, '#todo-list>li').__len__ == 3
    # If we want let the 'selenium.webdriver' wait the request execution , we should use the following options:
    from selenium.webdriver.support.wait import WebDriverWait
    WebDriverWait(driver=browser.driver, timeout=3.0).until(
        lambda driver: driver.find_elements(By.CSS_SELECTOR, '#todo-list>li').__len__
        == 3
    )
    '''


from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_complete_todo_1(driver, browser):
    driver.get('https://todomvc-emberjs-app.autotest.how')
    assert (
            driver.find_element(By.CSS_SELECTOR, '#new-todo').get_attribute('value') == ''
    )

    # the same in selene: assert browser.element('#new-todo').get(query.attribute('value')) == ''
    # or: browser.element('#new-todo').should(have.attribute('value').value(''))
    # or: browser.element('#new-todo').should(be.blank)

    # browser.element('#new-todo').locate() is the same as : driver.find_element(By.CSS_SELECTOR, '#new-todo')

    driver.find_element(By.CSS_SELECTOR, '#new-todo').send_keys('a' + Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, '#new-todo').send_keys('a' + Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, '#new-todo').send_keys('a' + Keys.ENTER)
