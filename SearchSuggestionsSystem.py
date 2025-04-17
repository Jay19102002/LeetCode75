# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

def suggestedProducts(products, searchWord):
    products.sort()
    res = []
    for i in range(len(searchWord)):
        prefix = searchWord[:i + 1]
        suggestions = []
        for product in products:
            if product.startswith(prefix):
                suggestions.append(product)
            if len(suggestions) == 3:
                break
        res.append(suggestions)
    return res

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(suggestedProducts(products, searchWord))