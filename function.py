# # def greet(name):
# #     """
# #     This function will be use greet everyone
# #     """
# #     print(f'Hello Everyone Here {name}')
# #
# # greet('Evans')
#
# #
# # def greet(name, age):
# #     """
# #     This function will be use greet everyone
# #     """
# #     print(f'Hello JOEL {name} You are {17} years')
# #
# # greet('JOEL',17)
#
#
#
# # def greet(name, age):
# #     """
# #     This function will be use greet everyone
# #     """
# #     print(f'Hello  {name} You are {age} years')
# #
# # greet('JOEL',17)
# # greet(age=34, name='Evans')
#
# def greet(name, age=0):
#     """
#     This function will be use greet everyone
#     """
#     print(f'Hello  {name} You are {age} years')
#
# greet('JOEL')


# def greet(name, age):
#     """
#     This function will be use greet everyone
#     """
#     print(f'Hello  {name} You are {age} years')
#
# greet('JOEL',17)
# greet(age=34, name='Evans')


def sum(*numbers):
    """This to sum numbers"""
    size = len(numbers)
    result = 0
    for i in range(size):
        result += numbers[i]
        print(f'the result is : {result}')

sum(2,3,5)
