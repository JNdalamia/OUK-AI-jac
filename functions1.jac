def is_max(num1: int, num2: int) -> int {
    if num1 > num2 {
        return num1;
    } else {
        return num2;
    }
}
with entry {
    print(is_max(20, 30));
}