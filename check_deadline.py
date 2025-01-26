import datetime

# Получаем текущую дату
today = datetime.date.today().strftime("%d.%m.%Y")
print('Текущая дата:', today)


def check_deadline(issue_date_str):
    # Определяем формат даты
    date_format = "%d-%m-%Y"

    # Преобразуем строку даты в объект datetime
    try:
        issue_date = datetime.datetime.strptime(issue_date_str, date_format)
    except ValueError:
        print("Неверный формат даты! Пожалуйста, используйте формат: день-месяц-год (DD-MM-YYYY).")
        return

    # Получаем текущую дату
    current_date = datetime.datetime.now()

    # Сравниваем даты
    if issue_date < current_date:
        print("Предупреждение: дедлайн истек!")
    elif issue_date == current_date:
        print("Сегодня последний день выполнения задачи!")
    else:
        days_remaining = (issue_date - current_date).days
        print(f"У вас еще {days_remaining} {'день' if days_remaining == 1 else 'дня'} до истечения дедлайна.")


if __name__ == "__main__":
    deadline_input = input("Введите дату дедлайна (день-месяц-год): ")
    check_deadline(deadline_input)
