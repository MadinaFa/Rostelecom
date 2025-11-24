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



# Клик на кнопку "пользовательского соглашения" : Открывается страница "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
def test_user_agreement_link_opens_correct_page(driver):
    # Arrange
    driver.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(driver, 10)
    main_window = driver.current_window_handle

    # Act
    # Ожидаем и кликаем по ссылке "Пользовательское соглашение"
    agreement_link = wait.until(
        EC.element_to_be_clickable((By.ID, "rt-auth-agreement-link"))
    )
    agreement_link.click()

    # Ожидаем появления второй вкладки
    wait.until(lambda d: len(d.window_handles) > 1)

    # Переключаемся на новую вкладку
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    # Assert
    expected_url_prefix = "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
    assert driver.current_url.startswith(expected_url_prefix), \
        f"Ожидался URL, начинающийся с {expected_url_prefix}, но получен: {driver.current_url}"

    # Дополнительная проверка: убедимся, что страница содержит ключевой текст
    page_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Пользовательское соглашение" in page_text, \
        "На странице пользовательского соглашения не найден ожидаемый текст"




# Клик на кнопку "Помощь": найден элемент с заголовком "Ваш безопасный ключ к сервисам Ростелекома"
def test_help_button_opens_help_page(driver):
    driver.get("https://b2c.passport.rt.ru")

    # Ждём кнопку "Помощь"
    help_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "faq-open"))
    )

    # Кликаем
    help_button.click()

    # 🟡 ЖДЁМ ПОЯВЛЕНИЕ НОВОЙ ВКЛАДКИ
    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > 1
    )

    # Переключаемся на новую вкладку
    driver.switch_to.window(driver.window_handles[-1])

    # Ждём заголовок на странице
    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, "//*[contains(text(), 'Ваш безопасный ключ к сервисам Ростелекома')]"
        ))
    )

    assert header.is_displayed(), "Страница 'Помощь' не открылась или заголовок не найден"




#  Клик на кнопку "Зарегистрироваться" на форме авторизации + нажать на кнопку "Зарегистрироваться" в форме "Регистрация" :не заполнено поле "ИМЯ"
def test_registration_empty_firstname(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # 1. Переход на форму регистрации из авторизации
    register_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    register_btn.click()

    # Убеждаемся, что мы на форме регистрации
    wait.until(
        EC.presence_of_element_located((By.NAME, "lastName"))
    )

    # 2. НЕ заполняем поле "Имя"

    # 3. Заполняем остальные обязательные поля минимально корректно
    driver.find_element(By.NAME, "lastName").send_keys("Иванова")
    driver.find_element(By.NAME, "address").send_keys("test@example.com")
    driver.find_element(By.NAME, "password").send_keys("Test1234!")
    driver.find_element(By.NAME, "password-confirm").send_keys("Test1234!")

    # 4. Жмём Зарегистрироваться
    driver.find_element(By.ID, "kc-register").click()

    # 5. Ждём появления ошибки под полем "Имя"
    error = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(@class,'rt-input-container__meta--error') and text()='Введите имя']")
        )
    )

    assert error.is_displayed(), "Ошибка 'Введите имя' не отображается при пустом поле Имя"




#  Клик на кнопку "Зарегистрироваться" на форме авторизации + нажать на кнопку "Зарегистрироваться" в форме "Регистрация" : не заполнено поле "Фамилия"
def test_registration_empty_lastname(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # 1. Переход на форму регистрации из авторизации
    register_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    register_btn.click()

    # Убеждаемся, что мы на форме регистрации
    wait.until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    )

    # 2. НЕ заполняем поле "Фамилия"

    # 3. Заполняем остальные обязательные поля минимально корректно
    driver.find_element(By.NAME, "firstName").send_keys("Иван")
    driver.find_element(By.NAME, "address").send_keys("test@example.com")
    driver.find_element(By.NAME, "password").send_keys("Test1234!")
    driver.find_element(By.NAME, "password-confirm").send_keys("Test1234!")

    # 4. Жмём Зарегистрироваться
    driver.find_element(By.ID, "kc-register").click()

    # 5. Ждём появления ошибки под полем "Фамилия"
    error = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(@class,'rt-input-container__meta--error') and text()='Введите фамилию']")
        )
    )

    assert error.is_displayed(), "Ошибка 'Введите фамилию' не отображается при пустом поле Фамилия"




# #  Клик на кнопку "Зарегистрироваться" на форме авторизации + нажать на кнопку "Зарегистрироваться" в форме "Регистрация" : не заполнено поле "E-mail или мобильный телефон"
def test_registration_empty_email(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    # Переход на форму регистрации
    register_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    register_btn.click()

    # Убеждаемся, что форма загрузилась
    wait.until(EC.presence_of_element_located((By.NAME, "firstName")))

    # Заполняем остальные обязательные поля
    driver.find_element(By.NAME, "firstName").send_keys("Иван")
    driver.find_element(By.NAME, "lastName").send_keys("Иванов")
    driver.find_element(By.NAME, "password").send_keys("Test1234!")
    driver.find_element(By.NAME, "password-confirm").send_keys("Test1234!")

    # НЕ заполняем поле e-mail/телефон
    driver.find_element(By.ID, "kc-register").click()

    # Ждём появления ошибки
    error = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(@class,'rt-input-container__meta--error') and text()='Введите email или телефон']")
        )
    )

    assert error.is_displayed(), "Ошибка 'Введите email или телефон' не отображается при пустом поле"




# #  Клик на кнопку "Зарегистрироваться" на форме авторизации + нажать на кнопку "Зарегистрироваться" в форме "Регистрация" : не заполнено поле "Пароль"
def test_registration_empty_password(driver):
    driver.get("https://b2c.passport.rt.ru/")

    wait = WebDriverWait(driver, 10)

    register_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    register_btn.click()

    wait.until(EC.presence_of_element_located((By.NAME, "firstName")))

    driver.find_element(By.NAME, "firstName").send_keys("Иван")
    driver.find_element(By.NAME, "lastName").send_keys("Иванов")
    driver.find_element(By.NAME, "address").send_keys("test@example.com")
    driver.find_element(By.NAME, "password-confirm").send_keys("Test1234!")

    # НЕ заполняем поле пароль
    driver.find_element(By.ID, "kc-register").click()

    error = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(@class,'rt-input-container__meta--error') and text()='Введите пароль']")
        )
    )

    assert error.is_displayed(), "Ошибка 'Введите пароль' не отображается при пустом поле"