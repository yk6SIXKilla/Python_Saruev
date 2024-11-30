def seconds_since_last_hour(N):
    # Количество секунд в одном часу
    seconds_in_an_hour = 3600

    # Находим количество секунд, прошедших с начала последнего часа
    seconds_passed = N % seconds_in_an_hour

    return seconds_passed


# Пример использования функции
N = int(input("Введите количество секунд с начала суток: "))
result = seconds_since_last_hour(N)
print(f"Количество секунд, прошедших с начала последнего часа: {result}")