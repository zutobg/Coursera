# budget.py

def on_budget(books, budget):
    result = {
        "books_on_budget": 0,
        "loan": 0
        }

    count = 0
    total_pr = sum(books)

    for book in books:
        if budget - book < 0:
            break

        budget -= book
        total_pr -= book
        count += 1

    result["books_on_budget"] = count
    result["loan"] = max(0, total_pr - budget)

    return result

print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
