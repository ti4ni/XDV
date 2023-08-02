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


    def show_all():
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
                    tYpe_show_0 = f"Открыто/закрыто вино: {row_0[4]} \n"
                    amount_show_0 = f"Количество: {row_0[5]} \n"
                    wine_map_0 = f"Наличие в винной карте: {row_0[6]}"
                    print(winery_show_0, name_show_0, color_show_0, place_show_0, tYpe_show_0, amount_show_0, wine_map_0)

        finally:  # закрываем подключение
            connection.close()


    def inserting():
        try:

            with connection.cursor() as cursor:
                winery = input("Название винодельни: ")
                name = input("Название вина: ")
                color = input("Цвет вина: ")
                place = input("Место хранения: ")
                tYpe = input("Открыто/закрыто: ")
                amount = input("Количество: ")
                cursor.execute(
                    f"INSERT INTO `wine` (winery, name, color, place, type, amount) VALUES ('{winery}', '{name}', '{color}', '{place}', '{tYpe}', '{amount}');")
                connection.commit()

        finally:  # закрываем подключение
            connection.close()


    def show_name_winery():
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
                    tYpe_show_1 = f"Открыто/закрыто вино: {row_1[4]} \n"
                    amount_show_1 = f"Количество: {row_1[5]} \n"
                    wine_map_1 = f"Наличие в винной карте: {row_1[6]}"
                    print(winery_show_1, name_show_1, color_show_1, place_show_1, tYpe_show_1, amount_show_1, wine_map_1)

        finally:  # закрываем подключение
            connection.close()


    def show_name_place():
        try:
            with connection.cursor() as cursor:
                place_input = input("Введите название места хранения для показа всех вин: ")
                cursor.execute(f"SELECT * FROM `wine` WHERE place = '{place_input}';")
                rows_2 = cursor.fetchall()
                for row_2 in rows_2:
                    print("_" * 100)
                    winery_show_2 = f" Винодельня: {row_2[0]} \n"
                    name_show_2 = f"Название: {row_2[1]} \n"
                    color_show_2 = f"Цвет вина: {row_2[2]} \n"
                    place_show_2 = f"Место хранения: {row_2[3]} \n"
                    tYpe_show_2 = f"Открыто/закрыто вино: {row_2[4]} \n"
                    amount_show_2 = f"Количество: {row_2[5]}"
                    print(winery_show_2, name_show_2, color_show_2, place_show_2, tYpe_show_2, amount_show_2)

        finally:  # закрываем подключение
            connection.close()


    print(("Добрый день. Нажмите цифру, соответствующую вашему запросу: \n"
           "1 - Показать все вина в ресторане \n"
           "2 - Записать новое вино в список \n"
           "3 - Поиск вина по винодельне \n"
           "4 - Поиск вина по месту хранения \n"))

    selection = int(input())
    if selection == 1:
        show_all()
    elif selection == 2:
        inserting()
    elif selection == 3:
        show_name_winery()
    elif selection == 4:
        show_name_place()

except Exception as ex:  # вывод ошибок
    print(ex)

