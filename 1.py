# На каждой итерации длина отрезка поиска уменьшается примерно в два раза, поэтому O(log n)
# граница от 0 до n, так как n^0.5 лежит в этом отрезке, а уменьшить сверху нельзя так как n = 1 = n^2. А если target!=0, можно брать l = 1 
def binarySearchSqrt(target):
    l, r = 0, target
    while l <= r:
        middle = (l + r) // 2
        if middle * middle > target:
            r = middle - 1
        elif middle * middle < target:
            l = middle + 1
        else:
            return middle
    return r
def main():
    print(binarySearchSqrt(10))

if __name__ == "__main__":
    main()
