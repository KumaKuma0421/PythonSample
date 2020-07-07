def test_function01(num1: int, num2: int) -> int:

    response = -1

    if num1 == 1 and num2 == 1:
        print("num1 = 1 and num2 = 1")
        response = num1 + num2
    elif num1 > 1 and num2 > 1:
        print("num > 1 and num > 1")
        response = num1 + num2 + 10
    else:
        print("other response.")
        response = num1 * num2

    
    # 多少インデントが広くても問題ない。
    return response


if __name__ == "__main__":
    response = test_function01(2, 1)
    print("response=" + str(response))
