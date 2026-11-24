RECORD = {'title': 'AI for Beginners Handbook',
          'topic': 'AI foundations and Python examples'}
 
def research():
    return RECORD.copy()
 
def write(facts):
    return (f"{facts['title']} introduces "
            f"{facts['topic']}.")
 
def review(draft, facts):
    return all(value in draft for value in facts.values())
 
def run_workflow():
    facts = research()
    draft = write(facts)
    if not review(draft, facts):
        return {'status': 'rejected', 'draft': draft}
    return {'status': 'approved', 'draft': draft}
 
result = run_workflow()
print(result['status'].upper())
print(result['draft'])

