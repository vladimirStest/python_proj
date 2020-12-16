# Задание 6
products = []
params = ("название", "цена", "количество")
number = int(input("Какое количество товаров вы готовы описать: "))
product = {}

for count in range(number):
    for param in params:
        element = input(f"Введите {param} для товара {count + 1}: ")
        if element.isdigit():
            element = int(element)
        product[param] = element
    products.append((count + 1, product))
    product = {}
print(products)
