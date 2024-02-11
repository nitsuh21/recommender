from faker import Faker

def get_fake_profiles(count=10):
    fake = Faker()
    user_data = []
    for _ in range(count):
        profile = fake.profile()
        data = {
            'username': profile['username'],
            'email': profile['email'],
            'is_active': True
        }
        if 'name' in profile:
            fname,lname = profile['name'].split(' ')[:2]
            data['first_name'] = fname
            data['last_name'] = lname
        user_data.append(data)
    
    return user_data