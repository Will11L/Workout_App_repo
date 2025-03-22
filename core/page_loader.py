import panel as pn
import app_database as db
import datetime

import core.page_redirection as pr

def on_page_load(instance, file_name=None):
    instance.session_token = pn.state.location.query_params.get("session_token", None)
    instance.user_id = pn.state.location.query_params.get("user_id", None)

    session_token = instance.session_token
    user_id = instance.user_id

    if pn.state.location.query_params.get("user_id", None) is not None:
        print(f"{file_name} - user_id is :", instance.user_id)
    else:
        print(f"{file_name} - No user_id found : ", instance.user_id)

    if pn.state.location.query_params.get("session_token", None) is not None:
        print(f"{file_name} - session_token is :", instance.session_token)
    else:
        print(f"{file_name} - No session_token found : ", instance.session_token)
    
    print(f"🚀 {file_name or instance.__class__.__name__} is loaded")

    if session_token:
        users_sessions = db.get_table_as_df("users_sessions")

        user_exists = users_sessions[users_sessions["user_id"] == user_id]

        if user_exists.empty:
            print(f"{file_name} ❌ - User '{user_id}' not found in users_sessions table.")
            pr.redirection_to_login_page()

        else:
            valid_session = user_exists[user_exists["session_token"] == session_token]
            if valid_session.empty:
                print(f"{file_name} ❌ - User '{user_id}' found but session_token is invalid or expired.")
                pr.redirection_to_login_page()
            else:
                print(f"{file_name} ✅ - Valid session found for user '{user_id}'")
                db.edit_row_with_conditions(
                    "users_sessions",
                    {"user_id": user_id, "session_token": session_token},
                    {"is_active": True, "last_activity": datetime.datetime.now()},
                )
    else:
        print(f"{file_name} ❌ - No session_token provided in URL")
        pr.redirection_to_login_page()