import pytest


@pytest.mark.parametrize(
    "requester_club, expected_status_code",
    [
        (
            [
                {
                    "name": "Simply Lift 2",
                    "email": "john@simplylifttwo.co",
                    "points": "4",
                }
            ],
            200,
        ),
        (
            [
                {
                    "name": "Association Solidarite",
                    "email": "contact@association-solidarite.org",
                    "points": 12,
                }
            ],
            200,
        ),
    ],
)
def test_showSummary(client, mocker, requester_club, expected_status_code):

    mocker.patch("server.clubs", requester_club)

    response = client.post("/showSummary", data={"email": requester_club[0]["email"]})
    assert response.status_code == expected_status_code


def test_showSummary_fail(client):

    response = client.post("/showSummary", data={"email": "contact@iron_gauntlet.co"})

    assert response.status_code == 400
