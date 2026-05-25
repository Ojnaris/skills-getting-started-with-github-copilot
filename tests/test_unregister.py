from src.app import activities


def test_unregister_removes_participant(client):
    # Arrange
    email = activities["Chess Club"]["participants"][0]

    # Act
    response = client.delete("/activities/Chess Club/participants", params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload == {"message": f"Unregistered {email} from Chess Club"}
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        "/activities/Unknown Activity/participants",
        params={"email": email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {"detail": "Activity not found"}


def test_unregister_unknown_participant_returns_404(client):
    # Arrange
    email = "not.signed.up@mergington.edu"

    # Act
    response = client.delete(
        "/activities/Chess Club/participants",
        params={"email": email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {"detail": "Participant not found in this activity"}
