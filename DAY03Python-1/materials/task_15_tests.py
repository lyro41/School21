from task15 import BaseWallet, RubbleWallet, DollarWallet, EuroWallet


def cls(wallet):
    return wallet.__class__.__name__


class Test:
    def __init__(self, base, rubble, dollar, euro):
        self.BaseWallet = base
        self.RubbleWallet = rubble
        self.DollarWallet = dollar
        self.EuroWallet = euro
        self.all_wallets = (self.RubbleWallet, self.DollarWallet, self.EuroWallet)

    def get_exchange_rate(self, wallet):
        if isinstance(wallet, self.RubbleWallet) or wallet is self.RubbleWallet:
            return 1
        if isinstance(wallet, self.DollarWallet) or wallet is self.DollarWallet:
            return 60
        if isinstance(wallet, self.EuroWallet) or wallet is self.EuroWallet:
            return 70

    def test_init(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            assert wallet.name == "Name", f"Неверный name при создании {Wallet.__name__}"
            assert wallet.amount == 15, f"Неверный amount при создании {Wallet.__name__}"
            assert wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при создании {Wallet.__name__}"

    def test_add_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            summed_wallet = wallet + 20
            assert isinstance(summed_wallet, Wallet), f"Неверный тип при сложении {Wallet.__name__} с числом"
            assert summed_wallet.name == wallet.name, f"Изменилось имя кошелька при сложении {Wallet.__name__} с числом"
            assert summed_wallet.amount == 35, f"Неверная сумма при сложении {Wallet.__name__} с числом"
            assert summed_wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при сложении {Wallet.__name__} с числом"

    def test_radd_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            summed_wallet = 30 + wallet
            assert isinstance(summed_wallet, Wallet), f"Неверный тип при сложении числа с {Wallet.__name__}"
            assert summed_wallet.name == wallet.name, f"Изменилось имя кошелька при сложении числа с {Wallet.__name__}"
            assert summed_wallet.amount == 45, f"Неверная сумма при сложении числа с {Wallet.__name__}"
            assert summed_wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при сложении числа с {Wallet.__name__}"
    
    def test_add_wallet(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            for Other in self.all_wallets:
                other = Other("Right", 10)
                summed_wallet = wallet + other
                assert isinstance(summed_wallet, Wallet), f"Неверный тип при сложении {Wallet.__name__} с {Other.__name__}"
                assert summed_wallet.name == wallet.name, f"Изменилось имя кошелька при сложении {Wallet.__name__} с {Other.__name__}"
                true_amount = (wallet.amount * wallet.exchange_rate + other.amount * other.exchange_rate) / wallet.exchange_rate
                assert round(summed_wallet.amount, 2) == round(true_amount, 2),\
                    f"Неверная сумма при сложении {Wallet.__name__} с {Other.__name__} - {summed_wallet.amount} : {true_amount}"
                assert summed_wallet.exchange_rate == self.get_exchange_rate(wallet),\
                    f"Неверный exchange_rate при сложении {Wallet.__name__} с {Other.__name__}"

    def test_iadd_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            wallet += 20
            assert isinstance(wallet, Wallet), f"Неверный тип при += сложении {Wallet.__name__} с числом"
            assert wallet.name == "Name", f"Изменилось имя кошелька при += сложении {Wallet.__name__} с числом"
            assert wallet.amount == 35, f"Неверная сумма при += сложении {Wallet.__name__} с числом"
            assert wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при += сложении {Wallet.__name__} с числом"

    def test_iadd_wallet(self):
        for Wallet in self.all_wallets:
            for Other in self.all_wallets:
                wallet = Wallet("Name", 15)
                init = Wallet("Name", 15)
                other = Other("Right", 10)
                wallet += other
                assert isinstance(wallet, Wallet), f"Неверный тип при += сложении {Wallet.__name__} с {Other.__name__}"
                assert wallet.name == init.name, f"Изменилось имя кошелька при += сложении {Wallet.__name__} с {Other.__name__}"
                result_amount = (init.amount * self.get_exchange_rate(init) + other.amount * self.get_exchange_rate(other)) / self.get_exchange_rate(init)
                assert round(wallet.amount, 2) == round(result_amount, 2),\
                    f"Неверная сумма при += сложении {Wallet.__name__} с {Other.__name__}. {wallet.amount} : {result_amount}"
                assert wallet.exchange_rate == self.get_exchange_rate(init),\
                    f"Неверный exchange_rate при += сложении {Wallet.__name__} с {Other.__name__}"


    def test_sub_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            subbed_wallet = wallet - 5
            assert isinstance(subbed_wallet, Wallet), f"Неверный тип при вычитании из {Wallet.__name__} числа"
            assert subbed_wallet.name == wallet.name, f"Изменилось имя кошелька при вычитании из {Wallet.__name__} числа"
            assert subbed_wallet.amount == 10, f"Неверная сумма при вычитании из {Wallet.__name__} числа"
            assert subbed_wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при вычитании из {Wallet.__name__} числа"

    def test_rsub_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            subbed_wallet = 30 - wallet
            assert isinstance(subbed_wallet, Wallet), f"Неверный тип при вычитании из числа {Wallet.__name__}"
            assert subbed_wallet.name == wallet.name, f"Изменилось имя кошелька при вычитании из числа {Wallet.__name__}"
            assert subbed_wallet.amount == 15, f"Неверная сумма при вычитании из числа {Wallet.__name__}"
            assert subbed_wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при вычитании из числа {Wallet.__name__}"
    
    def test_sub_wallet(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            for Other in self.all_wallets:
                other = Other("Right", 10)
                subbed_wallet = wallet - other
                assert isinstance(subbed_wallet, Wallet), f"Неверный тип при вычитании из {Wallet.__name__} {Other.__name__}"
                assert subbed_wallet.name == wallet.name, f"Изменилось имя кошелька при вычитании из {Wallet.__name__} {Other.__name__}"
                assert round(subbed_wallet.amount, 2) == round((wallet.amount * wallet.exchange_rate - other.amount * other.exchange_rate) / wallet.exchange_rate, 2),\
                    f"Неверная сумма при вычитании из {Wallet.__name__} {Other.__name__}"
                assert subbed_wallet.exchange_rate == self.get_exchange_rate(wallet),\
                    f"Неверный exchange_rate при вычитании из {Wallet.__name__} {Other.__name__}"

    def test_isub_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            wallet -= 10
            assert isinstance(wallet, Wallet), f"Неверный тип при -= вычитании из {Wallet.__name__} числа"
            assert wallet.name == "Name", f"Изменилось имя кошелька при -= вычитании из {Wallet.__name__} числа"
            assert wallet.amount == 5, f"Неверная сумма при -= вычитании из {Wallet.__name__} числа"
            assert wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при -= вычитании из {Wallet.__name__} числа"

    def test_isub_wallet(self):
        for Wallet in self.all_wallets:
            for Other in self.all_wallets:
                wallet = Wallet("Name", 15)
                init = Wallet("Name", 15)
                other = Other("Right", 10)
                wallet -= other
                assert isinstance(wallet, Wallet), f"Неверный тип при -= вычитании из {Wallet.__name__} {Other.__name__}"
                assert wallet.name == init.name, f"Изменилось имя кошелька при -= вычитании из {Wallet.__name__} {Other.__name__}"
                assert round(wallet.amount, 2) == round((init.amount * init.exchange_rate - other.amount * other.exchange_rate) / init.exchange_rate, 2),\
                    f"Неверная сумма при -= вычитании из {Wallet.__name__} {Other.__name__}"
                assert wallet.exchange_rate == self.get_exchange_rate(init),\
                    f"Неверный exchange_rate при -= вычитании из {Wallet.__name__} {Other.__name__}"


    def test_mul_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            summed_wallet = wallet * 10
            assert isinstance(summed_wallet, Wallet), f"Неверный тип при умножении {Wallet.__name__} на число"
            assert summed_wallet.name == wallet.name, f"Изменилось имя кошелька при умножении {Wallet.__name__} на число"
            assert summed_wallet.amount == 150, f"Неверная сумма при умножении {Wallet.__name__} на число"
            assert summed_wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при умножении {Wallet.__name__} на число"

    def test_rmul_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            summed_wallet = 10 * wallet
            assert isinstance(summed_wallet, Wallet), f"Неверный тип при умножении числа на {Wallet.__name__}"
            assert summed_wallet.name == wallet.name, f"Изменилось имя кошелька при умножении числа на {Wallet.__name__}"
            assert summed_wallet.amount == 150, f"Неверная сумма при умножении числа на {Wallet.__name__}"
            assert summed_wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при умножении числа на {Wallet.__name__}"

    def test_imul_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            wallet *= 10
            assert isinstance(wallet, Wallet), f"Неверный тип при *= умножении {Wallet.__name__} на число"
            assert wallet.name == "Name", f"Изменилось имя кошелька при *= умножении {Wallet.__name__} на число"
            assert wallet.amount == 150, f"Неверная сумма при *= умножении {Wallet.__name__} на число"
            assert wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при *= умножении {Wallet.__name__} на число"

    def test_div_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            summed_wallet = wallet / 10
            assert isinstance(summed_wallet, Wallet), f"Неверный тип при делении {Wallet.__name__} на число"
            assert summed_wallet.name == wallet.name, f"Изменилось имя кошелька при делении {Wallet.__name__} на число"
            assert summed_wallet.amount == 1.5, f"Неверная сумма при делении {Wallet.__name__} на число"
            assert summed_wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при делении {Wallet.__name__} на число"

    def test_idiv_number(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            wallet /= 10
            assert isinstance(wallet, Wallet), f"Неверный тип при /= делении {Wallet.__name__} на число"
            assert wallet.name == "Name", f"Изменилось имя кошелька при /= делении {Wallet.__name__} на число"
            assert wallet.amount == 1.5, f"Неверная сумма при /= делении {Wallet.__name__} на число"
            assert wallet.exchange_rate == self.get_exchange_rate(wallet),\
                f"Неверный exchange_rate при /= делении {Wallet.__name__} на число"


    def test_eq(self):
        amount = 15
        for Wallet1 in self.all_wallets:
            for Wallet2 in self.all_wallets:
                wallet1 = Wallet1("Name", amount)
                wallet2 = Wallet2("Name", amount)
                if Wallet1 is Wallet2:
                    assert wallet1 == wallet2, "При одинаковых типах кошельков и суммах кошельки должны быть равны"
                else:
                    assert not (wallet1 == wallet2), "Разные типы кошельков при равных суммах не должны быть равны"
                wallet1 = Wallet1("Name1", amount)
                wallet2 = Wallet2("Name2", amount)
                if Wallet1 is Wallet2:
                    assert wallet1 == wallet2, "При одинаковых типах кошельков и суммах кошельки должны быть равны"
                else:
                    assert not (wallet1 == wallet2), "Разные типы кошельков при равных суммах не должны быть равны"
                wallet1 = Wallet1("Name", amount)
                wallet2 = Wallet2("Name", amount + 10)
                assert not (wallet1 == wallet2), "При разных суммах кошельки не должны быть равны"
                wallet1 = Wallet1("Name1", amount)
                wallet2 = Wallet2("Name2", amount + 10)
                assert not (wallet1 == wallet2), "При разных суммах кошельки не должны быть равны"
    
    def test_spend_all(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 15)
            wallet.spend_all()
            assert wallet.amount == 0, f"{Wallet.__name__}: spend_all не обнулил баланс кошелька с положительной зарплатой"
            wallet = Wallet("Name", -15)
            wallet.spend_all()
            assert wallet.amount == -15, f"{Wallet.__name__}: spend_all не должен обнулять отрицательный баланс"

    def test_to_base(self):
        for Wallet in self.all_wallets:
            wallet = Wallet("Name", 10)
            right_value = 10 * self.get_exchange_rate(wallet)
            assert wallet.to_base() == right_value, f"to_base выдает неверное значение: {wallet.to_base()} вместо {right_value}"

    def test_print(self):
        assert self.RubbleWallet("Name", 15).__str__() == "Rubble Wallet Name 15"
        assert self.DollarWallet("Name", 15).__str__() == "Dollar Wallet Name 15"
        assert self.EuroWallet("Name", 15).__str__() == "Euro Wallet Name 15"

    def run_all(self):
        for name, function in self.__class__.__dict__.items():
            if name.startswith("test_"):
                function(self)


tests = Test(BaseWallet, RubbleWallet, DollarWallet, EuroWallet)
tests.run_all()
