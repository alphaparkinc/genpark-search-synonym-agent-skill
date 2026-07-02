from client import SearchSynonymClient
def main():
    c = SearchSynonymClient()
    print(c.optimize_query("cheap mobile earbud"))
if __name__ == '__main__':
    main()
