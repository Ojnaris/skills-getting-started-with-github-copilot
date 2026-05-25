from src.app import activities


def test_signup_adds_participant(client):
    # Arrange
    email = "new.student@mergington.edu"

    # Act
    response = client.post("/activities/Chess Club/signup", params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload == {"message": f"Signed up {email} for Chess Club"}
    assert email in activities["Chess Club"]["participants"]


def test_signup_rejects_duplicate_participant(client):
    # Arrange
    existing_email = activities["Chess Club"]["participants"][0]

    # Act
    response = client.post("/activities/Chess Club/signup", params={"email": existing_email})
    payload = response.json()

    # Assert
    assert response.status_code == 400
    assert payload == {"detail": "Student already signed up"}


def test_signup_unknown_activity_returns_404(client):
    # Arrange
    email = "student@mergington.edu"

    # Act
    response = client.post(
        "/activities/Unknown Activity/signup",
        params={"email": email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {"detail": "Activity not found"}
