# Test
## Тестовое задание в паттерне Page Object Model


Структура директорий

├── README.md
├── pages
│   ├── __init__.py
│   ├── base_page.py
│   ├── book_page.py
│   ├── locators.py
│   └── main_page.py
├── __init__.py
├── conftest.py
├── requirements.txt
└── test_main_page.py


Комманды для запуска тестов: 
По умолчанию запуск тестов производится в браузере Google Chrome

1  Стандартная комманда: pytest test___.py
2  Для запуска тестов в браузере Firefox: pytest -s -v --browser_name=firefox test___.py
