import time 

my_time = int(input("Enter the time in seconds: "))


x=my_time

while x > 0:
    print(x)

    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600

    print('Time left: {} hours, {} minutes, {} seconds'.format(hours, minutes, seconds))

    time.sleep(1)

    x -= 1

print("beep beep beep")