def process_data(data):
    # Простая и понятная логика
    result = [x * 1.1 for x in data if x > 0]
    return result