import pprint

phone_inventory = [
    {
        "user": "Tyson",
        "number": "2061113334",
        "my_extension": "3334",
        "speed_dial": ["Keith", "Alec", "Chuck", "Alex"]
    },
    {
        "user": "James",
        "number": "2061115334",
        "my_extension": "5334",
        "speed_dial": ["John", "Jason"]
    },
    {
        "user": "Seth",
        "number": "2061119864",
        "my_extension": "9864",
        "speed_dial": ["Govenor", "Jeff"]
    }
]


# Unsorted list of phone profiles
print("\n\n#### Unsorted List")
pprint.pprint(phone_inventory)

# Sort the speed_dial of the first profile
print("\n\n#### Sort the first phone profile")
phone_inventory[0]['speed_dial'].sort()
pprint.pprint(phone_inventory[0])

# Sort the speed_dial of the first profile
phone_inventory[-1]['speed_dial'].sort()
print("\n\n#### Sort the last phone profile")
pprint.pprint(phone_inventory[-1])

# Add an additional profile to the inventory
phone_inventory.append(
    {
        "user": "Justin",
        "number": "2061117777",
        "my_extension": "7777",
        "speed_dial": ["Layne", "Weiss", "Britney"]
    }
)


def sort_phone(phone_obj):
    return phone_obj['user']

# Sort the list of profiles based on username
print("\n\n#### Sort all the entries by username")
phone_inventory.sort(key=sort_phone)
pprint.pprint(phone_inventory)
