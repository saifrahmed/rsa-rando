import random
from pprint import pprint

import gmpy2
from gmpy2 import mpz, isqrt


def trial_division(n, max_trials=100000000):
    """
    Attempt to factorize n using random trial division.
    Returns a factor if found, otherwise None.
    """

    sqrt_n = isqrt(n)
    for x in range(max_trials):
        candidate = random.randrange(3, sqrt_n, 2)
        candidate = mpz(candidate)

        print(f"Attempt {x:,}: Trying {candidate}", end="")        
        # Check if candidate is a factor
        remainder = n % candidate
        if remainder == 0:
            return candidate
        else:
            print(f"\t no luck, remainder {remainder}")
    return None

def get_problems(infile="problems.csv"):
    import csv
    problems = {}
    with open(infile, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            problems[row[0]] = mpz(row[1].strip().replace(',', '').replace(' ', ''))
    return problems

def main():
    problems = get_problems()
    pprint(problems)
    print(f"Found {len(problems)} problems")
    prob = input("Enter a challenge to factorize: ").strip().upper()
    num_to_factor = problems[prob]
    print(f"Number length: {len(str(num_to_factor))} digits")

    for problem in problems:
        print(f"Attempting to factor {problem}...")
        print(f"Number length: {len(str(problems[problem]))} digits")
        
        factor = trial_division(num_to_factor)
    
    if factor:
        print(f"\nFound factor: {factor}")
        other_factor = num_to_factor // factor
        print(f"Other factor: {other_factor}")
        print(f"Verification: {factor} * {other_factor} = {factor * other_factor}")
    else:
        print("No factor found within trial limit.")

if __name__ == "__main__":
    main()
