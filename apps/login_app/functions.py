# from random import randint

# from pathlib import Path

# script_location = Path(__file__).absolute().parent
# file_location = script_location / 'pins.txt'

# usedpins = []
# current_pin = 0

# class Security:
#     def getpin():
#         invalid_pin = True
#         pin = 0
#         while invalid_pin == True:
#             pin = randint(99, 150)
#             print (pin)
#             file = open(file_location, "r")
#             for x in file:
#                 usedpins.append(x) 
#             if pin not in usedpins:
#                 invalid_pin = False
#                 break
#             print (invalid_pin)
#         file = open(file_location, "a")
#         file.write("\n" + str(pin))
#         file.close()
#         current_pin = pin
#         print (current_pin)