items = [
    {
        "title": "3-к квартира, 80 м2, 13/22 эт.",
        "rooms": 3,
        "price": 70000,
        "petFriendly": True
    },
    {
        "title": "2-к квартира, 45 м2, 5/5 эт.",
        "rooms": 3,
        "price": 45000,
        "petFriendly": True,
        "deposit": 60000
    },
    {
        "title": "2-к квартира, 44 м2, 4/24 эт.",
        "rooms": 3,
        "price": 55000,
        "petFriendly": False,
        "deposit": 40000
    },
    {
        "title": "2-к квартира, 44 м2, 4/4 эт.",
        "rooms": 3,
        "price": 65000,
        "petFriendly": True
    },
]

# res = [item["price"] for item in items if item["price"] in range(45000, 60000) ]


def filter_items_by_price(items: list, low: int, hi: int) -> list:
    return list(filter(lambda x: x["price"] in range(low, hi), items))


res = filter_items_by_price(items, 45000, 60000)

#print(res)

def filter_by_title(items: list, substr: str) -> list:
  
  return list(filter(lambda x: substr in x["title"], items))

res_titles = filter_by_title(items, "квартира")
print(res_titles)