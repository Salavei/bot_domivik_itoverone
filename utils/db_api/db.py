import sqlite3
import datetime


class SQLestate:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # SQL ANNOUNCEMENTS ONLY

    def add_announcements_rent(self, price, number_of_rooms, street, rent_description, phone, photo,
                               date_time, tg_id, placed, allow=True, allow_admin=False):
        """Добавляем обьявление аренды"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `announcements_rent` (`price`,`number_of_rooms`,`street`,"
                "`rent_description`,`phone`,`placed`, `photo`, `date_time`, `allow_admin`, `allow`, `tg_id`) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                (price, number_of_rooms, street, rent_description, phone, placed, photo,
                 date_time, allow_admin, allow, tg_id))

    def add_announcements_sell(self, price, number_of_rooms, street, rent_description, phone, photo,
                               date_time, tg_id, placed, allow=True, allow_admin=False):
        """Добавляем обьявление продажи"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `announcements_sell` (`price`,`number_of_rooms`,`street`,"
                "`rent_description`,`phone`,`placed`, `photo`, `date_time`, `allow_admin`, `allow`, `tg_id`) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                (price, number_of_rooms, street, rent_description, phone, placed, photo,
                 date_time, allow_admin, allow, tg_id))

    def add_request_rent(self, id_an_rent, number_request, name_request):
        """Добавляем запрос аренды"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `request_rent` (`id_an_rent`,`number_request`,`name_request`) VALUES(?,?,?)",
                (id_an_rent, number_request, name_request))

    def add_request_sell(self, id_an_sell, number_request, name_request):
        """Добавляем запрос продажи"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `request_sell` (`id_an_sell`,`number_request`,`name_request`) VALUES(?,?,?)",
                (id_an_sell, number_request, name_request))

    def show_request_sell(self, id_tg):
        """показывает запрос продажи"""
        with self.connection:
            return self.cursor.execute(
                "SELECT `number_request`, `name_request`,`id_an_sell` FROM `request_sell` WHERE `id_an_sell` IN (SELECT `id` FROM `announcements_sell` WHERE `tg_id` =? )",
                (int(id_tg),)).fetchall()

    def show_request_rent(self, id_an_rent):
        """показывает запрос аренды"""
        with self.connection:
            return self.cursor.execute(
                "SELECT `number_request`, `name_request`,`id_an_rent` FROM `request_rent` WHERE `id_an_rent` IN (SELECT `id` FROM `announcements_rent` WHERE `tg_id` =? )",
                (int(id_an_rent),)).fetchall()

    def show_requeat_announcements_rent(self, id_an):
        """Показать все объявления по аренде"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_rent` WHERE `id` = ?", (id_an,)).fetchall()

    def show_requeat_announcements_sell(self, id_an):
        """Показать все объявления по аренде"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_sell` WHERE `id` = ?", (id_an,)).fetchall()

    def show_all_announcements_sell(self, ):
        """Показать все объявления по продаже"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_sell` WHERE `allow_admin` = ? and `allow` = ?",
                                       (True, True,)).fetchall()

    def show_all_announcements_rent(self, ):
        """Показать все объявления по аренде"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_rent` WHERE `allow_admin` = ? and `allow` = ?",
                                       (True, True,)).fetchall()

    def show_all_my_announcements_rent(self, tg_id):
        """Показать все объявления по аренде"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_rent` WHERE `tg_id` = ?", (tg_id,)).fetchall()

    def show_all_my_announcements_rent_request(self, id_an):
        """Показать все объявления по аренде для запросов"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_rent` WHERE `id` = ?", (id_an,)).fetchall()

    def show_all_my_announcements_sell(self, tg_id):
        """Показать все объявления по продаже"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_sell` WHERE `tg_id` = ?", (tg_id,)).fetchall()

    def show_all_my_announcements_sell_request(self, id_an):
        """Показать все объявления по продаже для запросов"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_sell` WHERE `id` = ?", (id_an,)).fetchall()

    def dell_an_sell_user(self, an_id):
        """Пользователь удаляет объявление продажи"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `announcements_sell` WHERE `id` =?", (an_id,))

    def dell_an_rent_user(self, an_id):
        """Пользователь удаляет объявление аренды"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `announcements_rent` WHERE `id` =?", (an_id,))

    # SQL USERS ONLY

    def check_subscriber(self, tg_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `tg_id` = ?', (tg_id,)).fetchall()
            return bool(len(result))

    def give_subscriber_card(self, tg_id):
        """

        """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `tg_id` = ?', (tg_id,)).fetchall()
            return result

    def take_my_cards(self, tg_id):
        """

        """
        with self.connection:
            result = self.cursor.execute('SELECT `street`, `number_house` FROM `users` WHERE `tg_id` = ?',
                                         (tg_id,)).fetchone()
            return result

    def take_my_info(self, tg_id):
        """

        """
        with self.connection:
            result = self.cursor.execute('SELECT `first_name`, `number_phone` FROM `users` WHERE `tg_id` = ?',
                                         (tg_id,)).fetchone()
            return result

    def take_all_cards_neighbors(self, street, number_house):
        """

        """
        idstart = int(number_house) + 3
        idend = int(number_house) - 3
        with self.connection:
            return self.cursor.execute(
                'SELECT * FROM `users` WHERE `street` = ? AND `number_house` <= ? OR `number_house` >= ?',
                (street, idstart, idend,)).fetchall()

    def give_feedback(self, tg_id, user_text):
        """

        """
        with self.connection:
            return self.cursor.execute("INSERT INTO `feedback` (`tg_id`, `user_text`)"" VALUES(?, ?)",
                                       (tg_id, user_text,))

    def try_search_car_owner(self, owner_car):
        return self.cursor.execute('SELECT * FROM `users` WHERE `car` = ?', (owner_car,)).fetchone()

    def successful_search_car_owner(self, owner_car):
        return self.cursor.execute('SELECT `tg_id` FROM `users` WHERE `car` = ?', (owner_car,)).fetchone()

    def subscriber_exists(self):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users`', ).fetchall()
            return len(result)

    def start_my_announcements_rent(self, id):
        """Проверяем, на запуск аренды"""
        with self.connection:
            return self.cursor.execute('SELECT `allow` FROM `announcements_rent` WHERE `id` = ?', (id,)).fetchone()[0]

    def start_my_announcements_sell(self, id):
        """Проверяем, на запуск продажи"""
        with self.connection:
            return self.cursor.execute('SELECT `allow` FROM `announcements_sell` WHERE `id` = ?', (id,)).fetchone()[0]

    def add_subscriber(self, tg_id, confirm, first_name, last_name, city, region, district, number_house, street,
                       entrance, floor, apartment, number_phone, car, admin=False):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `users` (`id`,`tg_id`, `admin` , `confirm`, `first_name`, `last_name`, `city`, `region`, `district`, `number_house`, `street`, `entrance`, `floor`,  `apartment`, `number_phone`, `car`) "
                "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    int(self.subscriber_exists()) + 1, tg_id, admin, confirm, first_name, last_name, city, region,
                    district,
                    number_house, street,
                    entrance, floor, apartment, number_phone, car))

    def update_domovik_subscriber(self, tg_id, first_name, last_name, city, region, district, number_house, street,
                                  entrance, floor, apartment, number_phone, car):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute(
                "UPDATE `users` SET `first_name`  =?, `last_name`  =?, `city`  =?, `region`  =?, `district`  =?, `number_house`  =?, `street`  =?, `entrance`  =?, `floor`  =?,  `apartment`  =?, `number_phone`  =?, `car`  =? WHERE `tg_id` =?"
                ,
                (first_name, last_name, city, region, district, number_house, street, entrance, floor, apartment,
                 number_phone, car, tg_id))

    def confirm_announcements_sell_user(self, id_conf, allow):
        """Подтвердить объявление продажи как юзер"""
        with self.connection:
            return self.cursor.execute("UPDATE `announcements_sell` SET `allow_admin` = ?, `allow` = ? WHERE `id` =?",
                                       (False, allow, id_conf))

    def confirm_announcements_rent_user(self, id_conf, allow):
        """Подтвердить объявление arend как юзер"""
        with self.connection:
            return self.cursor.execute("UPDATE `announcements_rent` SET `allow_admin` = ?, `allow` = ? WHERE `id` =?",
                                       (False, allow, id_conf))

    def confirm_announcements_sell_admin(self, id_conf):
        """Подтвердить объявление продажи как админ"""
        with self.connection:
            return self.cursor.execute("UPDATE `announcements_sell` SET `allow_admin` = ? WHERE `id` =?",
                                       (True, id_conf))

    def confirm_announcements_rent_admin(self, id_conf):
        """Подтвердить объявление аренды как админ"""
        with self.connection:
            return self.cursor.execute("UPDATE `announcements_rent` SET `allow_admin` = ? WHERE `id` =?",
                                       (True, id_conf))

    def dell_an_rent_admin(self, an_id):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `announcements_rent` WHERE `id` =?", (an_id))

    def dell_an_sell_admin(self, an_id):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `announcements_sell` WHERE `id` =?", (an_id))

    def why_get_admin(self, user_id) -> bool:
        """Проверка на админку"""
        with self.connection:
            return self.cursor.execute("SELECT `admin` FROM `users` WHERE `tg_id` =?", (user_id,)).fetchone()[0]

    def get_admin(self, user_id, allow_admin) -> list:
        """Выдача админки"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `admin` = ? WHERE `tg_id` =?", (allow_admin, user_id))

    def admin_all_announcements_rent(self, ):
        """Показать все объявления по аренде для админа"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_rent` WHERE `allow_admin` = ? and `allow` = ?",
                                       (False, True,)).fetchall()

    def admin_all_announcements_sell(self, ):
        """Показать все объявления по продаже для админа"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_sell` WHERE `allow_admin` = ? and `allow` = ?",
                                       (False, True,)).fetchall()

    def add_announcements(self, type_of_services, job_title, job_description, salary, phone, user_id, allow=False,
                          allow_admin=False):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `tg_my_announcements` (`type_of_services`,`job_title`,`job_description`,"
                "`salary`,`phone`,`allow`, `date_time`, `user_id_id`, `allow_admin`) VALUES(?,?,?,?,?,?,?,?,?)",
                (type_of_services, job_title,
                 job_description, salary, phone, allow, datetime.datetime.now(), user_id, allow_admin))

    def get_announcements_all(self, allow_admin=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_announcements` WHERE `allow_admin` = ?",
                                       (allow_admin,)).fetchall()

    def get_admin_announcements_all(self, allow_admin=False):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_announcements` WHERE `allow_admin` = ?",
                                       (allow_admin,)).fetchall()

    def get_announcements_my(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_announcements` WHERE `user_id_id` = ?",
                                       (user_id,)).fetchall()

    def add_resume(self, name, skills, area_of_residence, phone, user_id, allow=False, allow_admin=False):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `tg_my_resume` (`name`,`skills`,`area_of_residence`,"
                "`phone`,`allow`, `date_time`, `user_id_id`, `allow_admin`) VALUES(?,?,?,?,?,?,?,?)",
                (name, skills,
                 area_of_residence, phone, allow, datetime.datetime.now(), user_id, allow_admin))

    def get_resume_all(self, allow_admin=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_resume` WHERE `allow_admin` = ? ORDER BY `date_time` DESC",
                                       (allow_admin,)).fetchall()

    def update_resume_my(self, name, skills, area_of_residence, phone, user_id, allow=True, allow_admin=False):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `tg_my_resume` SET `name` = ? ,`skills` = ? ,`area_of_residence` = ?,`phone` = ? ,`allow` = ?, `date_time` = ?, `user_id_id`, `allow_admin` = ? WHERE `user_id_id` = ?",
                (name, skills,
                 area_of_residence, phone, allow, datetime.datetime.now(), user_id, user_id, allow_admin))

    def get_resume_my(self, user_id: int) -> list:
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_resume` WHERE `user_id_id` = ?", (user_id,)).fetchall()

    def get_resume_for_adm(self, allow_admin=False) -> list:
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_resume` WHERE `allow_admin` = ?",
                                       (allow_admin,)).fetchall()

    def get_announcement_for_adm(self, allow_admin=False) -> list:
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_announcements` WHERE `allow_admin` = ?",
                                       (allow_admin,)).fetchall()

    def stop_resume(self, user_id, ):
        with self.connection:
            take_id = self.cursor.execute("SELECT `id` FROM `users` WHERE `tg_id` =?", (int(user_id),)).fetchall()
            pars = self.cursor.execute("UPDATE `tg_my_resume` SET `allow` = ? WHERE `id` = ?", (0, *take_id[0],))
            return pars

    def confirm_my_resume(self, id_conf: int) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_resume` SET `allow` = ? WHERE `id` =?", (True, id_conf))

    def confirm_announcements(self, id_conf: int) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_announcements` SET `allow` = ? WHERE `id` =?", (True, id_conf))

    def update_announcements(self, id_conf: int, allow, allow_admin=False) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_announcements` SET `allow` = ?, `allow_admin` = ?  WHERE `id` =?",
                                       (allow, allow_admin, id_conf))

    def check_announcements(self, id_resume: int) -> bool:
        with self.connection:
            return \
                self.cursor.execute("SELECT `allow` FROM `tg_my_announcements` WHERE `id` = ?",
                                    (id_resume,)).fetchone()[0]
            # return bool(self.cursor)

    def start_my_resume(self, id_resume: int) -> bool:
        with self.connection:
            return self.cursor.execute("SELECT `allow` FROM `tg_my_resume` WHERE `id` = ?", (id_resume,)).fetchone()[0]
            # return bool(self.cursor)

    def update__my_resume(self, id_resume: int, allow, allow_admin=False) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_resume` SET `allow` = ?, `allow_admin` = ? WHERE `id` =?",
                                       (allow, allow_admin, id_resume))

    def reject_db_resume_admin(self, id_resume):
        with self.connection:
            return self.cursor.execute("DELETE FROM `tg_my_resume` WHERE `id` =?", (id_resume,))

    def reject_db_announcement_admin(self, id_resume):
        with self.connection:
            return self.cursor.execute("DELETE FROM `tg_my_announcements` WHERE `id` =?", (id_resume,))

    def confirm_resume_admin(self, id_conf: int) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_resume` SET `allow_admin` = ? WHERE `id` =?", (True, id_conf))

    def show_all_feedback(self) -> list:
        with self.connection:
            return self.cursor.execute("SELECT `user_text` FROM `feedback`", ).fetchall()

    def confirm_announcements_admin(self, id_conf: int) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_announcements` SET `allow_admin` = ? WHERE `id` =?",
                                       (True, id_conf))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
