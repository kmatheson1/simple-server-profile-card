from playwright.sync_api import Page, expect

def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200



# will no work without SSL certificate
# def test_has_title(page: Page):
#     page.goto("https://kmatheson-portfolio.xf.mkrs.link")
#     h1_tags = page.locator("h1")
#     # Expect a title "to contain" a substring.
#     expect(h1_tags).to_have_text("Kieran Matheson")