def compare_version_strings(v_string_1, v_string_2):
    version_1 = v_string_1.split('.')
    version_2 = v_string_2.split('.')

    version_number_1 = int(''.join(version_1))
    version_number_2 = int(''.join(version_2))

    if version_1 > version_2:
        return f"{v_string_1} is greater than {v_string_2}"
    elif version_1 == version_2:
        return f'{v_string_1} is equal to {v_string_2}'
    else:
        return f'{v_string_2} is greater than {v_string_1}'


v_string_1 = '1.0'
v_string_2 = '1.2'
print(compare_version_strings(v_string_1, v_string_2))