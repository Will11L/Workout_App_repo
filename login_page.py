# =================================================================================================================================================#
# Project Name : Power Meter Selector
# Main file : Home_page.py
# Description : To be defined
# Author : LEHNERT William
# Creation Date : 5 March 2025
# =================================================================================================================================================#

# =================================================================================================================================================#
# This source code and the related information are the property of William Lehnert.
# Any reproduction, distribution, modification, or unauthorized use of this code or the related information is
# strictly prohibited without the prior written consent of William Lehnert."
# =================================================================================================================================================#

import re                                           # Regex to find patterns in strings
import pandas as pd                                 # To manipulate dataframes

import numpy as np                                  # To manipulate arrays
#?import win32com.client                              # To interact with other software
import os                                           # To interact with the operating system (create folders, move files, etc.)
import sys
import shutil                                       # To move files

import time                                         # To use time.sleep() function
from datetime import datetime                       # To get the current date
import random                                       # To generate random numbers

import panel as pn                                  # To create the interface with the widgets
import bokeh as bk                                  # To create the interface with the widgets
import ipywidgets as wd                             # To create the interface with the widgets
from IPython.display import display                 # To display the widgets

import sqlite3                                      # To create a database
import app_database as db                           # To interact with the database (create tables, add elements, etc.)


#?import Interface_FrontEnd_styles_firefox as css_s   # To stylize the interface (Firefox)
from styles import common_css as common_css                     # To stylize the interface (Chrome)
from styles import styles_login_page as css_s                   # to stylize the interface (Chrome)

import importlib                                    # To reload the modules
#importlib.reload(db)                                # Reload the db module
#importlib.reload(css_s)                             # Reload the css_s module

#?import pypdf                                        # To concatenate PDF files

#?import pythoncom                                    # To interact with other software

import datetime                                     # To get the current date
import math                                         # To use math functions

#?import check_user_token as cut                    # To check if a user is already trying to use an extern application or software
import threading                                    # To use threads

import warnings
warnings.filterwarnings("ignore", message="Specified region overlaps with the following existing object(s) in the grid")

import uuid

# -------------------- Modules and external files -------------------- #

import core.page_redirection as pr
import core.page_loader as pl

import core.ping_user as pu

# =================================================================================================================================================#

# -------------------- App interface -------------------- #

class Login:

    def __init__(self):
        pass
        # Instanciation of your database
        #self.db = db.create_database()          # Create a database
 
    def display(self):
        
        def check_login(event):
            sso = str(sso_TextInput.value)
            password = str(password_TextInput.value)

            try:
                users = db.get_table_as_df('users')
                user_match = users[users['SSO_id'].astype(str) == sso]

                if user_match.empty:
                    pn.state.notifications.error("SSO / User not found", duration=2000)
                    sso_TextInput.value = "Enter a valid login"
                    sso_TextInput.stylesheets = [css_s.stylesheet_TextInput_error]

                elif password != user_match['password'].values[0]:
                    pn.state.notifications.error("Wrong password", duration=2000)
                    password_TextInput.value = ""
                    #TODO : change style of the password input when error
                    password_TextInput.stylesheets = [css_s.stylesheet_TextInput_error]

                else:
                    # Update the user_sessions table
                    sso = sso_TextInput.value
                    session_token = str(uuid.uuid4())  # Token unique pour cette session
                    is_active = True
                    session_start = datetime.datetime.now()
                    last_activity = None

                    try:
                        users_sessions = db.get_table_as_df('users_sessions')
                        user_session = users_sessions[
                            (users_sessions['user_id'] == sso) & (users_sessions['session_token'] == session_token)
                        ]
                        if user_session.empty:
                            db.add_element_to_table('users_sessions', (sso, session_token, is_active, session_start, last_activity))
                        else:
                            db.edit_row_with_conditions('users_sessions', {'is_active': True, 'session_start': session_start}, {'user_id': sso, 'session_token': session_token})
                    except Exception as e:
                        print("Error while updating user_sessions table:", e)
                        pn.state.notifications.error("Error while updating user_sessions table", duration=2000)
                    else:
                        # Redirection only if successful login
                        
                        pn.state.notifications.success("Login successful", duration=2000)

                        time.sleep(1)
                        pr.redirection_to_url_with_token_and_user_id(pr.main_page_path, session_token, sso)
                            

            except Exception as e:
                print("Error while checking login:", e)
                pn.state.notifications.error("Error while checking login", duration=2000)

            else:
                print("✅ Login process completed.")

        def update_database(event, tabulator, table):
            pass
        
        (template,
            sso_TextInput, password_TextInput, login_button,
            ) = self._build_interface()

        # ---------- Widgets Events ---------- #

        # * ---------- Sidebar Widgets ---------- * #        
        
        # Nothing here

        # * ---------- Main Widgets ---------- * #

        # Watchers
        login_button.on_click(check_login)
        sso_TextInput.param.watch(lambda event: check_login(event), 'enter_pressed')
        password_TextInput.param.watch(lambda event: check_login(event), 'value')

        # Callbacks
        #pn.state.add_periodic_callback(update_graphes, period=5000)

        return template

    def _build_interface(self):

        pn.extension('gridstack')
        
        #pn.extension(design = 'material', global_css = [':root { --design-primary-color: #41B06E; }'])
        #pn.extension(design = 'material', global_css = [':root { --design-primary-color: blue; }']) #! revoir cette ligne

        pn.extension(design = 'material') #! revoir cette ligne
        pn.extension(notifications=True)
        #? Available design systems include: ['design', 'bootstrap', 'fast', 'material', 'native'].
        # Réinitialiser la configuration CSS de Panel pour qu'elle ne contienne aucun fichier CSS externe
        #! important car sinon il y a des problèmes de chargement de CSS
        pn.config.raw_css = []
        #pn.config.raw_css.append(css)  #! Deprecated ! -> use stylesheets instead

        #pn.extension(design = 'design', global_css = [f":root {{ --design-primary-color: {evergreen}; }}"])
        #! vérifier si il n'y a pas un résidu de l'extension enregistrée       

        # ---------- Template ---------- #
        
        template = pn.template.FastListTemplate(
            title='GE VERNOVA',
            main_layout = None,                          # Default is 'card', accept [None, 'card']
            collapsed_sidebar = True,                     # Default is False
            header = None,                                # Default is 'default'
            raw_css = [common_css.template_css, css_s.login_template_css],
            logo = "./files/images/gevernova_logo_white.png",
            favicon = "./files/images/gevernova_logo_white.png",
            theme_toggle = False,
            busy_indicator = None
            #meta_refresh = '10'               # Refresh the page every 10 seconds
        )
        template.header.allow_None=True

        # ---------- Header ---------- #

        template.modal.append(pn.Column(sizing_mode='stretch_width'))
        template.modal.append(pn.Column(sizing_mode='stretch_width'))

        #? ---------- Widgets definition, create all of them here ---------- ?#       

        # ---------- Sidebar ---------- #

        # * ---------- Settings ---------- * #

        #? -------------------- Main -------------------- ?#

        #*---------- Partie 1 : Login ----------*#

        gridStack = pn.GridStack(
            allow_resize=False,
            allow_drag=False,
            align="center",
            sizing_mode="stretch_both",
            stylesheets=[css_s.stylesheet_gridStack]
        )

        language_selector = pn.widgets.Select(
            name='Select your language',
            options=['English', 'French', 'Spanish'],
            value='English',
            align='start',
            sizing_mode='stretch_width',
            stylesheets = [css_s.stylesheet_language_selector]
        )
        
        markdown_login = pn.pane.Markdown(
            "###### Please Log in",
            align='start',
            sizing_mode='stretch_width',
            stylesheets = [css_s.stylesheet_markdown_login]
        )

        sso_TextInput = pn.widgets.TextInput(
            name='Login',
            placeholder='Enter your SSO',
            value='',
            align='start',
            sizing_mode='stretch_width',
            stylesheets = [css_s.stylesheet_TextInput]
        )

        password_TextInput = pn.widgets.PasswordInput(
            name='Password',
            placeholder='Enter your password',
            value='',
            align='start',
            sizing_mode='stretch_width',
            stylesheets = [css_s.stylesheet_TextInput]
        )
        forgot_password_button = pn.widgets.Button(
            name="Forgot password",
            align='start',
            stylesheets = [css_s.stylesheet_forgot_button]
        )
        login_button = pn.widgets.Button(
            name='Log in',
            align='start',
            stylesheets = [css_s.stylesheet_login_button]
        )

        column= pn.Column(
            language_selector,
            markdown_login,
            sso_TextInput,
            password_TextInput,
            forgot_password_button,
            login_button,
            stylesheets = [css_s.stylesheet_column]
        )

        login_image = pn.pane.Image(
            object="./files/images/login_image.jpg",
            stylesheets = [css_s.stylesheet_login_image]
        )

        cloud = common_css.cloud
        
        nrows = 7
        ncols = 5
        #? Row 1 → Top margin
        gridStack[0:1 , :] = pn.Spacer(height=50, styles=dict(background=cloud))

        #? Row 2 → Center row
        gridStack[1:nrows , 0] = pn.Spacer(width=50, styles=dict(background=cloud))
        
        col_login_image = 0
        end_col = 0
        if ncols % 2 != 0:
            ncols += 1

        col_login_image = int(ncols / 2)
        end_col = ncols - 1
        col_form = col_login_image

        gridStack[1:nrows , 1:col_login_image] = login_image
        gridStack[1:nrows , col_form:end_col] = column

        gridStack[1:nrows , ncols-1] = pn.Spacer(width=50, styles=dict(background=cloud))

        #? Row 3 → Bottom margin
        gridStack[nrows , :] = pn.Spacer(height=50, styles=dict(background=cloud))
        
        template.main.append(gridStack)
        
        # ? --------------- Dashboard --------------- ? #
        # Return all widgets
        all_widgets = (
            template,
            sso_TextInput, password_TextInput, login_button,
            )
        return all_widgets
    

if __name__.startswith("bokeh"):
    # start with panel serve script.py
    app = Login()
    dashboard = app.display()
    dashboard.servable()
 
if __name__ == "__main__":
    # start with python script.py
    app = Login()
    dashboard = app.display()
    dashboard.show()
    #dashboard.servable()