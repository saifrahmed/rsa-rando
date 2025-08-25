import random
import gmpy2
from gmpy2 import mpz, isqrt


RSA_TODO=mpz('35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667')
RSA_TODO=mpz('992654469589')
RSA_TODO=mpz('135066410865995223349603216278805969938881475605667027524485143851526510604859533833940287150571909441798207282164471551373680419703964191743046496589274256239341020864383202110372958725762358509643110564073501508187510676594629205563685529475213500852879416377328533906109750544334999811150056977236890927563')
sqrt_n = isqrt(RSA_TODO)

def trial_division(n, max_trials=100000000):
    """
    Attempt to factorize n using random trial division.
    Returns a factor if found, otherwise None.
    """
    for _ in range(max_trials):
        # Generate a random odd number between 2 and sqrt(n)
        # For RSA-2048, sqrt is ~2^1024, so we'll use a smaller range for practicality
        candidate = random.randrange(3, sqrt_n, 2)  # Start with smaller numbers
        candidate = mpz(candidate)

        print(f"Trying {candidate}", end="")        
        # Check if candidate is a factor
        remainder = n % candidate
        if remainder == 0:
            return candidate
        else:
            print(f"\t no luck, remainder {remainder}")
    return None

def main():
    print("Attempting to factor RSA-2048 challenge number...")
    print(f"Number length: {len(str(RSA_TODO))} digits")
    
    factor = trial_division(RSA_TODO)
    
    if factor:
        print(f"\nFound factor: {factor}")
        other_factor = RSA_TODO // factor
        print(f"Other factor: {other_factor}")
        print(f"Verification: {factor} * {other_factor} = {factor * other_factor}")
    else:
        print("No factor found within trial limit.")

if __name__ == "__main__":
    main()
