# OTUS Algorithms

### Домашние задания по курсу "Алгоритмы и структуры данных"

Для автоматической проверки домашних заданий необходимо 
запустить файл `homeworks/main.py`
указав номер домашнего задания в `homework_num`.

Пример:

    homeworks = [
        ('0.String', LenSolution),
        ('1.Tickets', FastSolution),
    ]
    CheckHomework.set_homeworks(homeworks)

    homework_num = 0
    CheckHomework(num=homework_num).run()

Результат:

```
0.String result:
test.0.in:          OK                  0.0                              8 = 8
test.1.in:          OK                  0.0                             64 = 64
test.2.in:          OK                  0.0                              0 = 0
test.3.in:          OK                  0.0                              1 = 1
test.4.in:         NOK                  0.0                             25 = 26
```
,где 

`test.0.in` - номер теста; \
`OK\NOK` - результат; \
`0.0` - время выполнения в мс; \
`8 = 8` - сравнения результата с ожидаемым; \

в переменную `homeworks` выкладываются решения.