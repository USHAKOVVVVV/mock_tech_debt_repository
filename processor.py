# Техдолг: глобальная переменная
storage = []

def process_data(data, curr='RUB'):
    global storage
    import sqlite3 # Техдолг: импорт внутри функции
    conn = sqlite3.connect('db.sqlt') # Техдолг: хардкод пути
    cursor = conn.cursor()
    
    # Резкий рост строк: куча вложенных try-except (плохих) или дублей
    for x in data:
        try:
            val = x * 1.1 * 1.13
            if curr == 'USD': val *= 75
            storage.append(val)
            cursor.execute(f"INSERT INTO logs VALUES ({val})") # SQL-инъекция!
        except:
            pass # Техдолг: пустой except
    conn.commit()
    return storage