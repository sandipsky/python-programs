
inp_seconds = int(input("Enter number of seconds"))


minute = (inp_seconds // 60) % 60

hours = inp_seconds // 3600

seconds = inp_seconds % 60

print(str(hours) + "hours" + str(minute) + "minutes" + str(seconds) + "seconds")


