from scraper import scraper

def test_can_open_craigslist():
    num_links = scraper._open_craigslist(
        'file:///home/projects/pythonic_recruiter/pythonic_recruiter/scraper/test_data/fullpage.html'
    )
    assert num_links == 100

    

