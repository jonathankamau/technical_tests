class FizzBuzz:

    def fizz_buzz(self, n):

        if (n % 3 == 0) and (n % 5 == 0):
            return('FizzBuzz')
        elif (n % 3 == 0) and not (n % 5 == 0):
            return('Fizz')
        elif (n % 5 == 0) and not (n % 3 == 0):
            return('Buzz')
        else:
            return(n)
