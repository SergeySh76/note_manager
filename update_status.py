#Отображение списка возможных статусов и выбора нового статуса заметки
print("Выберите новый статус заметки:")
print("1. Выполнено")
print("2. В процессе")
print("3. Отложено")

# Словарь соответствия числового значения статусу
status_dict = {1:"выполнено", 2:"в процессе", 3:"отложено"}
while True:
    choice = input("Ваш выбор: ")
    if choice.isdigit():
        choice = int(choice)
        if choice in status_dict:
            new_status = status_dict[choice]
            print(f"Статус заметки успешно обновлён на: \"{new_status}\"")
            break
        else:
            print("Пожалуйста, выберите корректное значение.")
    else:
        print("Пожалуйста, введите число.")