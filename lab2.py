#String Operations in Python 

#1. Find the length of the string 

  str = "Hello"
  print(len(str))

#2. Slice the string as per your choice 
    String = 'Hello'
    print(String[:3])
    print(String[1:4:2])

#3. Concatenate two strings 
    a = "Good"
    b = "Day"
    c = a + " " + b
    print(c)


#4. Convert lower case in to uppercase character
    a= "lowercase"
    print(a.upper())
    
#5. Convert upper case into lower case characters

    b= "UPPERCASE"
    print(b.lower())

#6. convert the character into Unicode ( Ascii values)

    str="d"
    pint(ord(str))

#7. convert Unicode into character 
    i=ord('A)
    print(i)

#8. Check whether the given "substring" exists in the string
    string1 = "hello world"
    substring = "world"
    exists = substring in string1
    print(f"8. Substring '{substring}' exists in the string: {exists}")


#9. Replace the character 'k' with 'h'

    string = "Hello World"
    new_string = string.replace("Hello", "Bye")

    print(new_string)

    
#10. Pad the string with "x" at the end
    s = "hello"
    padded = s.ljust(10, 'x')
    print(f"10. Padded string: {padded}")

#11. remove leading and trailing whitespace or specified characters from the string
    s = "  hello  "
    trimmed = s.strip()
    print(f"11. String after stripping whitespace: '{trimmed}'")

    s = "@@@hello@@@"
    trimmed = s.strip('@')
    print(f"    String after stripping '@': '{trimmed}'")

#12. split the given string in to group of five characters 
    s = "abcdefghijklmnopqrstuvwxy"
    split_strings = [s[i:i+5] for i in range(0, len(s), 5)]
    print(f"12. String split into groups of 5: {split_strings}")


#13. count total number of words 
     s = "My name is shreyas"
    word_count = len(s.split())
    print(f"13. Total number of words: {word_count}")


#14. Find the frequency of each characters in the string 
     s = "good"
    frequency = Counter(s)
    print(f"14. Character frequency: {frequency}")

#STDIN and File operators 
#15. get the file name from the user 
    file_name = input("Enter the file name: ")


#16. check the file exist or not 
    exists = os.path.isfile(file_name)
    print("16. File exists" if exists else "    File does not exist")

    if exits: 
	#17. read the contents from the file 
	with open(file_name, 'r') as file:
            content = file.read()
        print("17. File content:")
        print(content)

	#18. reverse the contents from the file 
	reversed_content = content[::-1]
        print("18. Reversed content:")
        print(reversed_content)

	#19. Write into the file 
	with open(file_name, 'a') as file:
            file.write("\nAppended text.")
        print("19. Text appended to file.")


#Math operations 
#20. convert Frequency in to percentage (continuation of 12th Question) 
      x = "example for frequency"
    frequency = Counter(x)
    total_chars = len(x)
    percentages = {char: (count / total_chars) * 100 for char, count in frequency.items()}
    print(f"20. Character frequencies as percentages: {percentages}")


#21. Perform modular arithmetic operation 
    a = 10
    b = 3
    modular_result = a % b
    print(f"21. Modular arithmetic result of {a} % {b}: {modular_result}")


#22. Find the prime numbers 
    #check the given number is prime or not 
    #print the prime numbers with the given range 
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_numbers_in_range(start, end):
        return [num for num in range(start, end + 1) if is_prime(num)]

    number = 29
    print(f"22. {number} is prime: {is_prime(number)}")

    start = 10
    end = 50
    print(f"    Prime numbers between {start} and {end}: {prime_numbers_in_range(start, end)}")


#23. Check the given two numbers are co prime or not 
     def are_coprime(x, y):
        return math.gcd(x, y) == 1

    num1 = 15
    num2 = 28
    print(f"23. Numbers {num1} and {num2} are co-prime: {are_coprime(num1, num2)}")


#24. find the factors for the given number ( can use python library)
     def find_factors(n):
        factors = [i for i in range(1, n + 1) if n % i == 0]
        return factors

    number = 36
    print(f"24. Factors of {number}: {find_factors(number)}")
