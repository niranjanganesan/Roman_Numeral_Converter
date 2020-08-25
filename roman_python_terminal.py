import roman_convert

def main():
    print('Please enter Roman Numeral(s): ')
    string = str(input())
    result = roman_new.fromRoman(string)
    Blank_Input = result[1]
    Invalid_Input = result[2]
    output = result[0]
    if Invalid_Input:
        print('Invalid Roman numeral: ' +"'"+ string +"'"+ '. Please enter a valid input')
    elif Blank_Input:
        print('Input cannot be blank')
    else:
        print('The numeric equivalent is', output)


if __name__=="__main__":
    main()