# # Testing LEGB

# #1) With variables
# x = "Global Variable".capwords
# def mainFn():
#     x="Enclosed Variable"
#     def localFn():
#         nonlocal x
#         x = "Local Variable"
#         print(x)
#     localFn()
#     print(x)
# mainFn()
# print(x)

# # #2) With Functions
# # def opNum(a ,b):
# #     print("Addition(Global)", a+b)
# # def operations(a,b):
# #     def opNum():
# #         print("Subtraction(Enclosed)", a-b)
# #     opNum()
# # operations(1,2)
# # # opNum(1,2)
# b,o,h = False, False, True
# base = 2 if b else 8 if o else 16 if h else 1
print (list(zip(["1","2","3"],[1,2,3])))