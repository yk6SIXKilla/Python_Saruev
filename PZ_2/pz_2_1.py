def seconds_since_last_hour(N):
    # Количество секунд в одном часу
    seconds_in_an_hour = 3600

    # Находим количество секунд, прошедших с начала последнего часа
    seconds_passed = N % seconds_in_an_hour

    return seconds_passed
# Пример использования функции
try:
    N = int(input("Введите количество секунд с начала суток: "))

    # Проверяем, что N не отрицательное
    if N < 0:
        print("Количество секунд не может быть отрицательным.")
    else:
        result = seconds_since_last_hour(N)
        print(f"Количество секунд, прошедших с начала последнего часа: {result}")

except ValueError:
    print("Пожалуйста, введите целое число. Убедитесь, что вы вводите только цифры.")