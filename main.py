import pymysql

try:  # подключение к бд
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        charset="utf8",
        database="xdv",
    )


    def show_all():  # все вина
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM `wine`;")
                rows_0 = cursor.fetchall()
                for row_0 in rows_0:
                    print("_" * 100)
                    winery_show_0 = f" Винодельня: {row_0[0]} \n"
                    name_show_0 = f"Название: {row_0[1]} \n"
                    color_show_0 = f"Цвет вина: {row_0[2]} \n"
                    place_show_0 = f"Место хранения: {row_0[3]} \n"
                    tYpe_show_0 = f"Открыто/закрыто/закончено вино: {row_0[4]} \n"
                    amount_show_0 = f"Количество: {row_0[5]} \n"
                    wine_map_0 = f"Наличие в винной карте: {row_0[7]}"
                    print(winery_show_0, name_show_0, color_show_0, place_show_0, tYpe_show_0, amount_show_0, wine_map_0)

        finally:  # закрываем подключение
            connection.close()


    def inserting():  # ввод вина в бд
        try:

            with connection.cursor() as cursor:
                winery = input("Название винодельни: ")
                name = input("Название вина: ")
                color = input("Цвет вина: ")
                place = input("Место хранения: ")
                tYpe = input("Открыто/закрыто: ")
                amount = int(input("Количество: "))
                glass = amount * 6
                wine_map = input("Есть ли в винной карте: ")
                cursor.execute(
                    f"INSERT INTO `wine` (winery, name, color, place, type, amount, glass, wine_map) VALUES ('{winery}', '{name}', '{color}', '{place}', '{tYpe}', '{amount}', '{glass}', '{wine_map}');")
                connection.commit()

        finally:  # закрываем подключение
            connection.close()


    def show_winery():  # поиск по винодельне
        try:
            with connection.cursor() as cursor:
                wine_input = input("Введите название винодельни для показа всех вин: ")
                cursor.execute(f"SELECT * FROM `wine` WHERE winery = '{wine_input}';")
                rows_1 = cursor.fetchall()
                for row_1 in rows_1:
                    print("_" * 100)
                    winery_show_1 = f" Винодельня: {row_1[0]} \n"
                    name_show_1 = f"Название: {row_1[1]} \n"
                    color_show_1 = f"Цвет вина: {row_1[2]} \n"
                    place_show_1 = f"Место хранения: {row_1[3]} \n"
                    tYpe_show_1 = f"Открыто/закрыто/закончено вино: {row_1[4]} \n"
                    amount_show_1 = f"Количество: {row_1[5]} \n"
                    wine_map_1 = f"Наличие в винной карте: {row_1[7]}"
                    print(winery_show_1, name_show_1, color_show_1, place_show_1, tYpe_show_1, amount_show_1, wine_map_1)

        finally:  # закрываем подключение
            connection.close()


    def show_name():  # поиск по названию
        try:
            with connection.cursor() as cursor:
                name_input = input("Введите название для показа всех вин: ")
                cursor.execute(f"SELECT * FROM `wine` WHERE name = '{name_input}';")
                rows_2 = cursor.fetchall()
                for row_2 in rows_2:
                    print("_" * 100)
                    winery_show_2 = f" Винодельня: {row_2[0]} \n"
                    name_show_2 = f"Название: {row_2[1]} \n"
                    color_show_2 = f"Цвет вина: {row_2[2]} \n"
                    place_show_2 = f"Место хранения: {row_2[3]} \n"
                    tYpe_show_2 = f"Открыто/закрыто/закончено вино: {row_2[4]} \n"
                    amount_show_2 = f"Количество: {row_2[5]} \n"
                    wine_map_2 = f"Наличие в винной карте: {row_2[7]}"
                    print(winery_show_2, name_show_2, color_show_2, place_show_2, tYpe_show_2, amount_show_2, wine_map_2)

        finally:  # закрываем подключение
            connection.close()


    def show_place():  # поиск по месту
        try:
            with connection.cursor() as cursor:
                place_input = input("Введите название места хранения для показа всех вин: ")
                cursor.execute(f"SELECT * FROM `wine` WHERE place = '{place_input}';")
                rows_3 = cursor.fetchall()
                for row_3 in rows_3:
                    print("_" * 100)
                    winery_show_3 = f" Винодельня: {row_3[0]} \n"
                    name_show_3 = f"Название: {row_3[1]} \n"
                    color_show_3 = f"Цвет вина: {row_3[2]} \n"
                    place_show_3 = f"Место хранения: {row_3[3]} \n"
                    tYpe_show_3 = f"Открыто/закрыто/закончено вино: {row_3[4]} \n"
                    amount_show_3 = f"Количество: {row_3[5]} \n"
                    wine_map_3 = f"Наличие в винной карте: {row_3[7]}"
                    print(winery_show_3, name_show_3, color_show_3, place_show_3, tYpe_show_3, amount_show_3, wine_map_3)

        finally:  # закрываем подключение
            connection.close()

    def global_search():  # поиск по винодельне + названию
        try:
            with connection.cursor() as cursor:
                global_input = input("Введите название винодельни и название для показа всех вин: ")
                splitt = global_input.split()
                if len(splitt) == 3:
                    splitt[1] = splitt[1] + " "
                    if splitt[2] not in splitt[1]:
                        splitt[1] += splitt[2]
                elif len(splitt) == 4:
                    splitt[1] = splitt[1] + " "
                    if splitt[2] not in splitt[1]:
                        splitt[1] += splitt[2]
                        if splitt[3] not in splitt[1]:
                            splitt[1] += " " + splitt[3]
                elif len(splitt) == 5:
                    splitt[1] = splitt[1] + " "
                    if splitt[2] not in splitt[1]:
                        splitt[1] += splitt[2]
                        if splitt[3] not in splitt[1]:
                            splitt[1] += " " + splitt[3]
                            if splitt[4] not in splitt[1]:
                                splitt[1] += " " + splitt[4]

                new_splitt = splitt[0], splitt[1]
                cursor.execute(f"SELECT * FROM `wine` WHERE winery = '{new_splitt[0]}' AND name = '{new_splitt[1]}';")
                rows_4 = cursor.fetchall()
                for row_4 in rows_4:
                    print("_" * 100)
                    winery_show_4 = f" Винодельня: {row_4[0]} \n"
                    name_show_4 = f"Название: {row_4[1]} \n"
                    color_show_4 = f"Цвет вина: {row_4[2]} \n"
                    place_show_4 = f"Место хранения: {row_4[3]} \n"
                    tYpe_show_4 = f"Открыто/закрыто/закончено вино: {row_4[4]} \n"
                    amount_show_4 = f"Количество: {row_4[5]} \n"
                    wine_map_4 = f"Наличие в винной карте: {row_4[7]}"
                    print(winery_show_4, name_show_4, color_show_4, place_show_4, tYpe_show_4, amount_show_4, wine_map_4)

        finally:  # закрываем подключение
            connection.close()

    def start_list():  # старт лист
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM `wine` WHERE type = 'Открыто';")
                rows_5 = cursor.fetchall()
                for row_5 in rows_5:
                    print("_" * 100)
                    winery_show_5 = f" Винодельня: {row_5[0]} \n"
                    name_show_5 = f"Название: {row_5[1]} \n"
                    color_show_5 = f"Цвет вина: {row_5[2]} \n"
                    place_show_5 = f"Место хранения: {row_5[3]} \n"
                    tYpe_show_5 = f"Открыто/закрыто/закончено вино: {row_5[4]} \n"
                    amount_show_5 = f"Количество: {row_5[5]} \n"
                    wine_map_5 = f"Наличие в винной карте: {row_5[7]}"
                    print(winery_show_5, name_show_5, color_show_5, place_show_5, tYpe_show_5, amount_show_5, wine_map_5)

        finally:  # закрываем подключение
            connection.close()


    def stop_list():  # стоп лист
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM `wine` WHERE amount = 0;")
                rows_6 = cursor.fetchall()
                for row_6 in rows_6:
                    print("_" * 100)
                    winery_show_6 = f" Винодельня: {row_6[0]} \n"
                    name_show_6 = f"Название: {row_6[1]} \n"
                    color_show_6 = f"Цвет вина: {row_6[2]} \n"
                    place_show_6 = f"Место хранения: {row_6[3]} \n"
                    tYpe_show_6 = f"Открыто/закрыто/закончено вино: {row_6[4]} \n"
                    amount_show_6 = f"Количество: {row_6[5]} \n"
                    wine_map_6 = f"Наличие в винной карте: {row_6[7]}"
                    print(winery_show_6, name_show_6, color_show_6, place_show_6, tYpe_show_6, amount_show_6, wine_map_6)

        finally:  # закрываем подключение
            connection.close()


    # def open_bottle():
    #     try:
    #         with connection.cursor() as cursor:
    #             cursor.execute()

    print(("Добрый день. Нажмите цифру, соответствующую вашему запросу: \n"
           '1 - Показать все вина в ресторане \n'
           '2 - Записать новое вино в список \n'
           '3 - Поиск вина по винодельне \n'
           '4 - Поиск вина по названию \n'
           '5 - Поиск вина по месту хранения \n'
           '6 - Глобальный поиск вина (по винодельне + названию) \n'
           '7 - Показать старт лист (открытые вина) \n'
           '8 - Показать стоп лист (вина, которых нет в наличии) \n'
           '9 - Открыть бутылку вина \n'
           '10 - Налить из открытой бутылки вина \n'
           '11 - Очистить базу данных от бутылок со статусом "Закончено" \n'))

    selection = int(input())
    if selection == 1:
        show_all()
    elif selection == 2:
        inserting()
    elif selection == 3:
        show_winery()
    elif selection == 4:
        show_name()
    elif selection == 5:
        show_place()
    elif selection == 6:
        global_search()
    elif selection == 7:
        start_list()
    elif selection == 8:
        stop_list()


except Exception as ex:  # вывод ошибок
    print(ex)

