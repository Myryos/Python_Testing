import pytest
from bs4 import BeautifulSoup


@pytest.mark.parametrize(
    "clubs, expected_order",
    [
        (
            [
                {
                    "name": "Eternal Champions",
                    "email": "champions@eternal.com",
                    "points": 25,
                },
                {
                    "name": "Strikers United",
                    "email": "contact@strikers_united.com",
                    "points": 50,
                },
                {
                    "name": "Galactic Titans",
                    "email": "contact@galatic_titans.com",
                    "points": 35,
                },
                {
                    "name": "Gundam United",
                    "email": "contact@gundam_united.com",
                    "points": 6,
                },
                {
                    "name": "Cosmic Vanguard",
                    "email": "contact@cosmic_vanguard.com",
                    "points": 15,
                },
            ],
            [
                "Strikers United",
                "Galactic Titans",
                "Eternal Champions",
                "Cosmic Vanguard",
                "Gundam United",
            ],
        ),
        ([], []),
    ],
)
def test_leaderboard_sorting(client, mocker, clubs, expected_order):

    mocker.patch("server.clubs", clubs)
    response = client.get("/leaderboard")
    assert response.status_code == 200
    data = response.data.decode("utf-8")
    soup = BeautifulSoup(data, "html.parser")
    order_response = [
        tr.get_text().strip("\n").split("\n")[0] for tr in soup.find_all("tr")
    ]
    assert expected_order == order_response[1:]
