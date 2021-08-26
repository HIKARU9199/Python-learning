def divisors(num):
    divisors =[]
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors

    #ListComprenhension
# divisors = [i: for i in range(1, num + 1) if num % i ==1]

def run():
    num = int(input("Enter a Number: "))
    print(divisors(num))
    print("termino mi programa")

if __name__ == '__main__':
    run()