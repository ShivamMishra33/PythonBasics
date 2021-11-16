class CoffeeMachine:
    def __init__(self, money, water, milk, coffee_beans, disposable_cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups

    def print_values(self):
        print("The coffee machine has :")
        print('{} of water'.format(self.water))
        print('{} of milk'.format(self.milk))
        print('{} of coffee beans'.format(self.coffee_beans))
        print('{} of disposable cups'.format(self.disposable_cups))
        print('${} of money'.format(self.money))
        print()

    def buy(self):
        buy_ = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        print()
        if buy_ == '1':
            if self.water < 250:
                print('Sorry, not enough water')
                print()
            elif self.coffee_beans < 16:
                print('Sorry, not enough coffee beans')
                print()
            elif self.disposable_cups < 1:
                print('Sorry not enough disposable cups')
                print()
            else:
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.disposable_cups -= 1
                print('I have enough resources, making you a coffee!')
                print()
        elif buy_ == '2':
            if self.water < 350:
                print('Sorry, not enough water')
                print()
            elif self.coffee_beans < 20:
                print('Sorry, not enough coffee beans')
                print()
            elif self.disposable_cups < 1:
                print('Sorry not enough disposable cups')
                print()
            elif self.milk < 75:
                print('Sorry not enough milk')
                print()
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.disposable_cups -= 1
                print('I have enough resources, making you a coffee!')
                print()
        elif buy_ == '3':
            if self.water < 200:
                print('Sorry, not enough water')
                print()
            elif self.coffee_beans < 12:
                print('Sorry, not enough coffee beans')
                print()
            elif self.disposable_cups < 1:
                print('Sorry not enough disposable cups')
                print()
            elif self.milk < 100:
                print('Sorry not enough milk')
                print()
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.disposable_cups -= 1
                print('I have enough resources, making you a coffee!')
                print()
        elif buy_ == 'back':
            return

    def fill(self):
        w = int(input('Write how many ml of water do you want to add:'))
        self.water += w
        m = int(input("Write how many ml of milk do you want to add:"))
        self.milk += m
        c = int(input('Write how many gms of coffee do you want to add:'))
        self.coffee_beans += c
        d = int(input('Write how many disposable cups do you want to add:'))
        self.disposable_cups += d
        print()

    def take(self):
        print('I gave you {}'.format(self.money))
        print()
        self.money = 0


# Main Program
cm = CoffeeMachine(550, 400, 540, 120, 9)
action = input('Write action (buy, fill, take, remaining, exit):')
while action != 'exit':
    if action == 'buy':
        print()
        cm.buy()
    elif action == 'fill':
        print()
        cm.fill()
    elif action == 'take':
        print()
        cm.take()
    elif action == 'remaining':
        cm.print_values()
    elif action == 'exit':
        break
    action = input('Write action (buy, fill, take, remaining, exit): ')
