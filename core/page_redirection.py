import panel as pn

login_page_path = "/login_page"
main_page_path = "/main_page"
database_page_path = "/database_page"
page_1_path = "/page1"
page_2_path = "/page2"

page_not_found_path = "/not_found"

def redirection_to_url(url):
    pn.state.location.pathname = url
    pn.state.location.reload = True

def redirection_to_url_with_token_and_user_id(url, token, user_id):
    token = str(token)
    user_id = str(user_id)
    full_url = url + f"?session_token={token}&user_id={user_id}"
    print(f"🔄 Redirecting to: {full_url}")
    pn.state.location.pathname = full_url
    pn.state.location.reload = True

def redirection_to_login_page():
    pn.state.location.search = ""           # Clear query parameters
    redirection_to_url(login_page_path)     # Redirect to login page
def redirection_to_main_page():
    redirection_to_url(main_page_path)
def redirection_to_database_page():
    redirection_to_url(database_page_path)
def redirection_to_page1():
    redirection_to_url(page_1_path)
def redirection_to_page2():
    redirection_to_url(page_2_path)


def change_page(instance, event):
        selected_page = event.obj.value
        page_path_mapping = {
            'Main page': main_page_path,
            'Database page': database_page_path,
            'Page 1': page_1_path,
            'Page 2': page_2_path,
        }
        page_path = page_path_mapping.get(selected_page)

        if page_path:
            print(f"[change_page] 🔄 Changing page to: {page_path}")

            page_path = page_path.replace(" ", "_").lower() if page_path else None
            url = page_path
            pn.state.location.pathname = url
            pn.state.location.reload = True
        else:
            print(f"[change_page] 🚫 Page not found: {selected_page}")
            pn.state.location.pathname = page_not_found_path
