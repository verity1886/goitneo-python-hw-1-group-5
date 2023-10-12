def parse_input(user_input):
    cmd = ''
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except ValueError:
        return cmd, []


def validate_contact_args(args):
    if len(args) != 2:
        return 'Error: namely 2 arguments (Name & Phone Number) are required.'

    name, phone = args
    if (len(name) > 20 or len(phone) > 20):
        return 'Error: args shouldn\'t contain more than 20 symbols each.'

    # seem like validation of the phone number is out of scope

    return ''


def handle_add_contact(args, contacts):
    validation_res = validate_contact_args(args)
    if validation_res:
        return validation_res

    name, phone = args
    contacts[name] = phone
    return 'Contact is added.'


def handle_change_contact(args, contacts):
    validation_res = validate_contact_args(args)
    if validation_res:
        return validation_res

    name, phone = args
    if name not in contacts:
        return 'Contact is not found.'

    contacts[name] = phone
    return 'Contact is updated.'


def handle_show_contact(args, contacts):
    if len(args) != 1:
        return 'Error: namely 1 argument (Name) is required.'

    name = args[0]
    if name not in contacts:
        return 'Contact is not found.'

    return contacts[name]


def handle_get_all(contacts):
    format_str = '{:<21}  {:<21}'
    lines = [format_str.format(name, contacts[name]) for name in contacts]
    output = ['=' * 42, format_str.format('Name:', 'Phone Number: ')]
    output = output + lines + ['=' * 42]

    return '\n'.join(output)


def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == '':
            continue
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(handle_add_contact(args, contacts))
        elif command == 'change':
            print(handle_change_contact(args, contacts))
        elif command == 'phone':
            print(handle_show_contact(args, contacts))
        elif command == 'all':
            print(handle_get_all(contacts))
        else:
            print('Invalid command.')


if __name__ == '__main__':
    main()
