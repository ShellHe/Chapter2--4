now = float(input("what is the time now? "))
wait = float(input("how many hours to wait? "))


totalhours = now + wait


alarm = totalhours % 24


if alarm > 12:
    alarm = alarm % 12
    print(str(alarm)+"pm")
else:
    print(str(alarm) + "am")


print(alarm)