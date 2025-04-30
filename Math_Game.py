import random, threading, time
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    op = get_operation()
    lv = get_level()
    questions = 0
    score = 0
    while questions < 10:
        x, y = generate_integer(op, lv)
        questions += 1
        if op == "+": the_answer = x + y
        elif op == "-": the_answer = x - y
        elif op == "×": the_answer = x * y
        elif op == "÷": the_answer = x // y
        answer = [None]

        def ask():
            try:
                answer[0] = int(input(f"{Fore.CYAN}{x} {op} {y} = {Style.RESET_ALL}"))

            except ValueError:
                answer[0] = "invalid"
        in_thr = threading.Thread(target=ask)
        in_thr.start()
        t_1 = time.time()
        in_thr.join(timeout=10)
        t_2 = time.time()
        t = t_2 - t_1
        if in_thr.is_alive():
            print(f"{Fore.RED}⏰ Time's up!{Style.RESET_ALL}")
            in_thr.join()
        else:
            if answer[0] == "invalid":
                print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")
            elif answer[0] == the_answer:
                if t <= 5:
                    score += 2
                    print(f"{Fore.GREEN}Excellent! (+2 points) answered in {t:.2f} sec{Style.RESET_ALL}")
                else:
                    score += 1
                    print(f"{Fore.YELLOW}Good! (+1 point) answered in {t:.2f} sec{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Wrong! {x} {op} {y} = {the_answer}{Style.RESET_ALL}")

    print(f"{Fore.MAGENTA}🏁 Final score: {score}/20 🏁{Style.RESET_ALL}")

def get_operation():
    while True:
        op = input("Which operation (+, -, ×, or ÷)? ")
        if op in ("+", "-", "×", "÷"):
            return op
        else:
            print(f"{Fore.RED}Invalid! Try again...{Style.RESET_ALL}")

def get_level():
    while True:
        try:
            lv = int(input("Which level (1 or 2)? "))
            if lv in (1, 2):
                return lv
            else:
                print(f"{Fore.RED}Invalid! Try again...{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Invalid! Try again...{Style.RESET_ALL}")

def generate_integer(op, lv):
    if op == "+":
        if lv == 1:
            x = random.randint(0,100)
            y = random.randint(0,100)
        else:
            x = random.randint(-100,100)
            y = random.randint(-100,100)
    elif op == "-":
        if lv == 1:
            x = random.randint(0,100)
            y = random.randint(0,100)
            if x < y:
                x, y = y, x
        else:
            x = random.randint(-100,100)
            y = random.randint(-100,100)
    elif op == "×":
        if lv == 1:
            x = random.randint(0,10)
            y = random.randint(0,10)
        else:
            x = random.randint(-10,10)
            y = random.randint(-10,10)
    elif op == "÷":
        if lv == 1:
            x = random.randint(0,100)
            y = random.randint(1,10)
            x = x - (x % y)
        else:
            while True:
                y = random.randint(-10,10)
                if y != 0:
                    break
            x = random.randint(-100,100)
            x = x - (x % y)
    return x, y

if __name__ == "__main__":
    main()
