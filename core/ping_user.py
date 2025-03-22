from numpy import append
import panel as pn

import app_database as db
import datetime

from styles import common_css as common_css

import core.page_redirection as pr

def ping_user(instance, file_name=None):
    """
    Update the last_activity field in the users_sessions table
    Callable by each page to update the last_activity field in the users_sessions table
    """

    session_token = instance.session_token
    user_id = instance.user_id
    now = datetime.datetime.now()

    print(f"[ping_user] 🔁 Ping à {now.strftime('%Y-%m-%d %H:%M:%S')} - user_id={user_id}, session_token={session_token}")
    
    if user_id and session_token:
        #TODO -> compute the remaining time before disconnection = countdown
        time_remaining = 30

        markdown1 = pn.pane.Markdown("Ping en cours...", align="center", stylesheets=[common_css.stylesheet_markdown_modal])
        markdown2 = pn.pane.Markdown("Are you still there ?", align="center", stylesheets=[common_css.stylesheet_markdown_modal])
        countdown_text = pn.pane.Markdown(f"⏱ You will be disconnected in **{time_remaining} seconds**", align="center", stylesheets=[common_css.stylesheet_markdown_modal])
        yes_button = pn.widgets.Button(name="Yes, I'm here", button_type="primary")
        no_button = pn.widgets.Button(name="No, disconnect me", button_type="danger")

        column_of_modal = instance.modal[0]

        """
        modal_content = pn.Column(
            pn.pane.Markdown("🔁 Ping en cours...", sizing_mode="stretch_width"),
            pn.pane.Markdown("⚠ Are you still there ?", sizing_mode="stretch_width"),
            countdown_text,
            pn.Row(yes_button, no_button),
            sizing_mode="stretch_width"
        )
        """

        column_of_modal.clear()
        column_of_modal.append(markdown1)
        column_of_modal.append(markdown2)
        column_of_modal.append(countdown_text)
        column_of_modal.append(pn.Row(yes_button, no_button))

        # 🔁 Dynamic Timer
        def update_countdown():
            nonlocal time_remaining
            time_remaining -= 1
            countdown_text.object = f"⏱ You will be disconnected in **{time_remaining} seconds**"
            if time_remaining <= 0:
                timer_callback.stop()
                print("[ping_user] 🔴 Timer expired, auto logout")
                db.edit_row_with_conditions(
                    "users_sessions",
                    {"user_id": user_id, "session_token": session_token},
                    {"is_active": False}
                )
                pr.redirection_to_login_page()

        timer_callback = pn.state.add_periodic_callback(update_countdown, period=1000)

        # ✅ Bouton "Yes, I'm here" → reset last_activity and is_active
        def on_yes_click(event):
            print("[ping_user] ✅ User confirmed presence")
            timer_callback.stop()
            column_of_modal.clear().clear()
            instance.modal.open = False
            db.edit_row_with_conditions(
                "users_sessions",
                {"user_id": user_id, "session_token": session_token},
                {"is_active": True, "last_activity": datetime.datetime.now()}
            )

        # ❌ Bouton "No, disconnect me"
        def on_no_click(event):
            print("[ping_user] ❌ User chose to disconnect")
            timer_callback.stop()
            column_of_modal.clear().clear()
            instance.modal.open = False
            db.edit_row_with_conditions(
                "users_sessions",
                {"user_id": user_id, "session_token": session_token},
                {"is_active": False, "last_activity": datetime.datetime.now()}
            )
            pr.redirection_to_login_page()

        yes_button.on_click(on_yes_click)
        no_button.on_click(on_no_click)
        
        instance.modal.open = True

        #TODO -> answer and then update the user_session

    else:
        print("[ping_user] ⚠ user_id or session_token missing")