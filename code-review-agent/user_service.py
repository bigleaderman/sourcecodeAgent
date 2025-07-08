def validate_user(user_data):
    if not user_data.get("email"):
        raise ValueError("Email is required")
    if "@" not in user_data["email"]:
        raise ValueError("Invalid email format")
    return True


def get_user_by_id(user_id):
    # 실제 DB 호출 대신 테스트용 딕셔너리 사용
    mock_db = {
        1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
        2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
    }
    return mock_db.get(user_id)


if __name__ == "__main__":
    user = get_user_by_id(1)
    print("User:", user)
    validate_user(user)
