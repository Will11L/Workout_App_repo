import panel as pn
import app_database as db
import datetime

import common_css as common_css

def ping_user(instance, file_name=None):
    session_token = instance.session_token
    user_id = instance.user_id
    template = instance.template
    #print("session_token:", session_token)
    #print("user_id:", user_id)
    #print(f"template: {template}")

    """
    Met à jour la session utilisateur (last_activity + is_active) en interne.
    Appelée depuis chaque page Panel via un callback.
    """
    now = datetime.datetime.now()
    print(f"[ping_user] 🔁 Ping à {now.strftime('%Y-%m-%d %H:%M:%S')} - user_id={user_id}, session_token={session_token}")
    
    if user_id and session_token:
        #todo -> compute the remaining time before disconnection
        #todo -> display a countdown
        time_remaining = 30

        markdown1 = pn.pane.Markdown("Ping en cours...", align="center", stylesheets=[common_css.stylesheet_markdown_modal])
        markdown2 = pn.pane.Markdown("Are you still there ?", align="center", stylesheets=[common_css.stylesheet_markdown_modal])
        countdown_text = pn.pane.Markdown(f"⏱ You will be disconnected in **{time_remaining} seconds**", align="center", stylesheets=[common_css.stylesheet_markdown_modal])
        yes_button = pn.widgets.Button(name="Yes, I'm here", button_type="primary")
        no_button = pn.widgets.Button(name="No, disconnect me", button_type="danger")
        
        modal_column = template.modal[0]

        if template.modal[0] is not None:
            template.modal[0].clear()

        modal_column = template.modal[0]
        modal_column.append(markdown1)
        modal_column.append(markdown2)
        modal_column.append(countdown_text)
        modal_column.append(pn.Row(yes_button, no_button))

        # 🔁 Timer dynamique
        def update_countdown():
            nonlocal time_remaining
            time_remaining -= 1
            countdown_text.object = f"⏱ You will be disconnected in **{time_remaining} seconds**"
            if time_remaining <= 0:
                timer_callback.stop()
                print("[ping_user] 🔴 Timer expired, auto logout")
                # Appel déconnexion ici (à personnaliser)
                db.edit_row_with_conditions(
                    "users_sessions",
                    {"user_id": user_id, "session_token": session_token},
                    {"is_active": False}
                )
                #todo -> do a common redirection page or logout function
                instance.redirection_pane.object = "<script>window.location.href = 'http://localhost:8080/login_page';</script>"

        timer_callback = pn.state.add_periodic_callback(update_countdown, period=1000)

        # ✅ Bouton "Yes, I'm here" → reset last_activity and is_active
        def on_yes_click(event):
            print("[ping_user] ✅ User confirmed presence")
            timer_callback.stop()
            template.modal[0].clear()
            template.close_modal()
            db.edit_row_with_conditions(
                "users_sessions",
                {"user_id": user_id, "session_token": session_token},
                {"is_active": True, "last_activity": datetime.datetime.now()}
            )

        # ❌ Bouton "No, disconnect me"
        def on_no_click(event):
            print("[ping_user] ❌ User chose to disconnect")
            timer_callback.stop()
            template.modal[0].clear()
            template.close_modal()
            db.edit_row_with_conditions(
                "users_sessions",
                {"user_id": user_id, "session_token": session_token},
                {"is_active": False}, {"last_activity": datetime.datetime.now()}
            )
            #todo -> do a common redirection page or logout function
            instance.redirection_pane.object = "<script>window.location.href = 'http://localhost:8080/login_page';</script>"

        yes_button.on_click(on_yes_click)
        no_button.on_click(on_no_click)

        template.open_modal()

        #todo -> answer and then update the user_session

    else:
        print("[ping_user] ⚠ user_id or session_token missing")