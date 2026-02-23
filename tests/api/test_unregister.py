def test_unregister_removes_student_from_activity_participants(client):
    # Arrange
    activity_name = "Chess Club"
    email = "remove.me@mergington.edu"
    client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Act
    response = client.delete(f"/activities/{activity_name}/participants", params={"email": email})
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in participants
