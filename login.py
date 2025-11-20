import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import time

@pytest.fixture
def driver(request):
    # Создаем драйвер Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    time.sleep(5)
    driver.quit()

# АВТОРИЗАЦИЯ ПО НОМЕРУ ТЕЛЕФОНА
# Успешная авторизация с корректными номером телефона и паролем
def test_phone_positive(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём, пока кнопка "Войти" станет кликабельной
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )

    # Выбираем вкладку "Телефон"
    tab_input = driver.find_element(By.ID, "t-btn-tab-phone")
    tab_input.click()

    # Вводим корректные данные
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("+79231270217")  # <-- Корректный номер телефона
    password_input.send_keys("kraB4545")  # <-- Корректный пароль

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления элемента личного кабинета
    lk_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "a#logout, div.profile, h1, .header")
        )
    )

    # Проверяем, что элемент личного кабинета виден
    assert lk_element is not None




# Авторизация с незарегистрированным в системе номером телефона и существующим в системе паролем
def test_phone_wrong_phone(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём, пока кнопка "Войти" станет кликабельной
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )
    tab_input = driver.find_element(By.ID, "t-btn-tab-phone")
    # Кликаем "Войти"
    tab_input.click()

    # Вводим логин и пароль (вводим НЕкорректные данные)
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("+78000000000") # незарегистрированный в системе номер тлф
    password_input.send_keys("kraB4545") # существующий в системе пароль

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления ошибки о неправильном телефоне
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что текст ошибки содержит что-то
    assert "неверный" in error_message.text.lower()




# Авторизация с зарегистрированным в системе номером телефона и некорректным паролем
def test_phone_wrong_pssword(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём, пока кнопка "Войти" станет кликабельной
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )
    tab_input = driver.find_element(By.ID, "t-btn-tab-phone")
    # Кликаем "Войти"
    tab_input.click()

    # Вводим логин и пароль (вводим НЕкорректные данные)
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("+79231270217") # зарегистрированный в системе номер тлф
    password_input.send_keys("omaR4545") # некорректный пароль

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления ошибки о неправильном пароле
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что текст ошибки содержит что-то
    assert "неверный" in error_message.text.lower()




# Авторизация с пустыми полями телефона и пароля
def test_phone_empty_fields(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём кнопку "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )

    # Выбираем вкладку "Телефон"
    tab_input = driver.find_element(By.ID, "t-btn-tab-phone")
    tab_input.click()

    # Находим поля для ввода
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    # Очищаем поля, чтобы точно были пустые
    username_input.clear()
    password_input.clear()

    # Кликаем Войти без ввода данных
    login_button.click()

    # Ждём появления сообщения об ошибке
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что текст ошибки не пустой
    assert len(error_message.text) > 0

# АВТОРИЗАЦИЯ ПО ПОЧТЕ
# Авторизация по почте с корректными логином и паролем
def test_mail_positive(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём кнопку "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )

    # Выбираем вкладку "Почта"
    tab_input = driver.find_element(By.ID, "t-btn-tab-mail")
    tab_input.click()

    # Находим поля логина и пароля
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    # Вводим корректные данные
    username_input.send_keys("madinafakhrutdinova1@gmail.com")  # Корректный зарегистрированный email
    password_input.send_keys("kraB4545")  # Корректный пароль

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления элемента личного кабинета (видно только после успешного входа)
    lk_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "a#logout, div.profile, h1, .header")
        )
    )

    # Проверяем, что элемент личного кабинета виден
    assert lk_element is not None




# Авторизация с незарегистрированной в системе почтой и корректным паролем
def test_mail_wrong_mail(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём, пока кнопка "Войти" станет кликабельной
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )
    tab_input = driver.find_element(By.ID, "t-btn-tab-mail")
    # Кликаем "Войти"
    tab_input.click()

    # Вводим незарегистрированную почту и корректный пароль
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("madtreglietz@mail.ru") # незарегистрированная почта
    password_input.send_keys("kraB4545") # корректный пароль

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления ошибки о неправильной почте
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что текст ошибки содержит что-то
    assert "неверный" in error_message.text.lower()




# Авторизация с зарегистрированной в системе почтой и некорректным паролем
def test_mail_wrong_password(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём, пока кнопка "Войти" станет кликабельной
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )
    tab_input = driver.find_element(By.ID, "t-btn-tab-mail")
    # Кликаем "Войти"
    tab_input.click()

    # Вводим незарегистрированную почту и корректный пароль
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("madinafakhrutdinova1@gmail.com")  # зарегистрированная почта
    password_input.send_keys("omaR4545")  # НЕкорректный пароль

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления ошибки о неправильно пароле
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что текст ошибки содержит что-то
    assert "неверный" in error_message.text.lower()




# Авторизация по почте с пустыми полями почты и пароля
def test_mail_empty_fields(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём кнопку "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )

    # Выбираем вкладку "Почта"
    tab_input = driver.find_element(By.ID, "t-btn-tab-mail")
    tab_input.click()

    # Находим поля почты и пароля
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    # Очищаем поля, чтобы они точно были пустые
    username_input.clear()
    password_input.clear()

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления ошибки
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что текст ошибки не пустой
    assert len(error_message.text) > 0




# Авторизация по почте с корректным логином и некорректным длинным паролем (>12 символов)
def test_mail_wrong_long_password(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём кнопку "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )

    # Выбираем вкладку "Почта"
    tab_input = driver.find_element(By.ID, "t-btn-tab-mail")
    tab_input.click()

    # Находим поля почты и пароля
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    # Вводим корректную почту и длинный неверный пароль
    username_input.send_keys("madinafakhrutdinova1@gmail.com") # корректный логин
    password_input.send_keys("WrongSuperLongPass123!")  # <-- Некорректный длинный пароль

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления ошибки о неправильном пароле
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что текст ошибки содержит "неверный"
    assert "неверный" in error_message.text.lower()

    time.sleep(30) # для ввода капчи


    # АВТОРИЗАЦИЯ ПО ЛОГИНУ
    # Успешная авторизация с корректным логином и паролем
def test_login_success(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Находим поля ввода
    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    password_input = driver.find_element(By.ID, "password")

    # Вводим РЕАЛЬНЫЕ корректные данные
    username_input.send_keys("rtkid_1763606838542")
    password_input.send_keys("kraB4545")

    # Жмём "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )
    login_button.click()

    # Ожидаем перехода в личный кабинет – признак успешного входа
    # Обычно появляется имя пользователя, кнопка выхода или смена URL
    lk_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "a#logout, div.profile, h1, .header")
        )
    )

    assert lk_element is not None




    # Авторизация по логину с незарегистрированным в системе логином
def test_login_wrong_login(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём, пока кнопка "Войти" станет кликабельной
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )

    # Вводим НЕзарегистрированный логин и существующий в системе пароль
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("test_user")
    password_input.send_keys("kraB4545")

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления ошибки о неправильном логине
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что текст ошибки содержит что-то
    assert "неверный" in error_message.text.lower()




    # Авторизация по логину с корректным логином и неверным паролем
def test_login_wrong_password(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём, пока кнопка "Войти" станет кликабельной
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )

    # Вводим зарегистрированный логин и НЕправильный пароль
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("rtkid_1763606838542")   # Существующий логин
    password_input.send_keys("omaR4545")       # Неправильный пароль

    # Кликаем "Войти"
    login_button.click()

    # Ждём появления ошибки о неправильном пароле
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что текст ошибки действительно об ошибке
    assert "неверный" in error_message.text.lower()




    #Авторизация по логину с пустыми логином и паролем
def test_login_password_empty_fields(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём кнопку Войти
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-login"))
    )

    # Находим поля логина и пароля
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    # Очищаем, чтобы точно были пустые
    username_input.clear()
    password_input.clear()

    # Кликаем Войти без ввода данных
    login_button.click()

    # Ждём появления ошибки
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "form-error-message"))
    )

    # Проверяем, что нам сказали, что поля пустые или данные неверны
    assert len(error_message.text) > 0



# ПО УМОЛЧАНИЮ ВЫБРАНА ВКЛАДКА ТЕЛЕФОН
def test_default_tab_phone(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Ждём, пока вкладки загрузятся
    phone_tab = wait.until(
        EC.presence_of_element_located((By.ID, "t-btn-tab-phone"))
    )

    # Проверяем, что вкладка "Телефон" активна
    active_class = phone_tab.get_attribute("class")

    assert "rt-tab--active" in active_class, "По умолчанию не выбрана вкладка 'Телефон'"


