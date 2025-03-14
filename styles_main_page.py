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

stylesheet_buttons_row = f"""
:host {{
    background-color: {dark_blue} !important;
    border : 2px solid {light_blue} !important;
    /*border-radius: 25px !important;*/
    /*padding: 0px 20px !important;*/
    margin: 0px auto !important; /* Centrer l'élément horizontalement */
    /*margin-top: 50px !important;*/
    /*max-width: calc(100% - 100px); /* Empêcher le dépassement horizontal */*/
    display: flex !important;
    justify-content: space-between !important;
}}

/* Les éléments restent sur une seule ligne pour les écrans larges */
:host > div {{
    /*background-color: {evergreen} !important;*/
    /*border: 2px solid {light_blue} !important;*/
    /*padding: 2px !important;*/
    text-align: center !important;
    flex: 1 1 50% !important; /* Chaque div occupe un quart de la largeur */
    box-sizing: border-box;
}}

@media (max-width: 412px) and (max-height: 915px) {{
    /* Styles spécifiques pour le Samsung Galaxy S21+ en orientation portrait */
    :host {{
        /* Par exemple, ajuster la largeur ou la disposition pour ce type d’écran */
    }}

    :host > div {{
        /* Ajuster chaque élément de la Row pour qu'il prenne toute la largeur */
        flex: 1 1 25% !important;
    }}
}}

@media (max-width: 915px) and (max-height: 412px) {{
    /* Styles pour le Samsung Galaxy S21+ en orientation paysage */
    :host {{
        /* Styles spécifiques pour l’orientation paysage, si nécessaire */
    }}

    :host > div {{
        flex: 1 1 25% !important; /* Deux éléments par ligne en paysage */
    }}
}}
"""

stylesheet_gridStack = f"""
:host {{
    display: flex !important;
    border: 2px solid {orange} !important;
    border-radius: 0px 0px 5px 5px !important;
    background-color: {white_sand} !important;
}}
"""

stylesheet_column = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    /*border: 2px solid {alert_2} !important;*/
    border-radius: 0px !important;
    border: 1px solid {light_blue} !important;
}}
"""

stylesheet_markdown_main = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
}}

:host h3{{
    font-family: Arial, sans-serif !important;
    font-size: 30px !important;
    font-weight: bold !important;
    /*border: 3px solid {evergreen} !important;*/
    border-radius: 6px !important;
    /*padding: 10px !important;*/
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    margin: 5px 0px 0px !important;
    background-color: {other_dark_blue_2} !important;
    color: {white} !important;
    text-align: center !important;
    width: auto !important;
}}

:host a.header-anchor {{
    display: none !important;
    width: 0px !important;
    height: 0px !important;
}}

:host h2{{
    font-family: Arial, sans-serif !important;
    font-size: 28px !important;
    /*border: 3px solid {evergreen} !important;*/
    border-radius: 6px !important;
    padding: 10px 10px 10px !important;
    background-color: {other_dark_blue_2} !important;
    color: {white} !important;
    text-align: center !important;
    width: auto !important;
}}

:host h1{{
    font-family: Arial, sans-serif !important;
    font-size: 25px !important;
    /*border: 3px solid {gray_4} !important;*/
    border-radius: 6px !important;
    /*padding: 16px 10px 16px !important;*/
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    margin: 5px 0px 0px !important;
    background-color: {gray_5} !important;
    color: {white} !important;
    text-align: center !important;
    width: auto !important;
}}

:host p{{
    font-family: Arial, sans-serif !important;
    font-size: 25px !important;
    /*border: 3px solid {gray_4} !important;*/
    border-radius: 6px !important;
    /*padding: 16px 10px 16px !important;*/
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    padding-left: 10px !important;
    padding-right: 10px !important;
    margin: 15px 0px 0px !important;
    background-color: {gray_5} !important;
    color: {white} !important;
    text-align: center !important;
    width: auto !important;
}}
"""

stylesheet_select = f"""
:host {{
    align: center !important;
    /*border: 1px solid {evergreen} !important;*/
    /*background-color: {urgency_green} !important;*/
}}

:host .bk-input-group {{
    position: relative; /* Ajouté pour permettre le chevauchement */
}}

:host .bk-input-group .bk-input {{
    font-family: Arial, sans-serif !important;
    font-size: 20px !important;
    /*font-weight: bold !important;*/
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    border: 1px solid {white} !important;
    background-color: {dark_blue} !important;
    color: {white} !important;
    text-align: center !important;
}}

:host label {{
    font-family: Arial, sans-serif !important;
    font-weight: bold !important;
    font-size: 26px !important;
    padding: 0px 10px 0px !important;
    border: 2px solid {dark_blue} !important;
    border-radius: 5px !important;
    background-color: {white} !important;
    color: {dark_blue} !important;
    position: absolute; /* Permet de positionner le label de manière absolue */
    top: -10px; /* Ajuster selon le chevauchement souhaité */
    left: 10px; /* Ajuster selon la position souhaitée */
    z-index: 1; /* Assure que le label est au-dessus de l'input */
}}
"""