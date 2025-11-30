import wikipedia

page_title = input("Enter page title: ").strip()
while page_title != '':
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as error:
        print("We need a more specific title. Try one of the following, or a new search:")
        print("(BeautifulSoup warning)")
        print(error.options)
    except wikipedia.exceptions.PageError:
        print(f"Page id \"{page_title}\" does not match any pages. Try another id!\n")
    else:
        print(page.title)
        print(page.summary.split('\n')[0])
        print(page.url)

    page_title = input("Enter page title: ").strip()
print("Thank you.")
