# объявление функции
def get_shipping_cost(quantity):
    if quantity == 0:
        return 0
    return 1000 + (quantity-1)*120

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))