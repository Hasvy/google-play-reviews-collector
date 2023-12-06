def func():
    import bs4
    from Oppening_html_file import html_code, stop_name, reviews_folder

    result = open(reviews_folder + "result.txt", "a", encoding="utf-8")
    soup = bs4.BeautifulSoup(html_code, 'lxml')
    # First review
    # Name | review > review-header > inline-details > ul > li > span
    name = soup.find("span", class_="author-display-name")
    name = name.get_text()
    # Date | review > review-header > inline-details > ul > li
    # Checking date
    time = soup.find("li", class_="last-update-time")
    time = time.get_text()
    # Rating stars | review > div > star-rating > div
    rating = soup.find("star-rating")
    rating = str(rating)
    rating_soup = bs4.BeautifulSoup(rating, 'lxml')
    rating = rating_soup.div['aria-label']
    # Text in review | review > div > p > text-with-highlights
    text = soup.find("text-with-highlights")
    text = str(text)
    text_soup = bs4.BeautifulSoup(text, 'lxml')
    text = text_soup.span.span.get_text()
    print(name, file=result)
    print(time, file=result)
    print(rating, file=result)
    print(text + '\n', file=result)
    # All other reviews
    global name_in_cycle
    name_in_cycle = 'a'
    for sibling in soup.find("review").next_siblings:
        # Name
        name = sibling.find("span", class_="author-display-name")
        name = name.get_text()
        if name == stop_name:
            name_in_cycle = name
            break
        # Date
        time = sibling.find("li", class_="last-update-time")
        time = time.get_text()
        # Rating stars
        rating = sibling.find("star-rating")
        rating = str(rating)
        rating_soup = bs4.BeautifulSoup(rating, 'lxml')
        rating = rating_soup.div['aria-label']
        # Text in review
        text = sibling.find("text-with-highlights")
        text = str(text)
        text_soup = bs4.BeautifulSoup(text, 'lxml')
        text = text_soup.span.span.get_text()
        print(name, file=result)
        print(time, file=result)
        print(rating, file=result)
        print(text + '\n', file=result)
    result.close()
    return