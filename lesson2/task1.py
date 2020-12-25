# Задание 1
list_of_types = [1, bin(2), True, "string", (1, 2), {1, 2}, [1, 2], {1: 2, 2: 3}, None,
                 bytes('10'.encode('utf-8')), bytearray(b"some text")]
for i in list_of_types:
    print(f'{i} {type(i)}')
print(type(1 / 0))