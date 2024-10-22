def add_position():
    date = input("Введите дату покупки: ")
    category = input("На что было потрачено: ")
    amount = float(input("Сумма траты: "))
    
    with open("Py7//traty.txt", "a") as file:
        file.write(f"{date}, {category}, {amount}\n")

def all_positions():
    try:
        with open("Py7//traty.txt", "r") as file:
            expenses = file.readlines()
            if expenses:
                print("Список трат:")
                for expense in expenses:
                    print(expense.strip())
            else:
                print("Данные о расходах отсутствуют.")
    except FileNotFoundError:
        print("Файл с расходами не найден.")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Показать всё")
        print("3. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_position()
        elif choice == "2":
            all_positions()
        elif choice == "3":
            break
        else:
            print("Некорректный ввод")

if __name__ == "__main__":
    main()
