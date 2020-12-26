# Задание 2
def get_user(name, surname, year_of_birth, city, email, phone):
    return (f"пользователь:\nимя = {name}\nфамилия = {surname}\n" +
            f"год рождения = {year_of_birth}\nгород проживания = {city}\n" +
            f"email = {email}\nтелефон = {phone}\n")


print(get_user("Vladimir", "Vladimirov", 1987, "Москва", "mail@mail", 999111))
