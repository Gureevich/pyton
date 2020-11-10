a = input ("Vvedite kolichestvo sekund ")
b = a % 60
c = a // 3600
d = a // 60 - c * 60
print (str(c) + ':' + str(d) + ':' + str(b))