# 1 kzt -> 1 usd
currency_rate = 400


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.wallet = 0
        self.currency = 'KZT'


def add(user: User, amount: int) -> bool:
    user.wallet += amount
    return True


def withdraw(user: User, amount: int) -> bool:
    if user.wallet > amount:
        user.wallet -= amount
        return True

    return False


def change_currency(user: User) -> bool:
    user.wallet = user.wallet / currency_rate if user.currency == 'KZT' else user.wallet * currency_rate
    user.currency = 'USD' if user.currency == 'KZT' else 'KZT'

    return True


def main():
    prompt = 'Choose operation below:\n' \
             '1. Add balance to account\n' \
             '2. Withdraw balance from account\n' \
             '3. Change currency to {currency}\n' \
             '4. See current balance\n' \
             '0. Exit\n'

    user = User('username', 0)

    shut_off = False
    while not shut_off:
        command = int(input(prompt.format(currency=user.currency)))

        match command:
            case 1:
                amount = int(input('Enter amount\n'))
                add(user, amount)
            case 2:
                amount = int(input('Enter amount\n'))
                if not withdraw(user, amount):
                    print('You don\'t have enough money')
            case 3:
                change_currency(user)
            case 4:
                print(f'{user.wallet} {user.currency}')
            case 0:
                shut_off = True


if __name__ == '__main__':
    main()
