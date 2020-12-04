import base64
import pyperclip

# print("Пример ввода режима: e5, e33, d1, d15")
command =  input("Введите режим(e/d) и число повторений : ")
code = input("Введите слово для обработки: ")

if command[0] == "e":
	for it in range(1, int(command[1:]) + 1):
		code = bytes.decode(base64.b64encode(bytes(code, 'utf-8')))
		# print(command[0], it, code)
	print("Код создан!")
	pyperclip.copy(code)	# Копируем в буфер код

if command[0] == "d":
	# code = bytes(code, 'utf-8')
	for it in range(1, int(command[1:]) + 1):
		code = bytes.decode(base64.b64decode(bytes(code, 'utf-8')))	# Двойное преобразование нужно только для того, чтобы в буфер поступала строка
		# print(command[0], it, code)
	print("Код создан!")
	pyperclip.copy(code)	# Копируем в буфер код