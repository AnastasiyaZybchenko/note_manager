status = input("Введите текущий статус выполнения: ")
print("Измените статус, выбрав нужную цифру: \n 1. Выполнено \n 2. В процессе \n 3. Отложено")
status_new = input()
print("Ваш выбор: ", status_new)
if status_new == 1:
    print("Статус заметки успешно обновлен на: 'Выполнено'")
elif status_new == 2:
    print("Статус заметки успешно обновлен на: 'В процессе'")
elif status_new == 3:
    print("Статус заметки успешно обновлен на: 'Отложено'")
