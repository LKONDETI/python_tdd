class FizzBuzz:

# program should return Fizz when input is multiple of 3
# program should return buzz when input is multiple of 5
# any other return should return False

    def convert(self, number: int):
        result = ''

        if number % 15 == 0:
            result+='FizzBuzz'
        elif number % 5 == 0:
            result+='Buzz'
        elif number % 3 ==0:
            result+='Fizz'
        else:
            result=number
        return result