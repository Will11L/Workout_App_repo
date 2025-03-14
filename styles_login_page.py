from common_css import *

#? ---------- Main Widgets CSS Styles ---------- ? #

title_text_size = 16
select_text_size = 14
textinput_text_size = select_text_size

stylesheet_gridStack = f"""
:host {{
    border-radius: 0px 0px 5px 5px !important;
    background-color: {white_sand} !important;
    display: flex !important;
    /*
    border: 2px solid {orange} !important;
    */
}}

.grid-stack-item-content {{
    display: flex !important;
    padding: 0px !important;
    margin: 0px !important;
    width: 100% !important;
    /*
    border: 1px solid {red} !important;
    justify-content: end !important;
    height: 100% !important;
    */
}}
"""

stylesheet_column = f"""
:host {{
    justify-content: start !important;
    background-color: {white} !important;
    border-radius: 0px 20px 20px 0px !important;
    padding: 20px !important;
    height: 100% !important;
    /*
    border: 2px solid {light_blue} !important;
    width: 100% !important;
    */
}}
"""

stylesheet_language_selector = f"""
:host {{
    align: center !important;
    padding: 0px !important;
    margin: 0px !important;
    width: 25% !important;
    transition-duration: 500ms !important;
    
    /*
    border: 1px solid {evergreen} !important;
    background-color: {urgency_green} !important;
    */
}}

.open {{
    background-color: blue !important;
}}

.bk-input-group:has(> select) {{
    padding: 0px !important;
    margin: 0px !important;
}}

:host .bk-input-group {{
    /*position: relative; /* Ajouté pour permettre le chevauchement */*/
    padding: 0px !important;
}}

:host .bk-input-group .bk-input {{
    font-family: Arial, sans-serif !important;
    font-size: {select_text_size}px !important;
    padding: 5px !important;
    background-color: {white} !important;
    border: 1px solid {white} !important;
    border-radius: 15px !important;
    color: {black} !important;
    text-align: center !important;
    /*
    font-weight: bold !important;
    */
}}

:host label {{
    display: none !important;
    font-family: Arial, sans-serif !important;
    font-weight: nomal !important;
    font-size: {header_height_text}px !important;
    border: 2px solid {dark_blue} !important;
    border-radius: 5px !important;
    background-color: {red} !important;
    color: {dark_blue} !important;
    /*
    padding: 0px 10px 0px !important;
    */
}}
"""

stylesheet_markdown_login = f"""
:host {{
    display: flex !important;
    justify-content: start !important;
    align-items: center !important;
    padding: 0px !important;
    margin: 0px !important;
    /*
    margin-left: 80px !important;
    margin-right: 80px !important;
    */
}}

:host a.header-anchor {{
    display: none !important;
}}

:host h1{{
    font-family: Arial, sans-serif !important;
    font-size: {title_text_size}px !important;
    font-weight: bold !important;
    text-align: center !important;
    padding: 10px !important;
    background-color: {white} !important;
    color: {black} !important;
    /*
    padding: 16px 10px 16px !important;
    margin: 15px 0px 0px !important;
    border: 3px solid {gray_4} !important;
    border-radius: 6px !important;
    */
}}

:host p{{
    font-family: Arial, sans-serif !important;
    font-size: 15px !important;
    border-radius: 6px !important;
    padding: 10px !important;
    background-color: {white} !important;
    color: {celtic_blue} !important;
    text-align: center !important;
    /*
    margin: 15px 0px 0px !important;
    padding: 16px 10px 16px !important;
    border: 3px solid {gray_4} !important;
    */
}}
"""

stylesheet_TextInput = f"""
:host {{
    align: center !important;
    font-family: Arial, sans-serif !important;
    margin-top: 25px !important;
    /*
    border: 1px solid {evergreen} !important;
    border-radius: 4px !important;
    background-color: {urgency_green} !important;
    */
}}

:host .bk-input-group {{
    position: relative;
}}

:host .bk-input-group .bk-input{{
    font-family: Arial, sans-serif !important;
    font-size: {select_text_size}px !important;
    background-color: {white} !important;
    border: 2px solid {nevada} !important;
    color: {nevada} !important;
    text-align: center !important;
    /*
    font-weight: bold !important;
    font-style: italic !important;
    */
}}

:host label{{
    font-family: Arial, sans-serif !important;
    font-size: {select_text_size}px !important;
    font-weight: bold !important;
    text-align: start !important;
    padding: 0px 10px 0px !important;
    background-color: {white} !important;
    color: {nevada} !important;
    position: absolute;
    top: -15px !important;  /* 10px from the top */
    left: -15px !important;  /* 10px from the left */
    z-index: 1 !important;  /* Place the label on top */
    /*
    border: 2px solid {orange} !important;
    border-radius: 5px !important;
    display: none !important;
    */
}}
"""

stylesheet_login_button = f"""
:host {{
    display: flex !important;
    justify-content: start !important;
    align-items: center !important;
    border-radius: 0px !important;
    width: 25% !important;
    margin-top: 15px !important;
    /*
    border: 2px solid {alert_2} !important;
    */
}}

:host(.solid) .bk-btn.bk-btn-default {{
    background-color: {celtic_blue} !important;
    color: {day} !important;
    font-family: Arial, sans-serif !important;
    font-size: {select_text_size}px !important;
    font-weight: bold !important;
    transition: background-color 0s ease;
    /*
    padding: 10px 20px 10px !important;
    */
}}
"""

stylesheet_forgot_button = f"""
:host {{
    display: flex !important;
    justify-content: start !important;
    align-items: center !important;
    border-radius: 0px !important;
    width: 25% !important;
    padding: 0px !important;
    margin: 0px !important;
    margin-top: 10px !important;
    /*
    border: 2px solid {alert_2} !important;
    */
}}

:host(.solid) .bk-btn.bk-btn-default {{
    background-color: {white} !important;
    color: {celtic_blue} !important;
    font-family: Arial, sans-serif !important;
    font-size: {select_text_size}px !important;
    font-weight: normal !important;
    transition: background-color 0s ease;
    /*
    padding: 10px 20px 10px !important;
    */
}}
"""

stylesheet_login_image = f"""
:host {{
    padding: 0px !important;
    margin: 0px !important;
    width: 100% !important;
    height: 100% !important;
    border-radius: 20px 0px 0px 20px !important;
    /*
    border: 2px solid {alert_2} !important;
    */
}}

:host img {{
    display: flex !important;
    justify-content: end !important;
    width: 100% !important;
    height: 100% !important;
    border-radius: 20px 0px 0px 20px !important;
    object-fit: cover !important;   /* cove by cutting the image */
    /*
    border: 2px solid {green} !important;
    object-fit: fill !important;    /* fill by resizing the image */
    */
}}
"""

stylesheet_column2 = f"""
:host {{
    justify-content: start !important;
    background-color: {white} !important;
    border: 1px solid {light_blue} !important;
    border-radius: 0px 20px 20px 0px !important;
    padding: 20px !important;
    height: 100% !important;
    /*
    width: 100% !important;
    border: 2px solid {alert_2} !important;
    */
}}
"""