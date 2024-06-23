import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_index_page(browser, live_server):
    browser.get("http://127.0.0.1:5000/")
    assert "GUDLFT Registration" in browser.title


def test_show_summary(browser):
    # Access the home page
    browser.get("http://127.0.0.1:5000/")

    # Find the email input and submit it
    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("admin@irontemple.com")
    submit_button = browser.find_element(By.ID, "submit-email-button")
    submit_button.click()
    time.sleep(2)  # Wait for the page to load

    # Assert that the welcome page is displayed
    assert "Welcome" in browser.page_source


def test_booking_page(browser):
    browser.get("http://127.0.0.1:5000/")

    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("admin@irontemple.com")

    book_link = browser.find_element(By.ID, "submit-email-button")
    book_link.click()

    assert "Welcome" in browser.page_source

    competition_name = "Fall Classic"  # Remplacez par l'ID réel de votre compétition
    xpath_expression = f"//h4[contains(text(), '{competition_name}')]"

    # Trouver l'élément <h4> qui a cet ID
    comp_h4 = browser.find_element(By.XPATH, xpath_expression)
    # Trouver le bouton "Book Places" qui est un enfant de l'élément <h4>
    book_button = comp_h4.find_element(
        By.XPATH, "./following-sibling::a[contains(@class, 'btn-success')]"
    )

    # Cliquer sur le bouton "Book Places"
    book_button.click()
    time.sleep(2)  # Wait for the page to load

    # Assert that the booking page is displayed
    assert "Booking for" in browser.page_source


def test_purchase_places(browser):
    browser.get("http://127.0.0.1:5000/book/Spring%20Festival/Iron%20Temple")

    places_input = browser.find_element(By.NAME, "places")
    places_input.send_keys("1")
    submit_button = browser.find_element(By.ID, "booking_button")
    submit_button.click()

    assert "Great booking complete!" in browser.page_source


def test_integration_selenium(browser):
    # Access the home page
    browser.get("http://127.0.0.1:5000/")

    # Find the email input and submit it
    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("admin@irontemple.com")
    submit_button = browser.find_element(By.ID, "submit-email-button")
    submit_button.click()
    time.sleep(2)  # Wait for the page to load

    # Assert that the welcome page is displayed
    assert "Welcome" in browser.page_source

    competition_name = "Fall Classic"  # Remplacez par l'ID réel de votre compétition
    xpath_expression = f"//h4[contains(text(), '{competition_name}')]"

    # Trouver l'élément <h4> qui a cet ID
    comp_h4 = browser.find_element(By.XPATH, xpath_expression)

    # Trouver le bouton "Book Places" qui est un enfant de l'élément <h4>
    book_button = comp_h4.find_element(
        By.XPATH, "./following-sibling::a[contains(@class, 'btn-success')]"
    )

    # Cliquer sur le bouton "Book Places"
    book_button.click()
    time.sleep(2)  # Wait for the page to load

    # Assert that the booking page is displayed
    assert "Booking for" in browser.page_source

    # Find the places input, enter the number of places, and submit the form
    places_input = browser.find_element(By.NAME, "places")
    places_input.send_keys("1")
    submit_button = browser.find_element(By.ID, "booking_button")
    submit_button.click()
    time.sleep(2)  # Wait for the page to load

    # Assert that the booking was successful
    assert "Great booking complete!" in browser.page_source

    # Access the leaderboard
    leaderboard_link = browser.find_element(By.ID, "leaderboard_btn")
    leaderboard_link.click()
    time.sleep(2)  # Wait for the page to load

    # Assert that the leaderboard is displayed
    assert "Leaderboard" in browser.page_source

    # Go back to the welcome page
    browser.back()
    time.sleep(2)  # Wait for the page to load

    # Assert that the welcome page is displayed
    assert "Welcome" in browser.page_source

    # Logout
    logout_link = browser.find_element(By.ID, "logout_btn")
    logout_link.click()
    time.sleep(2)  # Wait for the page to load

    # Assert that the index page is displayed
    assert "Welcome to the GUDLFT Registration Portal!" in browser.page_source
