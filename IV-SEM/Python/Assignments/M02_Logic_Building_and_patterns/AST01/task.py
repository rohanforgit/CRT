def count_digits(n: int) -> int:
    lol = str(n)
    return len(lol)
    pass

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))
