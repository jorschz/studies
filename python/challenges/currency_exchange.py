def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    return round(amount % denomination, 3)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_rate = spread / 100
    new_value = exchange_rate * (1 + spread_rate)
    converted = budget / new_value
    bills = converted // denomination
    return bills * denomination


tests = [
    (exchange_money, (100000, 0.8), 125000),
    (exchange_money, (700000, 10.0), 70000),
    (get_change, (463000, 5000), 458000),
    (get_change, (1250, 120), 1130),
    (get_change, (15000, 1380), 13620),
    (get_value_of_bills, (10000, 128), 1280000),
    (get_value_of_bills, (50, 360), 18000),
    (get_value_of_bills, (200, 200), 40000),
    (get_number_of_bills, (163270, 50000), 3),
    (get_number_of_bills, (54361, 1000), 54),
    (get_leftover_of_bills, (10.1, 10), 0.1),
    (get_leftover_of_bills, (654321.0, 5), 1.0),
    (get_leftover_of_bills, (3.14, 2), 1.14),
    (exchangeable_value, (100000, 10.61, 10, 1), 8568),
    (exchangeable_value, (1500, 0.84, 25, 40), 1400),
    (exchangeable_value, (470000, 1050, 30, 10000000000), 0),
    (exchangeable_value, (470000, 0.00000009, 30, 700), 4017094016600),
    (exchangeable_value, (425.33, 0.0009, 30, 700), 363300),
]
# Testes organizados no formato (função, a, b, resultado esperado. sem uso de args)

for func, args, expected in tests:
    result = func(*args)
    assert result == expected, f"{func.__name__}{args} -> {result}, esperado {expected}"
print("Todos os testes passaram.")
