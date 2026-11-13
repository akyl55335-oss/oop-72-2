#@abstractmethod
#@staticmethod
#@classmethod
#@property

# Декоратор — это функция, которая принимает другую функцию,
# добавляет ей дополнительное поведение и возвращает новую функцию.

def simple_decorator(func):
    def wrapper():
        print("До выполнения!!")
        func()
        print("После выполнения!!")
    return wrapper

# @simple_decorator
# def say_hello():
#     print("Hello world!!")

# say_hello()

def decorator_greeting(func):
    def wrapper(name):
        print(f"{name} привет!")
        func(name)
    return wrapper

@decorator_greeting
def greeting(name):
    print(f"{name} как дела ?")

# greeting("Ардагер")

def repeat_decorator(value):
    def decorator(func):
        def wrapper(name):
            for i in range(int(value)):
                func(name)
        return wrapper
    return decorator

# value_user = input("dddd")

# @repeat_decorator(value_user)
def say_hello(name):
    print(f"{name} Hello world!!")

# say_hello("ardger")


def class_decorator(cls):
    class NewClass(cls):
        def action(self):
            print("New method!!")
    return NewClass

# @class_decorator
class OldClass:
    def action(self):
        print('Old method')

# test_obj = OldClass()
# test_obj.action()
# print(type(test_obj))

#
# def get_item(nums, target):
#     return nums[target]
#
# print(get_item(list_nums, 5))

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    step_count = 0
    while left <= right:
        step_count += 1
        middle = (left + right) // 2
        print(f"Какой проход {step_count}")
        print(f"Середина = Index-{middle} = Item-{nums[middle]} ")
        print(f"Left-{left} = Right-{right} ")
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return "Не нашли!"

def get_element(nums,target):
    for i in nums:
        if i == target:
            return i
    return "Не нашли элемент"

list_nums = [91,1,2,3,4,5,6,7,8,9,10]
print(get_element(list_nums, 91))