from scraper import scraper

def test_can_open_craigslist():
    links = scraper._open_craigslist(
        'file:///home/projects/pythonic_recruiter/pythonic_recruiter/scraper/test_data/fullpage.html'
    )
    assert len(links) == 100
    assert links[0] == 'http://boston.craigslist.org/gbs/sof/4882521354.html'

def test_can_get_craigslist_post():
    details = scraper._get_craigslist_post(
        'file:///home/projects/pythonic_recruiter/pythonic_recruiter/scraper/test_data/detail_page.html'
    )
    assert details['title'] == 'C# / ASP.NET Developer -- Downtown Boston'
    assert details['location'] == 'Downtown Boston'
    assert details['compensation'] == 'Competitive'
    assert details['contact_link'] == 'http://boston.craigslist.org/reply/bos/sof/4882521354'

