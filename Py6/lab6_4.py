def function(name, age, company = "unnamed"):
    print(f"Имя: {name}, возраст: {age}, компания: {company}")

person = ("Mihail", 30, "Google")
function(*person)