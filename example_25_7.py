verified = {'price_myr': 40.0, 'stock': 12}
 
def check_claims(claims):
    required = set(verified)
    if set(claims) != required:
        return False
    return (type(claims['price_myr']) in (int, float)
            and claims['price_myr'] == verified['price_myr']
            and type(claims['stock']) is int
            and claims['stock'] == verified['stock'])
 
print('Valid:', check_claims({'price_myr': 40.0, 'stock': 12}))
print('Valid:', check_claims({'price_myr': 45.0, 'stock': 12}))

