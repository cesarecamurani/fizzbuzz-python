def FizzBuzz(num):

    if not num % 15:
        return "fizzbuzz"

    if not num % 5:
        return "buzz"

    if not num % 3:
        return "fizz"

    return num
