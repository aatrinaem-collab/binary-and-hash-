#Сохраняем просмотренные элементы в словаре вместе с их индексами и для каждого нового элемента проверяем, 
# есть ли в словаре число, дополняющее его до target, поэтому двойной цикл не нужен.
def twoSum(data, target):
    cache = {}
    for i in range(len(data)):
        diff = target - data[i]
        if diff in cache:
            return [cache[diff], i]
        cache[data[i]] = i
    return []

def main():
    print(twoSum([2, 7, 11, 15], 9))

if __name__ == "__main__":
    main()
