def calculate_index(rows):
    result = {}
    total = 0

    for row in rows:
        for word in row.split(' '):
            if word in result:
                result[word]["amount"] += 1
            else:
                result[word] = {
                    "amount": 1,
                    "percent": 0
                }
            total += 1

    for word in result:
        result[word]["percent"] = result[word]["amount"] / total * 100

    return result

search_queries = [
    'watch new movies',
    'coffee near me',
    'how to find the determinant',
    'python',
    'data science jobs in UK',
    'courses for data science',
    'taxi',
    'google',
    'yandex',
    'bing',
    'foreign exchange rates USD/BYN',
    'Netflix movies watch online free',
    'Statistics courses online from top universities'
]

result = calculate_index(search_queries)

for word in result:
    print(result[word]["percent"],"%", word)
