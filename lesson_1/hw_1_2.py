a = input ("Vvedite kolichestvo sekund ")
b = a % 60
c = a // 3600
d = a // 60 - c * 60
vremya = f"{c:02}:{d:02}:{b:02}"
print (vremya)