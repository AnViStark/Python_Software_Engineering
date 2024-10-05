def superset(set_1, set_2):
    if set_1 > set_2:
        print(f"0бъект {set_1} является чистым супермножеством")
    elif set_1 == set_2:
        print(f"Множества равны")
    elif set_1 < set_2:
        print(f"0бъект {set_2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

if __name__ == "__main__":
    superset({1, 2, 3, 4, 5}, {1, 2, 3, 4, 5})
    superset({1, 2, 3, 4, 5}, {1, 2, 3, 4})