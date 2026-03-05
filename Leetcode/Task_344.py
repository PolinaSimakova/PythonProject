
def reverse_string(s: list[str]) -> None:
    start_index = 0

    for end_index in range(len(s)-1, len(s) // 2 -1, -1):
        temp = s[start_index]
        s[start_index] = s[end_index]
        s[end_index] = temp
        start_index +=1

if __name__ == "__main__":
    arr = ["a", "b", "c"]
    reverse_string(arr)
    print(arr)