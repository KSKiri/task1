s = input()
h = len(s) // 2
print(s[:h] == s[:len(s)-h-1:-1])
нужна строка, потом с помощью срезов смотрим, равна её первая половина со второй, записанной наоборот. Если нечётное количество символов, то средний символ не используется в проверке, потому что не влияет на итог.