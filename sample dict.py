"""contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
#contacts['Jason'] = '555-0000'
jasons_phone = contacts['Jason']
print('Dial {} to call Jason.'.format(jasons_phone))

contacts ={'aki' : '1111111', 'vvi' : '34444444'}
contacts['k123'] ='0000'

#print (contacts['qq'])
#print(contacts)
for number in contacts :
    print('phone : {}'.format(number))"""



people = {
    "Jeff": "Is afraid of clowns.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display the original dictionary
print("Original list:")
for person, fact in people.items():
    print(f"{person}: {fact}")

# Change a fact about one person
people["Jeff"] = "Is afraid of heights."

# Add a new person and fact
people["Jill"] = "Can hula dance."

# Display the updated dictionary
print("\nUpdated list:")
for person, fact in people.items():
    print(f"{person}: {fact}")