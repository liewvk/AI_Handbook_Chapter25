AGENTS = {'inventory', 'pricing', 'general'}
 
def supervisor(request):
    text = request.lower()
    if 'stock' in text or 'available' in text:
        selected = 'inventory'
    elif 'price' in text or 'cost' in text:
        selected = 'pricing'
    else:
        selected = 'general'
    assert selected in AGENTS
    return selected
 
for task in ['Check stock', 'Calculate price', 'Explain AI']:
    print(task, '->', supervisor(task))

