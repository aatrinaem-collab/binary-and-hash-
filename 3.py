# Сортируем животных и порции еды по возрастанию и каждой порцией кормим самое маленькое из ещё не накормленных животных, которому её хватает,
# поскольку так мы сохраняем более крупные порции для животных с большей потребностью и получаем максимальное количество накормленных животных.
def feedAnimals(animals, food):
    if len(animals) == 0 or len(food) == 0:
        return 0
    animals.sort()
    food.sort()
    count = 0
    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            break
    return count

def main():
    print(feedAnimals([8, 2, 3, 2], [1, 4, 3, 8]))

if __name__ == "__main__":
    main()
