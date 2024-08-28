# Домашняя работа по уроку "Пространство имен."

# Объявление функции test_function()
def test_function():
    # Объявление функции inner_function() внутри функции test_function()
    def inner_function():
        # вывод на консоль функции inner_function() (не видится)
        print('Я в области видимости функции test_function')

    # обращение к функции inner_function() из функции test_function()
    inner_function()
    # вывод на консоль результата функции inner_function(), на консоли не отобразится,
    # функция inner_function() находится в локальном пространстве test_function()
    # print(inner_function())


# вызов функции inner_function() вне функции test_function() вызывает ошибку неопределенного имени
# inner_function() видится только внутри пространства test_function() и ее результат будет виден только
# когда будет обращение к test_function()

# inner_function()

# вызов функции test_function() приводит к выводу на консоль результата inner_function() и этот результат
# вивден в глобальном пространстве и к этому выводится результат работы обеих функции (если раскомментировать
# print(inner_function()) в функции test_function(), то на консоль выводится результат работы этой функции)
test_function()
