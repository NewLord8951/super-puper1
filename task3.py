multiplier = int(input("Введите множитель: "))

start = 1
end = int(input("Введите конец диапазона: "))
while start <= end:
    result = start * multiplier
    print(f"{start} x {multiplier} = {result}")
    start += 1
