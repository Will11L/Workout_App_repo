from common_css import *

#? ---------- Sidebar Widgets CSS Styles ---------- ? #

stylesheet_on_sidebar_toggle = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    /*border: 2px solid {red} !important;*/
    border-radius: 0px !important;
}}

:host(.solid) .bk-btn.bk-btn-default {{
    background-color: {white} !important;
    color: {other_dark_blue_2} !important;
    font-family: Arial, sans-serif !important;
    font-size: {sidebar_widget_height}px !important;
    font-weight: bold !important;
    padding: 10px 20px 10px !important;
    transition: background-color 0s ease;
}}

:host(.solid) .bk-btn.bk-btn-primary {{
    background-color: {third_dark_blue} !important;
    color: {green} !important;
    font-family: Arial, sans-serif !important;
    font-size: {sidebar_widget_height}px !important;
    font-weight: bold !important;
    padding: 10px 20px 10px !important;
    transition: background-color 0s ease;
}}
"""

stylesheet_off_sidebar_toggle = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    /*border: 2px solid {alert_2} !important;*/
    border-radius: 0px !important;
}}

:host(.solid) .bk-btn.bk-btn-default {{
    background-color: {other_dark_blue_2} !important;
    color: {white} !important;
    font-family: Arial, sans-serif !important;
    font-size: {sidebar_widget_height}px !important;
    font-weight: bold !important;
    padding: 10px 20px 10px !important;
    transition: background-color 0s ease;
}}

:host(.solid) .bk-btn.bk-btn-primary {{
    background-color: {third_dark_blue} !important;
    color: {red} !important;
    font-family: Arial, sans-serif !important;
    font-size: {sidebar_widget_height}px !important;
    font-weight: bold !important;
    padding: 10px 20px 10px !important;
    transition: background-color 0s ease;
}}
"""


stylesheet_sidebar_button = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    /*border: 2px solid {alert_2} !important;*/
    border-radius: 0px !important;
}}

:host(.solid) .bk-btn.bk-btn-default {{
    background-color: {third_dark_blue} !important;
    color: {white} !important;
    font-family: Arial, sans-serif !important;
    font-size: {sidebar_widget_height}px !important;
    font-weight: bold !important;
    padding: 10px 20px 10px !important;
    transition: background-color 0s ease;
}}

:host(.solid) .bk-btn.bk-btn-primary {{
    background-color: {third_dark_blue} !important;
    color: {white} !important;
    font-family: Arial, sans-serif !important;
    font-size: {sidebar_widget_height}px !important;
    font-weight: bold !important;
    padding: 10px 20px 10px !important;
    transition: background-color 0s ease;
}}
"""

stylesheet_markdown_sidebar = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
}}

:host h2{{
    font-family: Arial, sans-serif !important;
    font-size: {sidebar_widget_height}px !important;
    /*border: 3px solid {evergreen} !important;*/
    border-radius: 6px !important;
    padding: 10px 10px 10px !important;
    background-color: {other_dark_blue_2} !important;
    color: {white} !important;
    text-align: center !important;
    width: auto !important;
}}
"""

#? ---------- Main Widgets CSS Styles ---------- ? #

table_text_size = 20

stylesheet_column = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    background-color: {white_sand} !important;
    border-radius: 10px !important;
    padding: 5px !important;
    margin: 5px !important;
    border: 2px solid {other_dark_blue_2} !important;
    height: 95% !important;
    width: 100% !important;
    /*
    */
}}
"""
stylesheet_markdown_table = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    background-color: {other_dark_blue_5} !important;
    border: 3px solid {other_dark_blue_2} !important;
    border-radius: 10px !important;
    padding: 10px !important;
    height: 20% !important;
}}

p{{
    font-family: Arial, sans-serif !important;
    font-size: {table_text_size}px !important;
    font-weight: bold !important;
    color: {black} !important;
    padding: 0px !important;
    margin: 0px !important;
}}
"""

stylesheet_tabulator = f"""
:host {{
    display: flex !important;
    border: 8px solid {other_dark_blue_2} !important;
    border-radius: 5px 5px 5px 5px !important;
    border-color: 2px solid {orange} !important;
    text-align: center !important;
    width: 100% !important;
    height: 80% !important;
    padding: 0px !important;
    margin: 0px !important;
}}

:host .pnx-tabulator.tabulator{{
    background-color: red !important;
}}

.tabulator-header{{
    background-color: {other_dark_blue} !important;
    border-bottom: 0px solid {other_dark_blue} !important;
    padding: 5px !important;
}}

.tabulator-header .tabulator-col-resize-handle{{
    background-color: {other_dark_blue} !important;
    width: 5px !important;
}}

:host .tabulator-header-contents{{
    background-color: {other_dark_blue} !important;
    text-align: center !important;
    padding: 0px !important;
    margin: 0px !important;
}}

.tabulator-headers{{
    background-color: {other_dark_blue} !important;
    border-bottom: 0px solid {other_dark_blue} !important;
    padding: 0px !important;
    margin: 0px !important;
}}

.tabulator-col{{
    background-color: {other_dark_blue} !important;
    border: 0px solid {other_dark_blue} !important;
    margin: 0px !important;
}}

.tabulator-col-content{{
    /* pour les titres de colonne */
    font-family: Arial, sans-serif !important;
    font-size: {tabulator_header_height}px !important;
    font-weight: bold !important;
    background-color: {other_dark_blue} !important;
    border: 0px solid {other_dark_blue} !important;
    color: {day} !important;
    padding: 0px !important;
    margin: 0px !important;
}}

:host .tabulator-tableholder{{
    background-color: {other_dark_blue_2} !important;
    border: 0px solid {green} !important;
}}

.tabulator-table{{
    background-color: {other_dark_blue_2} !important;
    border: 0px solid {green} !important;
}}

.tabulator-cell.tabulator-editable{{
    font-family: Arial, sans-serif !important;
    font-size: {tabulator_cell_height}px !important;
    color: {day} !important;
}}

.tabulator-row.tabulator-selectable.tabulator-row-even.tabulator-editing{{
    /*background-color: {red} !important;*/
    border-bottom: 2px solid {light_blue} !important;
    border-top: 2px solid {light_blue} !important;
}}

.tabulator-row.tabulator-selectable.tabulator-row-odd.tabulator-editing{{
    /*background-color: {red} !important;*/
    border-bottom: 2px solid {light_blue} !important;
    border-top: 2px solid {light_blue} !important;
}}

.tabulator-row.tabulator-selectable.tabulator-row-odd.tabulator-editing .tabulator-cell.tabulator-editable{{
    font-family: Arial, sans-serif !important;
    font-weight: bold !important;
    font-size: {tabulator_cell_height}px !important;
    color: {orange} !important;
}}

.tabulator-row.tabulator-selectable.tabulator-row-even.tabulator-editing .tabulator-cell.tabulator-editable{{
    font-family: Arial, sans-serif !important;
    font-weight: bold !important;
    font-size: {tabulator_cell_height}px !important;
    color: {orange} !important;
}}

.tabulator-row.tabulator-selectable.tabulator-row-even.tabulator-editing .tabulator-cell.tabulator-editable.input{{
    font-family: Arial, sans-serif !important;
    font-weight: bold !important;
    font-size: {tabulator_cell_height}px !important;
    color: {green} !important;
}}

.tabulator-row.tabulator-selectable.tabulator-row-even{{
    max-height: 60px !important;
    background-color: {other_dark_blue_3} !important;
}}

.tabulator-row.tabulator-selectable.tabulator-row-odd{{
    max-height: 60px !important;
    background-color: {other_dark_blue_2} !important;
}}

.tabulator-row.tabulator-selectable.tabulator-row-even .tabulator-col-resize-handle{{
    background-color: {other_dark_blue_3} !important;
    width: 5px !important;
}}

.tabulator-row.tabulator-selectable.tabulator-row-odd .tabulator-col-resize-handle{{
    background-color: {other_dark_blue_2} !important;
    width: 5px !important;
}}


:host(.bk-panel-models-tabulator-DataTabulator) .pnx-tabulator.tabulator{{
    background-color: {other_dark_blue_2} !important;
    border: 0px solid {green} !important;
}}

/* ---------- marche ? ---------- */

.bk-panel-models-tabulator-DataTabulator {{
    background-color: {other_dark_blue_2} !important;
    border: 0px solid {green} !important;
}}
"""

stylesheet_gridSpec = f"""
:host {{
    /*border: 2px solid {medium_blue} !important;*/
    border-radius: 0px 0px 5px 5px !important;
    background-color: {medium_blue} !important;
    text-align: center !important
    padding: 10px !important;
    /*width: auto !important;*/
}}

:host .bk-GridBox {{
    border: 3px solid {urgency_green} !important;
}}
"""

stylesheet_gridbox = f"""
:host {{
    background-color: {dark_blue} !important;
    border : 2px solid {orange} !important;
    border-radius: 25px !important;
    /*padding: 0px 20px !important;*/
    margin: 0px auto !important; /* Centrer l'élément horizontalement */
    max-width: calc(100% - 10px); /* Empêcher le dépassement horizontal */
    display: grid !important;
    grid-template-columns: repeat(2, 1fr); /* 2 colonnes */
    gap: 10px; /* Espacement entre les colonnes et lignes */
    box-sizing: border-box;
    transition: background-color 0s ease;
}}
"""

stylesheet_gridStack = f"""
:host {{
    border-radius: 0px 0px 5px 5px !important;
    background-color: {white} !important;
    display: flex !important;
    height: 100% !important;
    /*
    border: 2px solid {orange} !important;
    */
}}

.grid-stack-item-content {{
    display: flex !important;
    padding: 0px !important;
    margin: 0px !important;
    height: 100% !important;
    width: 100% !important;
    /*
    border: 1px solid {red} !important;
    justify-content: end !important;
    */
}}
"""