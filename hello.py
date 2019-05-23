password = input('Введите пароль: ')
#print(password)
if len(password) < 12:
  print ('Короткий пароль')
else:
  print ('Длинный пароль')
#print ('{} \nДлинна пароля {}'.format(password, len(password)))