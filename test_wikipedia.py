from playwright.sync_api import Page, expect

def test_wikipedia(page: Page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role('link', name ='English').click()
    expect(page.get_by_text('Welcome to Wikipedia,')).to_be_visible()

