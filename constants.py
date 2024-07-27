class Links:
    team_table = "https://docs.google.com/spreadsheets/d/1Gcs1f7JCxEGLhlPgex6oHdYYWZ0c9aDpWigDJYK1YAc/edit#gid=0"
    team_promo = "https://docs.google.com/presentation/d/1HwX4cHJrDhyokuUSyL_B1SD0sI3O2Jp0R9zU4trcavs/edit?usp=sharing"
    almanah = "https://drive.google.com/file/d/18b1lf58Is1LBp0E-o8uL_sV4fNIAEaTa/view?usp=drive_link"
    food_db = "https://docs.google.com/spreadsheets/d/10fcI7laF59V2pJkqzuxudaZK7ilFTTck8Ra5_RTLKL0/edit#gid=0"
    stickerpack = "https://t.me/addstickers/ShineBLD"
    vk_public = "https://vk.com/siyanieteam"
    photos = "https://vk.com/albums-215518590"


class TextTemplates:
    template_for_mailing = "Привет, Сияющий! \n\nТебе сообщение от @{author} \n {message}"
    message_before_auth = ("Привет, сияющий✨\n\n"
                           "Добро пожаловать в бот мероприятий ОПГ Сияния\n\n"
                           "Данный бот нужен для того, чтобы ты вовремя узнавал обо всех играх и встречах Сияющих, будь то кино, путешествие или что-то ещё 🔥\n\n"
                           "Обещаем в этом боте слать сообщения только по делу 🦀\n\n"
                           "Давай же познакомимся!\n\n"
                           "Нажми на кнопку 'Авторизоваться' ниже, чтобы начать использовать бота")
    message_after_auth = ("Приятно познакомиться :)\n\n В нашем боте есть еще одна замечательная функция, "
                          "помимо оповещений. \n Это меню! \nЧтобы изучить его возможности - "
                          "нажми кнопки внизу бота \n\nДо встречи👋")
    message_already_auth = "Оказывается, мы уже знакомы! Давай продолжим совместную работу!"

    message_games_table = (f"📌 Таблица всея команды: \n"
                           f"[Тык сюда]({Links.team_table}) \n\n"
                           "Здесь располагаются список команды, все актуальные игры и свободные места на них")

    message_team_promo = (f"📌 Презентация Сияния:\n"
                          f"[Тык сюда]({Links.team_promo})\n\n"
                          "Тут вся информация о нас собрана в одном месте: здесь и ссылка на таблицу, и на альманах, и вообще лучше подземелья")

    message_useful_links = (f"📌 Таблица всея команды:\n[Тык сюда]({Links.team_table})\n\n"
                            f"📌 Презентация Сияния:\n[Тык сюда]({Links.team_promo})\n\n"
                            f"📌 Альманах:\n[Тык сюда]({Links.almanah})\n\n"
                            f"📌 База едален:\n[Тык сюда]({Links.food_db})\n\n"
                            f"📌 Стикерпак Сияния:\n[Тык сюда]({Links.stickerpack})\n\n"
                            f"📌 Наша группа ВК:\n[Тык сюда]({Links.vk_public})\n\n"
                            f"📌 Фото Сияния:\n[Тык сюда]({Links.photos})\n\n"
                            f"❓Есть вопрос, идеи для улучшения команды \- пиши @Narp13 или @KatherinaPolezhaeva")

    message_food = (f"📌 База едален:\n[Тык сюда]({Links.food_db})\n\n"
                    f"Списочек местечек с едой и напитками, которые были рекомендованы Сияющими")

    message_notifications_off_confirm = "Ты хочешь описаться от оповещений о мероприятиях и играх Сияния? 😢"

    notifications_disabled = ("Очень жаль, но этому явно есть причина. Мы все понимаем 🙏\n\n"
                                      "Напомним, что меню для тебя все еще активно, а также есть функция 'Включить рассылку о мероприятиях' в меню бота\n\n"
                                      " До встречи 👋")
    notifications_not_disabled = "Тогда все в порядке 😉 \n\nКак только будет новая запись, тебе придет оповещение 🍀"

    notifications_already_disabled = ("Упс 🦀\n\n"
                                      "Ты уже отписан от оповещений Сияния\n\n"
                                      "Если захочешь вернуть их, ты можешь сделать это в меню✨")

    notifications_already_enabled = "Сияющий, ты уже подписан на рассылку от нашего бота\nКак только будет новая запись, тебе придет оповещение 🍀"

    notifications_enabled = "Готово! \n\nТеперь тебе снова будут приходить уведомления об играх и мероприятиях команды☺️"

    send_answer_to = "❗️❗️❗️\nСияющий, важно\n\nПока наш бот не умеет записывать людей на игры, поэтому, чтобы записать на игру, напиши об этом @Narp13 или @KatherinaPolezhaeva, указав игру и дату"


