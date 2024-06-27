В selene не все команды доступны на element, как в selenium.webdriver или в других фреймворках.
Например, uploadfile, draganddrop... и т.п. Это сделано специально.
Они вынесены отдельно.
Полный список команд 

from selene import browser, have, be, query, command

query - набор дополнительных запросов из selenium.webdriver для selene
command - набор дополнительных команд, которые можно выполнять

browser.element('#new-todo').get(query.attribute('value'))
selene_browser.element('#new-todo').perform(command.select_all)


Если по какой-то причине не работает browser.element('#save'').click(), например, на кнопке 'save', есть возможность это сделать с помощью JS:
browser.element('#save'').perform(command.js.click)
Они вынесены отдельно, так как это все же костыль. И желательно, чтобы разработчик старался избегать из использования. Но иногда, при отсутвии иного выхода, это вполне нормальный вариант.

Зачастую автоматизаторы введение текста делают с помощью JS, так как это быстрее, чем когда selene или selenium используют type('smth...'), так как в данном случае ввод происходит по 1 символу.

В selene это можно сделать:
selene_browser.config.type_by_js = True
И все type() будут вводиться разом без симуляции пользователя (по 1 символу).

Так же есть, чтобы все клики были через JS.
selene_browser.config.click_by_js = True
Но это реже используется.

Также через команду with_ можно локально для отдельных случаев переопределять эти вещи, если нас не интересует, чтобы все глобально выполнялось через JS.
browser.element('#save'').with_(click_by_js=True).click()
Данный вариант удобнее, чем через perform. Так как в случае perform, если нужно сделать много кликов, необходимо будет дублировать код каждый раз.
А в случая with_ можно просто сохранить элемент в переменную и потом вызывать:
save = browser.element('#save').with_(click_by_js=True)
save.click()
save.click()
save.click()
save.click()
save.click()
save.click()
...
Так как в данном случае на конкретном элементе мы настроили опцию click_by_js и теперь все клики выполняются таким образом.

Для добавления собственных команд можно провалиться в какую-то команду, например, select_all, и по шаблону можно попробовать реализоовать что0то свое.


Команды, которые начинаются с подчеркивания, они "приватные" ("экспериментальные"). И если их использовать, то есть шанс, что они пропадут/переименуются и тест перестанет работать.

ActionChains (из selenium.webdriver) для реализации цепочки команд (см. _long_press, double_click)


Как работать с коллекциями

selene_browser.all('#todo-list>li').should(have.size(3))
selene_browser.all('#todo-list>li').first.should(have.exact_text('a'))
selene_browser.all('#todo-list>li').second.should(have.exact_text('b'))
selene_browser.all('#todo-list>li')[2].should(have.exact_text('c'))

Все четыре строки можно записать как одну:
selene_browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

Она проверяет, что в коллекции all именно 3 элемента, которые расположены именно в таком порядке и именно с такими текстами, как указано в скобках.

Элементы можно выбирать по номеру, по условию.
selene_browser.all('#todo-list>li').second.element('.toggle').click()
selene_browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()

Второй вариант лучше, чем первый, так как лучше симулирует то, что делает пользователь. Но находит только 1 элемент. Если нужно найти все элементы, соответствующие условию:
selene_browser.all('#todo-list>li').by(have.css_class('completed'))


