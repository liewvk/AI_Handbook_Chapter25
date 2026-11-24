def execute_with_limit(step, max_attempts=3):
    if not 1 <= max_attempts <= 5:
        raise ValueError('Invalid attempt limit')
    for attempt in range(1, max_attempts + 1):
        try:
            result = step()
            if result is None:
                raise ValueError('Empty result')
            return {'status': 'ok', 'attempts': attempt,
                    'result': result}
        except (ValueError, ConnectionError) as error:
            print(f'Attempt {attempt}: {error}')
    return {'status': 'failed', 'attempts': max_attempts}
 
print(execute_with_limit(lambda: 'Completed'))

