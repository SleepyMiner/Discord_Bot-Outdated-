from duckduckgo_search import ddg

def search(keywords):
    results = ddg(keywords, region='wt-wt', safesearch='Off', time='y',max_results=5)
    return results[0]['body'][:4000], results[0]['title'], results[0]['href']

#print(search("lyrics of charlie puth attention"))
#query = "lyrics of charlie puth attention"
#response = search(query)[1] + '\n' + search(query)[2] + '\n' + search(query)[0]

#print(response)








