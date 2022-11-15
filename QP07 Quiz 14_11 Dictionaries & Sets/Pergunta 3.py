def roman_to_integer(a_string):
     dict_roman_to_decimal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
     order_roman = list(dict_roman_to_decimal.keys())
     result = 0
     for counter, current_char in enumerate(a_string):
         if counter > 0:
             previous_char = a_string[counter-1]
         else:
             previous_char = "M"
         if order_char(previous_char, current_char, order_roman):
             result += dict_roman_to_decimal[current_char]
         else:
             result -= dict_roman_to_decimal[previous_char] * 2
             result += dict_roman_to_decimal[current_char]
     return result
             
def order_char(previous_char, current_char, order_roman):
    for counter, char in enumerate(order_roman):
        if char == previous_char:
            position_previous_char = counter
        if char == current_char:
            position_current_char = counter
    if position_current_char <= position_previous_char:
        return True
    else:
        return False