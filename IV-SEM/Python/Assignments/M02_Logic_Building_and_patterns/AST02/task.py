def reverse_number(n: int) -> int:
    lol = str(n)
    josh = lol[::-1]
    francis =  int(josh)
    return francis

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))
