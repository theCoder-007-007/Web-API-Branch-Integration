def analyze_digits_and_case(user_input):
    user_input = user_input.strip()

    uppercase_count = sum(1 for char in user_input if char.isupper())
    digit_sum = sum(int(char) for char in user_input if char.isdigit())

    return uppercase_count, digit_sum