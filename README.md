# OTUS Algorithms

### Домашние задания по курсу "Алгоритмы и структуры данных"

RUN  `python main.py`

`homework_num` - номер домашнего задания

Пример:

    homeworks = [
        ('0.String', LenSolution),
        ('1.Tickets', FastSolution),
    ]

    homework_num = 0
    CheckHomework(homework=homeworks[homework_num]).run(show_results=True)

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