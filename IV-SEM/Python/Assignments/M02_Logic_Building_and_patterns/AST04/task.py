def right_triangle(n: int) -> str:
    s = ""
    for i in range(1, n+1):
        s += "*" * i
        if i < n:
            s += "\n"
    return s


if __name__ == "__main__":
    n = int(input())
    print(right_triangle(n))
if __name__ == "__main__":
    n = int(input())
    print(right_triangle(n))