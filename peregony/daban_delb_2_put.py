def find_uppercase_text(query):
    try:
        with open('D:/1 Dosug/Programming/my_work/my_project/zapros_rele/peregony/daban_delb_2_put', 'r', encoding='utf-8') as file:
            for line in file:
                if query.upper() in line:
                    return line
        return "Нет такого прибора."
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


if __name__ == '__main__':
    query = input("Введите полное название реле для поиска: ")
    result = find_uppercase_text(query)
    print(result)