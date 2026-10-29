# Подсчитываем количество каждой буквы в строке a, затем вычитаем вхождения букв из b; 
# лишней будет буква, которой не осталось в первой строке. Алгоритм работает за O(n)
def extraLetter(a, b):
    hashMap = {}
    for c in a:
        hashMap[c] = hashMap.get(c, 0) + 1
    for c in b:
        if c not in hashMap or hashMap[c] == 0:
            return c
        hashMap[c] -= 1
    return ""

def main():
    print(extraLetter("abcd", "abcde"))

if __name__ == "__main__":
    main()
