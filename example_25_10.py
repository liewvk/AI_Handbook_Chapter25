results = [True, True, False, True, True]
successes = sum(results)
total = len(results)
rate = successes / total if total else 0.0
print(f'Success: {successes}/{total}')
print(f'Success rate: {rate:.0%}')

