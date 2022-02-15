sec = int(input('Введите время в секундах '))
h = sec // 3600
m = (sec-(h * 3600))//60
s =  sec - (m * 60) - (h * 3600)
time = f' {h:02}:{m:02}:{s:02}'
print(time)

#s = sec % 60
#sec = sec // 60
#m = sec % 60
#h = sec // 60

