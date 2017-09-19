now = float(input("what is the time now? "))
wait = float(input("how many hours to wait? "))

totalhours = now + wait

alarm = totalhours % 24
print(alarm)