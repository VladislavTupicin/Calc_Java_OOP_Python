def show_result(num):
    try:
        print(f"Ответ: > {num.get_values()}")
    except Exception as err:
        print("Invalud type data")
        print(err)


choice_operation = """
Доступные операции:
\t1. Сложение
\t2. Вычитание
\t3. Умножение
\t4. Деление
\t5. Выход
"""


