# Housing_Market
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy, lightgbm
API: flask
Данные: с kaggle - https://www.kaggle.com/c/sberbank-russian-housing-market

Задача: предсказать стоимость жилья

Используемые признаки находятся в файле data_dictionary


Модель: lightgbm

### Клонируем репозиторий и создаем образ
```
$ git clone git clone https://github.com/Alex-Zhukov/Housing_Market.git
$ cd  Housing_Market
$ docker build -t alex-zhukov/housing_market .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -v <your_local_path_to_pretrained_models>:/app/app/models alex-zhukov/housing_market 
```

#### Данные для тестов находятся в папке for test
#### Обученная модель в папке app/models
