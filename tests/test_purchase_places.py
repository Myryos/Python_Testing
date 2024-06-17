import pytest
from freezegun import freeze_time


@pytest.mark.parametrize(
    "competition_requested, requester_club, places_requested, status_code, expected_message, expected_remaining_places, expected_remaining_points",
    [
        (
            [
                {
                    "name": "Summer Cup",
                    "date": "2024-08-01 10:00:00",
                    "numberOfPlaces": 20,
                }
            ],
            [
                {
                    "name": "Strikers United",
                    "email": "contact@strikers_united.com",
                    "points": 50,
                }
            ],
            "12",
            200,
            b"Great booking complete! 12 purchased!",
            8,
            38,
        ),
        (
            [
                {
                    "name": "Fantasy League",
                    "date": "2024-08-10 10:00:00",
                    "numberOfPlaces": 15,
                }
            ],
            [
                {
                    "name": "Galactic Titans",
                    "email": "contact@galatic_titans.com",
                    "points": 35,
                }
            ],
            "20",
            400,
            b"Error : Too many places requested",
            15,
            35,
        ),
        (
            [
                {
                    "name": "Winter Games",
                    "date": "2024-08-15 10:00:00",
                    "numberOfPlaces": 8,
                }
            ],
            [
                {
                    "name": "Eternal Champions",
                    "email": "champions@eternal.com",
                    "points": 25,
                }
            ],
            "3",
            200,
            b"Great booking complete! 3 purchased!",
            5,
            22,
        ),
        (
            [{"name": "Space Cup", "date": "2024-08-20 10:00:00", "numberOfPlaces": 4}],
            [
                {
                    "name": "Cosmic Vanguard",
                    "email": "contact@cosmic_vanguard.com",
                    "points": 15,
                }
            ],
            "5",
            400,
            b"Error: Not enough places!",
            4,
            15,
        ),
        (
            [
                {
                    "name": "Summer Cup 2",
                    "date": "2024-02-25 10:00:00",
                    "numberOfPlaces": 8,
                }
            ],
            [
                {
                    "name": "Gundam United",
                    "email": "contact@gundam_united.com",
                    "points": 6,
                }
            ],
            "8",
            400,
            b"Error: Competition is in the past.",
            8,
            6,
        ),
    ],
)
@freeze_time("2024-05-25 14:00:00")
def test_purchase_places(
    client,
    mocker,
    requester_club,
    competition_requested,
    places_requested,
    status_code,
    expected_message,
    expected_remaining_points,
    expected_remaining_places,
):

    mocker.patch("server.competitions", competition_requested)
    mocker.patch("server.clubs", requester_club)

    print(requester_club[0]["name"])
    response = client.post(
        "/purchasePlaces",
        data={
            "club": requester_club[0]["name"],
            "competition": competition_requested[0]["name"],
            "places": places_requested,
        },
    )

    assert response.status_code == status_code
    assert expected_message in response.data
    assert int(requester_club[0]["points"]) == expected_remaining_points
    assert int(competition_requested[0]["numberOfPlaces"]) == expected_remaining_places


@freeze_time("2024-05-25 14:00:00")
def test_purchase_places_404(client):

    response = client.post(
        "/purchasePlaces",
        data={"competition": "Winter Cup", "club": "Gundam United", "places": "5"},
    )

    assert response.status_code == 404
    assert b"ERROR: No matching club or matching competition" in response.data
