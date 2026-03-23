def process_data(data, curr='RUB'):
    # Техдолг: огромный if-else, дублирование логики, collect() в потенциале
    result = []
    if curr == 'RUB':
        for x in data:
            if x > 0:
                print(f"Processing {x}") # Техдолг: print вместо логгера
                result.append(x * 1.1 * 1.13)
    elif curr == 'USD':
        for x in data:
            if x > 0:
                result.append(x * 1.1 * 1.13 * 75) # Хардкод курса
    return result