## Script Details

This script checks the property of the greatest common divisor (GCD) of Fibonacci numbers. 
Specifically, it verifies that gcd(F(m), F(n)) == F(gcd(m, n)) for given integers m and n.

## Usage

To use the script, simply run it with Python:

```bash
python fibo.py -n <first_number> -m <second_number>
```

Replace <first_number> and <second_number> with the integers you want to check.

### Example Output

```bash
python fibo.py -n 10 -m 15
```

```
F(15) = 610, F(10) = 55
gcd(15, 10) = 5
F(gcd(15, 10)) = 5
gcd(F(15), F(10)) = 5
Property holds? True
```

## Requirements

- Python 3.x