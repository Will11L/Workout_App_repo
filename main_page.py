# =================================================================================================================================================#
# Project Name : Power Meter Selector
# Main file : main_page.py
# Description : This file contains the main class of the application, the interface class. It is used to create the interface of the application.
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
import common_css as common_css                     # To stylize the interface (Chrome)
import styles_main_page as css_s                    # to stylize the interface (Chrome)

import importlib                                    # To reload the modules
importlib.reload(db)                                # Reload the db module
importlib.reload(css_s)                             # Reload the css_s module

#?import pypdf                                        # To concatenate PDF files

#?import pythoncom                                    # To interact with other software

import datetime                                     # To get the current date
import math                                         # To use math functions

#?import check_user_token as cut                    # To check if a user is already trying to use an extern application or software
import threading                                    # To use threads

import warnings
warnings.filterwarnings("ignore", message="Specified region overlaps with the following existing object(s) in the grid")

import core.page_loader as pl
import core.ping_user as pu

# -------------------- App interface -------------------- #

class Interface:

    def __init__(self):
        
        file_name = os.path.basename(__file__)
        self.file_name = os.path.splitext(file_name)[0]
        self.session_token = None
        self.user_id = None
        self.redirection_pane = None
        self.template = None

        #* ---------- State ---------- *#
            
        pn.state.onload(self.on_load)
        #pn.state.on_session_destroyed(self.on_session_destroyed)
        
        #* ---------- callbacks ---------- *#

        # 300000 = 5 minutes
        # 1500000 = 25 minutes
        #todo -> do a common timer for all pages
        pn.state.add_periodic_callback(lambda: pu.ping_user(self, self.file_name), 300000)

        #* ---------- Database ---------- *#
        #? Nothing to do here
        #self.db = db.create_database()          # Create a database
    
    def on_load(self):

        #* ---------- Common loading part ---------- *#

        pl.on_page_load(self, self.file_name)

        #* ---------- Specific loading part ---------- *#
        #? Nothing to do here
    
    def on_session_destroyed(self, session_context):
        #! happens if the user closes the browser
        #! but if you go to another page, the session is destroyed too
        #!? if you refresh the page, the session is destroyed too
        #! so you can't use it to keep the user connected
        # only for database check
        pass

        #* ---------- Common session destroyed part ---------- *#

        #pe.on_exit(self, self.file_name)
        
        #* ---------- Specific session destroyed part ---------- *#
        #? Nothing to do here
        
    def display(self):

        def display_settings(event):
            Settings_toggle = event.obj
            if event.new:
                Settings_toggle.icon = 'eye'
                Settings_toggle.stylesheets = [css_s.stylesheet_on_sidebar_toggle]
            else:
                Settings_toggle.icon = 'eye-off'
                Settings_toggle.stylesheets = [css_s.stylesheet_off_sidebar_toggle]
            isVisible = event.new
            for widget in list_of_Settings_widgets:
                widget.visible = isVisible
        
        def allow_drag(event):
            allow_drag_toggle = event.obj
            if event.new:
                allow_drag_toggle.icon = 'lock-open'
                allow_drag_toggle.stylesheets = [css_s.stylesheet_on_sidebar_toggle]
                gridStack.allow_drag = True
            else:
                allow_drag_toggle.icon = 'lock'
                allow_drag_toggle.stylesheets = [css_s.stylesheet_off_sidebar_toggle]
                gridStack.allow_drag = False

        def display_database_tables(event):
            tables = db.get_all_tables_names()
            print("Tables in the database :", tables)
            for table in tables:
                if db.get_table_as_df(table).empty:
                    print(f"Table {table} is empty")
                else:
                    display(db.get_table_as_df(table))

        def show_id_modal(event):
            #! to be changed
            modal_column = template.modal[0]

            if template.modal[0] is not None:
                template.modal[0].clear()

            #! do not keep the following lines
            #user_id = pn.state.user_id if hasattr(pn.state, 'user_id') else None
            user_id = self.user_id

            modal_column.append(pn.pane.Markdown(f"## user_id : {user_id}", align="center", stylesheets=[common_css.stylesheet_markdown_modal]))
            modal_column.append(pn.pane.Markdown("This is the ID modal", align="center", stylesheets=[common_css.stylesheet_markdown_modal]))

            template.open_modal()

        def change_page(event):
            selected_page = event.obj.value
            if selected_page == 'Main page':
                redirection_pane.object = "<script>window.location.href = 'http://localhost:8080/main_page';</script>"
            elif selected_page == 'Database page':
                redirection_pane.object = "<script>window.location.href = 'http://localhost:8080/database_page';</script>"
            elif selected_page == 'Page 1':
                redirection_pane.object = "<script>window.location.href = 'http://localhost:8080/page1';</script>"
            elif selected_page == 'Page 2':
                redirection_pane.object = "<script>window.location.href = 'http://localhost:8080/page2';</script>"
            else:
                print("Error : Page not found")
        
        def update_database(event, tabulator, table):
            pass
        
        (template, redirection_pane, w_page_selector, id_button,
            w_settings_toggle, w_display_database_button, w_allow_drag_toggle,
            gridStack,
            list_of_Sidebar_widgets, list_of_Settings_widgets
            ) = self._build_interface()

        # ---------- Widgets Events ---------- #
        #todo to put at the good place    
        # * ---------- Sidebar Widgets ---------- * #        
        for widget in list_of_Settings_widgets:
            widget.visible = False

        self.redirection_pane = redirection_pane
        w_display_database_button.on_click(display_database_tables)
        w_settings_toggle.param.watch(display_settings, 'value')
        w_allow_drag_toggle.param.watch(allow_drag, 'value')
        #id_button.on_click(show_id_modal)
        w_page_selector.param.watch(change_page, 'value')

        def test_ping_user(event): #! to delete when it's good
            pu.ping_user(self, self.file_name)
        id_button.on_click(test_ping_user)
        # * ---------- Main Widgets ---------- * #


        return template

    def _build_interface(self):

        pn.extension('plotly')
        pn.extension('tabulator')
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
            raw_css = [common_css.template_css],
            theme_toggle = False,
            logo = "./files/images/gevernova_logo_white.png",
            favicon = "./files/images/gevernova_logo_white.png",
            busy_indicator = None,
            #meta_refresh = '10'               # Refresh the page every 10 seconds
        )
        self.template = template
        template.modal.show_close_button = False
        template.modal.append(pn.Column(sizing_mode='stretch_width'))
        template.header.sizing_mode = "stretch_width"
        

        # ---------- Header ---------- #

        #? ----------Widgets definition, create all of them here ---------- ?#       

        # ---------- Sidebar ---------- #

        # * ---------- Settings ---------- * #

        list_of_Settings_widgets = []

        w_settings_toggle = pn.widgets.Toggle(icon='eye-off', name='Display Settings', align="center", stylesheets=[css_s.stylesheet_off_sidebar_toggle])

        Settings_spacer = pn.Spacer(name='Settings_Spacer', height=20)
        list_of_Settings_widgets.append(Settings_spacer)

        w_allow_drag_toggle = pn.widgets.Toggle(icon='lock', name='Allow Drag', align="center", stylesheets=[css_s.stylesheet_off_sidebar_toggle])
        list_of_Settings_widgets.append(w_allow_drag_toggle)

        w_display_database_button = pn.widgets.Button(name='Display Database', stylesheets=[css_s.stylesheet_sidebar_button])
        list_of_Settings_widgets.append(w_display_database_button)

        # * ---------- Sidebar Widgets ---------- * #

        Sidebar_Title = pn.pane.Markdown("## Settings", align="center", stylesheets=[css_s.stylesheet_markdown_sidebar])
        template.sidebar.append(Sidebar_Title)

        list_of_Sidebar_widgets = []

        for element in list_of_Sidebar_widgets:
            template.sidebar.append(element)
        
        # * ---------- Sidebar Settings Appends ---------- * #

        template.sidebar.append(pn.Spacer(height=20))
        template.sidebar.append(pn.Spacer(height=20))
        template.sidebar.append(w_settings_toggle)
        template.sidebar.append(Settings_spacer)
        template.sidebar.append(w_display_database_button)
        template.sidebar.append(w_allow_drag_toggle)

        redirection_pane = pn.pane.HTML("")
        template.sidebar.append(redirection_pane)

        for element in template.sidebar:
            element.sizing_mode = "stretch_width"

        #? -------------------- Main -------------------- ?#

        #* ---------- Header ---------- *#

        header_select_width = 150
        w_page_selector = pn.widgets.Select(
            name='Select Page',
            options=['Select a page', 'Main page', 'Database page', 'Page 1', 'Page 2'],
            align="center",
            width=header_select_width,
            stylesheets=[common_css.stylesheet_page_selector]
        )
        w_page_selector2 = pn.widgets.Select(
            name='Select Page',
            options=['Main page', 'Database page', 'Page 1', 'Page 2'],
            align="center",
            width=header_select_width,
            stylesheets=[common_css.stylesheet_header_select]
        )
        w_button1 = pn.widgets.Button(
            name='Go to Page 1',
            stylesheets=[common_css.stylesheet_header_button]
        )
        w_button2 = pn.widgets.Button(name='Go to Page 2',
            stylesheets=[common_css.stylesheet_header_button]
        )

        id_button = pn.widgets.ButtonIcon(
            icon='info-small',
            active_icon='info-small',
            align="center",
            stylesheets=[common_css.stylesheet_id_button]
        )

        header_gridStack = pn.GridStack(
            nrows=1,
            allow_resize=False,
            allow_drag=False,
            align="center",
            sizing_mode="stretch_width",
            stylesheets=[common_css.stylesheet_header_gridStack]
        )

        header_gridStack[0, 0] = w_page_selector
        header_gridStack[0, 1] = w_page_selector2
        header_gridStack[0, 2] = w_button1
        header_gridStack[0, 3] = w_button2
        header_gridStack[0, 6] = id_button

        template.header.append(header_gridStack)

        #* ---------- Partie 1 : ----------*#

        gridStack = pn.GridStack(
            allow_resize=False,
            allow_drag=False,
            align="center",
            sizing_mode="stretch_both",
            stylesheets=[css_s.stylesheet_gridStack]
        )

        selector1 = pn.widgets.Select(name='Select 1', options=['Option 1', 'Option 2', 'Option 3'], align="center", stylesheets=[css_s.stylesheet_select])
        selector2 = pn.widgets.Select(name='Select 2', options=['Option 1', 'Option 2', 'Option 3'], align="center")
        TextInput1 = pn.widgets.TextInput(name='Text Input 1', align="center")
        TextInput2 = pn.widgets.TextInput(name='Text Input 2', align="center")
        column_1 = pn.Column(
            pn.pane.Markdown("## Partie 1", align="center", dedent=True, stylesheets=[css_s.stylesheet_markdown_main]),
            selector1,
            selector2,
            TextInput1,
            TextInput2,
            align="center",
            sizing_mode="stretch_width",
            stylesheets=[css_s.stylesheet_column]
        )

        column_2 = pn.Column(
            pn.pane.Markdown("## Partie 2", align="center", stylesheets=[css_s.stylesheet_markdown_main]),
            align="center",
            sizing_mode="stretch_width",
            stylesheets=[css_s.stylesheet_column]
        )
        
        column_3 = pn.Column(
            pn.pane.Markdown("## Partie 3", align="center", stylesheets=[css_s.stylesheet_markdown_main]),
            align="center",
            sizing_mode="stretch_width",
            stylesheets=[css_s.stylesheet_column]
        )

        gridStack[ : , 0:3 ] = column_1
        gridStack[ 0:2 , 3:6 ] = column_2
        gridStack[ 2:4 , 3:6 ] = column_3

        template.main.append(column_1)
        template.main.append(gridStack)
        template.main.append(column_2)

        
        # ? --------------- Dashboard --------------- ? #
        # Return all widgets
        all_widgets = (
            template, redirection_pane, w_page_selector, id_button,
            w_settings_toggle, w_display_database_button, w_allow_drag_toggle,
            gridStack,
            list_of_Sidebar_widgets, list_of_Settings_widgets
            )
        return all_widgets
    

if __name__.startswith("bokeh"):    # start with panel serve script.py
    app = Interface()
    dashboard = app.display()
    dashboard.servable()
 
if __name__ == "__main__":          # start with python script.py
    app = Interface()
    dashboard = app.display()
    dashboard.show()                # Display the dashboard
    #dashboard.servable()           # Serve the dashboard