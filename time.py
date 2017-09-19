now = float(input("what is the time now? "))
wait = float(input("how many hours to wait? "))

totalhours = now + wait

alarm = total hours  % 24

if alarm > 12:
    print(str(alarm) + "pm")
else alarm < 12:
    print(str(alarm) + "am")

print(alarm)