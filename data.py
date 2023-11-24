class URLS:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/order'
    DZEN_URL = "https://dzen.ru/?yredirect=true"
    BLANK_URL = "about:blank"


class MainPageData:

    # Заголовок Главной страницы
    TITLE_TEXT = 'Самокат\nна пару дней'

    # Блок Вопросы о важном на Главной странице
    QUESTIONS_AND_ANSWERS_LIST = [
        (1, 'Сколько это стоит? И как оплатить?',
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (2, 'Хочу сразу несколько самокатов! Так можно?',
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
            'можете просто сделать несколько заказов — один за другим.'),
        (3, 'Как рассчитывается время аренды?',
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
            'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
            'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (4, 'Можно ли заказать самокат прямо на сегодня?',
            'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (5, 'Можно ли продлить заказ или вернуть самокат раньше?',
            'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (6, 'Вы привозите зарядку вместе с самокатом?',
            'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — '
            'даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (7, 'Можно ли отменить заказ?',
            'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (8, 'Я жизу за МКАДом, привезёте?',
            'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]


class OrderPageData:

    # Страница заказа - Для кого самокат
    USER_1 = {
        'first_name': 'Иван',
        'last_name': 'Иванов',
        'address': 'Русаковская улица, 22',
        'station': 'Сокольники',
        'tel_number': '+79999999999',
        'station_index': 4                       # индекс станции Сокольники в списке
    }

    USER_2 = {
        'first_name': 'Сергей',
        'last_name': 'Петров',
        'address': 'Фрунзенская набережная, 4',
        'station': 'Фрунзенская',
        'tel_number': '+79876543210',
        'station_index': 14                       # индекс станции Фрунзенская в списке
    }

    # Страница заказа - Про аренду
    ORDER_1 = {
        'delivery_date': '01.12.2023',          # Когда привезти самокат
        'rent_days': 1,                         # Срок аренды - 1 сутки (от 1 до 7)
        'black': True,                          # Выбрать черный цвет
        'grey': False,                          # Не выбирать серый цвет
        'comment': 'Позвоните за полчаса',      # Комментарий для курьера
        'rent_text': 'сутки'                    # Текст в поле срок аренды после выбора
    }

    ORDER_2 = {
        'delivery_date': '31.12.2023',          # Когда привезти самокат - дата по умолчанию (сегодня)
        'rent_days': 2,                         # Срок аренды - 2 суток (от 1 до 7)
        'black': False,                         # Не выбирать черный цвет
        'grey': True,                           # Выбрать серый цвет
        'comment': '',                          # Комментарий для курьера
        'rent_text': 'двое суток'                    # Текст в поле срок аренды после выбора
    }

    # Заголовок окна оформления заказа
    FORM1_TITLE_TEXT = 'Для кого самокат'

    # Заголовок окна подтверждения после оформления заказа
    ORDER_CONFIRM_TITLE_TEXT = 'Заказ оформлен'

