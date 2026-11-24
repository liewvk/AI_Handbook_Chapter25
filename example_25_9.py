def proposed_email(subject, approved=False):
    if not isinstance(subject, str) or not subject.strip():
        raise ValueError('A subject is required')
    if approved is not True:
        return 'DRAFT ONLY: awaiting user approval'
    return 'SIMULATION ONLY: ready for authorized dispatch'
 
print(proposed_email('Book availability'))
print(proposed_email('Book availability', approved=True))

