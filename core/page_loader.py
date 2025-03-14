import panel as pn
import app_database as db
import datetime

def on_page_load(instance, file_name=None):
    instance.session_token = pn.state.location.query_params.get("session_token", None)
    instance.user_id = pn.state.location.query_params.get("user_id", None)

    session_token = instance.session_token
    user_id = instance.user_id
    print("session_token:", session_token)
    print("user_id:", user_id)

    if pn.state.location.query_params.get("user_id", None) is not None:
        print(f"{file_name} - user_id is :", instance.session_token)
    else:
        print(f"{file_name} - No user_id found : ", instance.user_id)
    
    print(f"🚀 {file_name or instance.__class__.__name__} is loaded")

    if session_token is not None:
        print(f"{file_name} - session_token is :", session_token)
        # Check if user in database, in session , isActive, etc
        users_sessions = db.get_table_as_df("users_sessions")
        user_session = users_sessions[
            (users_sessions["user_id"] == user_id)
            & (users_sessions["session_token"] == session_token)
        ]
        if user_session.empty:
            print(f"{file_name} - User session of {user_id} empty")
            instance.redirection_pane.object = "<script>window.location.href = 'http://localhost:8080/login_page';</script>"
        else:
            print(f"{file_name} - User session of {user_id} found")
            db.edit_row_with_conditions(
                "users_sessions",
                {"user_id": user_id, "session_token": session_token},
                {"is_active": True, "last_activity": datetime.datetime.now()},
            )
    else:
        print(f"{file_name} - No session_token found")
        instance.redirection_pane.object = "<script>window.location.href = 'http://localhost:8080/login_page';</script>"