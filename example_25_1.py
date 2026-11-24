CATALOGUE = {'AI Handbook': 40.0, 'Python Guide': 55.0}
 
def research_agent(title):
    if title not in CATALOGUE:
        return {'found': False, 'title': title}
    return {'found': True, 'title': title,
            'unit_price': CATALOGUE[title]}
 
def writing_agent(facts, quantity):
    if not facts['found']:
        return 'Title not found'
    amount = facts['unit_price'] * quantity
    return f"{quantity} x {facts['title']}: MYR {amount:.2f}"
 
def review_agent(facts, quantity, draft):
    if not facts['found']:
        return draft == 'Title not found'
    expected = f"MYR {facts['unit_price'] * quantity:.2f}"
    return expected in draft
 
facts = research_agent('AI Handbook')
draft = writing_agent(facts, 2)
print(draft)
print('Review passed:', review_agent(facts, 2, draft))

