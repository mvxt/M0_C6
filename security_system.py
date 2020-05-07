# M0_C6 - Security System

# Write your code here.
# Define any variables or functions you need.
# The tests are testing your program's output.

users = {
    'mhenderson': 'out',
    'jjabrams': 'out',
    'sbrown': 'out',
    'enterocc': 'out',
    'zzdawg': 'out'
}

if __name__ == '__main__':
    err_msg = '  ALARM SOUNDED'
    while True:
        user_input = input('Input: ')
        input_arr = user_input.split()
        if len(input_arr) != 2:
            print(err_msg)
            continue

        username = input_arr[0]
        action = input_arr[1]

        if username not in users or action != 'in' and action != 'out' or action == users[username]:
            print(err_msg)
        else:
            users[username] = action
            print(f'  {username} is checked {action}')

