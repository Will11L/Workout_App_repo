# =================================================================================================================================================#
# Project Name : Power Meter Selector
# Main file : database_page.py
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
import styles_database_page as css_s      # to stylize the interface (Chrome)

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

# -------------------- App interface -------------------- #

class Interface:

    def __init__(self):
        pass
        # Instanciation of your database
        #self.db = db.create_database()          # Create a database

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
        
        def update_database(event, tabulator, table_name):

            try:
                print("Event : ", event)
                cell_row_index = event.row+1                     # Get the row index
                cell_column = event.column                       # Get the column name
                cell_old_value = event.old                       # Get the old value
                cell_new_value = event.value                     # Get the new value

                print("table_name : ", table_name)
                table = db.get_table_as_df(str(table_name))
                print('table :', table)
                print('len(product_table) :', len(table))
            
                if cell_row_index >= len(table):
                    print("Row index out of range")
                    pn.state.notifications.error(f"Row index out of range for table {table_name}")
                    return
                else:
                    print("Row index in range")

                # Update the database
                db.update_cell_in_table(table_name, cell_column, cell_row_index, cell_new_value)
            
            except Exception as e:
                print("Error in update_database : ", e)
                pn.state.notifications.error(f"Error in update_database : {e}")

            else:
                print(f"Cell ({cell_row_index}, {cell_column}) updated in table {table_name}")
                pn.state.notifications.success(f"Cell ({cell_row_index}, {cell_column}) updated in table {table_name}")
        
        def show_id_modal(event):
            modal_column = template.modal[0]

            if template.modal[0] is not None:
                template.modal[0].clear()
            if template.modal[1] is not None:
                template.modal[1].clear()

            sso = pn.state.sso if hasattr(pn.state, 'sso') else None

            modal_column.append(pn.pane.Markdown(f"## sso : {sso}", align="center", stylesheets=[common_css.stylesheet_markdown_modal]))
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
        
        (template, redirection_pane, 
            w_page_selector, id_button,
            w_settings_toggle, w_display_database_button, w_allow_drag_toggle,
            gridStack, tuple_of_tables_and_tabulators,
            list_of_Sidebar_widgets, list_of_Settings_widgets
            ) = self._build_interface()

        # ---------- Widgets Events ---------- #    
        # * ---------- Sidebar Widgets ---------- * #        
        for widget in list_of_Settings_widgets:
            widget.visible = False

        w_display_database_button.on_click(display_database_tables)
        w_settings_toggle.param.watch(display_settings, 'value')
        w_allow_drag_toggle.param.watch(allow_drag, 'value')
        id_button.on_click(show_id_modal)
        w_page_selector.param.watch(change_page, 'value')

        # * ---------- Main Widgets ---------- * #
        for table_name, tabulator in tuple_of_tables_and_tabulators:
            tabulator.on_edit(lambda event, tab=tabulator, name=table_name: update_database(event, tab, name))

        # callbacks
        #pn.state.add_periodic_callback(update_graphes, period=5000)

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

        #* ---------- Template ---------- *#
        
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
        
        template.modal.append(pn.Column(sizing_mode='stretch_width'))
        template.modal.append(pn.Column(sizing_mode='stretch_width'))

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

        #* ------------------------------- *#


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

        #*---------- Partie 1 : Display the tables of the database ----------*#

        gridStack = pn.GridStack(
            allow_resize=True,
            allow_drag=False,
            align="center",
            sizing_mode="stretch_both",
            stylesheets=[css_s.stylesheet_gridStack]
        )
        template.main.append(gridStack)

        tables_name = db.get_all_tables_names()
        number_of_tables = len(tables_name)
        print("Number of tables in the database :", number_of_tables)
        tuple_of_tables_and_tabulators = []
        row = 0
        col = 0
        for table in tables_name:
            table_df = db.get_table_as_df(table)
            table_df = table_df.drop(columns=['id'])
            column_to_add = pn.Column(
                pn.pane.Markdown(
                    f"{table}",
                    align="center",
                    stylesheets=[css_s.stylesheet_markdown_table]
                ),
                stylesheets=[css_s.stylesheet_column]
            )

            tabulator = pn.widgets.Tabulator(
                table_df,
                theme='site',
                header_align='center',
                text_align='center',
                align='center',
                show_index=False,
                layout="fit_columns",
                configuration={
                    'clipboard': True,
                    'columnDefaults': {
                        'headerSort': False,
                    },
                },
                stylesheets = [css_s.stylesheet_tabulator]
            )

            column_to_add.append(tabulator)

            if col >= 2:
                row += 1
                col = 0
            gridStack[row, col] = column_to_add
            tuple_of_tables_and_tabulators.append((table, tabulator))
            col += 1
        
        # ? --------------- Dashboard --------------- ? #
        # Return all widgets
        all_widgets = (
            template, redirection_pane,
            w_page_selector, id_button,
            w_settings_toggle, w_display_database_button, w_allow_drag_toggle,
            gridStack, tuple_of_tables_and_tabulators,
            list_of_Sidebar_widgets, list_of_Settings_widgets
            )
        return all_widgets
    

if __name__.startswith("bokeh"):    # start with panel serve script.py
    app = Interface()
    dashboard = app.display()
    dashboard.servable()
 
if __name__ == "__main__":  # start with python script.py
    app = Interface()
    dashboard = app.display()
    dashboard.show()        # Display the dashboard
    #dashboard.servable()   # Serve the dashboard