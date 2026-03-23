def process_data(data):
    # Добавили налог 13% хардкодом
    result = []
    for x in data:
        if x > 0:
            result.append(x * 1.1 * 1.13) # Техдолг: магические числа
    return result