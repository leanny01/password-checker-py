import passwordChecker
import passwordChecker.test

name = input("Please input your name: ")
surname = input("Please input your surname: ")
password = input("Please input your password: ")
passConf = input("Please confirm your password: ")
passwordChecker.register(name, surname, password, passConf)
