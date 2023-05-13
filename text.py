import copy


class BankAccount:
    def __init__(self, surname='', name='', personal_code='', account_number='', balance=0, currency=''):
        self.surname = surname
        self.name = name
        self.personal_code = personal_code
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def __str__(self):
        return f"{self.surname};{self.name};{self.personal_code};{self.account_number};{self.balance};{self.currency}"

    def __eq__(self, other):
        return isinstance(other, BankAccount) and self.account_number == other.account_number

    def __copy__(self):
        return BankAccount(self.surname, self.name, self.personal_code, self.account_number, self.balance, self.currency)

    def __deepcopy__(self, memo):
        return BankAccount(copy.deepcopy(self.surname, memo), copy.deepcopy(self.name, memo), copy.deepcopy(self.personal_code, memo),
                           copy.deepcopy(self.account_number, memo), copy.deepcopy(self.balance, memo), copy.deepcopy(self.currency, memo))

    def read_from_file(self, line):
        self.surname, self.name, self.personal_code, self.account_number, self.balance, self.currency = line.strip().split(";")

    def write_to_file(self, file):
        file.write(str(self) + "\n")


if __name__ == '__main__':
    with open('bank_accounts.txt') as f:
        accounts = []
        for line in f:
            account = BankAccount()
            account.read_from_file(line)
            accounts.append(account)

    for account in accounts:
        print(account)
