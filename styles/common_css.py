# Colors
from re import sub


primary_color_palette = ['#005E60', '#C8FF08', '#FFFFFF', '#212121', '#FAFAFA', '#E3E3E3', '#CCCCCC', '#696969', '#484848']
primary_accents = ['#59C3C9', '#439297', '#75CA64', '#58984B', '#BFA682', '#8F7D62']
secondary_accents = ['#EC642B', '#F19F39', '#F5C147']
tints = ['#439297', '#96BDBD', '#C7DBDB']

# ? ---------- Primary color palette ---------- ? #
evergreen = '#005E60'
urgency_green = '#C8FF08'
day = '#FFFFFF'
night = '#212121'

gray_1 = '#FAFAFA'
gray_2 = '#E3E3E3'
gray_3 = '#CCCCCC'
gray_4 = '#696969'
gray_5 = '#484848'

# ? ---------- Accent color palette ---------- ? #
# Primary Accents, for use in PPT, charts, graphs and infographics only
sky = '#59C3C9'
dark_sky = '#439297'
forest = '#75CA64'
dark_forest = '#58984B'
earth = '#BFA682'
dark_earth = '#8F7D62'

# Secondary Accents, for remote operating center alerts OR when additional accents are needed
alert_1 = '#EC642B'
alert_2 = '#F19F39'
alert_3 = '#F5C147'

# Tints, use sparingly for accents
evergreen_tint_1 = '#439297'
evergreen_tint_2 = '#96BDBD'
evergreen_tint_3 = '#C7DBDB'

# Other colors
evergreen_100 = '#F5FBFB'
white = '#FFFFFF'
orange = '#FFA500'
dark_orange = '#BE5504'
red = '#FF0000'
dark_red = '#8B0000'
green = '#008000'
dark_green = '#006400'

# Blue Colors - Sea Theme
black = '#192428'
medium_black = '#2D3B3C'
gray = '#414C50'
#dark_blue = '#00072D'
dark_blue = '#04103A'
second_dark_blue = '#101C42'
third_dark_blue = '#273255'
dark_icon_blue = '#0C1532'
#light_blue = '#05D5FA'
light_blue = '#4AD0EE'
light_blue_2 = '#92E3F5'
medium_blue = '#0784B5'
#medium_blue = light_blue

other_dark_blue='#011F4B'
other_dark_blue_2='#03396C'
other_dark_blue_3='#005B96'
other_dark_blue_4='#6497B1'
other_dark_blue_5='#B3CDE0'

sand = '#F9E8C9'

tabulator_header_background = other_dark_blue
tabulator_line1_background = other_dark_blue_2
tabulator_line2_background = other_dark_blue_3

#* ---------- Colors of Dev_Team ---------- *#

yale_blue = '#00356B'       # For the navigation bar and hover color for buttons
celtic_blue = '#246BCE'     # is primary color, for all interactive elements, as buttons, links, different controls
honest = '#F4F4F4'          # is used like hover color in navigation bar, can show disable mode for some controls
lavender = '#E6E6FA'        # is used to indicate active menu item, active rove in list or table
shark = '#212529'           # indicated pressed icon
nevada = '#6E777B'          # default color for enabled icons
manatee = '#91969D'         # is used for label, hint, and caption text
silver = '#C0C0C0'          # is border and divider color
cloud = '#E0E0E0'           # indicates disabled inputs and is used for table header
white_sand = '#F5F5F5'      # can be background color for the card when there is an elevation.
                            # it is used for hover lists and tables
danger = '#DC3545'          # for destructive actions and negate moods, for validation text, for danger buttons
weed = '#28A745'
strawberry = '#FFB7B7'      # for background for danger alerts, error state
pistachio = '#98C379'       # for background for success alerts, success state

black = '#000000'
white = '#FFFFFF'           # Main background color. Can be Text color on Celtic blue, Yale blue, and Black background.
day = white                 # Main color for texts within the whole platform.

#* ---------- Data visualization colors ---------- *#

primary_color = '#5E00C3'
secondary_color = '#99E5F2'
tertiary_color = '#D85798'
fourth_color = '#1451C9'
fifth_color = '#2A9555'
sixth_color = '#F2BE38'


#* ---------- Typography ---------- *#

roboto_light = '300'
roboto_regular = '400'
roboto_medium = '500'
roboto_bold = '700'

h1_font_family = 'Roboto'
h1_font_size = '96px'
h1_font_weight = roboto_light

h2_font_family = 'Roboto'
h2_font_size = '60px'
h2_font_weight = roboto_light

h3_font_family = 'Roboto'
h3_font_size = '48px'
h3_font_weight = roboto_regular

h4_font_family = 'Roboto'
h4_font_size = '34px'
h4_font_weight = roboto_regular

h5_font_family = 'Roboto'
h5_font_size = '24px'
h5_font_weight = roboto_regular

h6_font_family = 'Roboto'
h6_font_size = '20px'
h6_font_weight = roboto_medium

subtitle1_font_family = 'Roboto'
subtitle1_font_size = '16px'
subtitle1_font_weight = roboto_regular

subtitle2_font_family = 'Roboto'
subtitle2_font_size = '14px'
subtitle2_font_weight = roboto_medium

body1_font_family = 'Roboto'
body1_font_size = '16px'
body1_font_weight = roboto_regular

body2_font_family = 'Roboto'
body2_font_size = '14px'
body2_font_weight = roboto_regular

button_font_family = 'Roboto'
button_font_size = '14px'
button_font_weight = roboto_medium

caption_font_family = 'Roboto'
caption_font_size = '12px'
caption_font_weight = roboto_regular

overline_font_family = 'Roboto'
overline_font_size = '10px'
overline_font_weight = roboto_regular


#? ---------- Global CSS Styles ---------- ? #

header_background = black

header_height = 40
header_height_text = 15

main_button_height = 15
sidebar_widget_height = 15

tabulator_header_height = 16
tabulator_cell_height = 12

template_css = f"""
/* -------------------- Header -------------------- */

nav#header {{
    top: 0 !important;
}}

#header-design-provider {{
    height: {header_height}px !important;
    padding: 0px !important;
    margin: 0px !important;
    /*
    border: 1px solid {green} !important;
    */
}}

#header-items {{
    align: center !important;
    display: flex !important;
    justify-content: start !important;
    background-color: {header_background} !important;
    font-weight: bold !important;
    height: {header_height}px !important;
    margin: 0px !important;
    padding: 0px !important;
    /*
    border: 1px solid {red} !important;
    border-bottom: 3px solid {light_blue} !important;
    width: 0px !important;
    color: {light_blue} !important;
    */
}}

.shadow {{
    height: {header_height}px !important;
    background-color: {header_background} !important;
    color: {white} !important;
    font-weight: bold !important;
    height: {header_height}px !important;
    padding: 5px 0px 5px 0px !important;
    /*
    padding: 0px !important;
    border-bottom: 3px solid {light_blue_2} !important;
    border: 3px solid {light_blue} !important;
    */
}}

.shadow .app-header .app-logo {{
    height: {header_height*0.8}px !important;
    width: {header_height*0.8}px !important;
    padding: 0px !important;
    margin: 0px !important;
    /*
    background-color: {red} !important;
    border: 1px solid {green} !important;
    */
}}

.shadow .app-header .title {{
    font-family: Arial, sans-serif !important;
    font-size: {header_height*0.4}px !important;
    background-color: {header_background} !important;
    color: {day} !important;
    /*
    font-weight: bold !important;
    text-align: center !important;
    border: 4px solid {evergreen} !important;
    border-radius: 4px !important;
    */
}}

.shadow .pn-bar {{
    display: none !important;
    background-color: {other_dark_blue_5} !important;
    border-radius: 3px !important;
    height: 5px !important;
    width: 25px !important;
    margin: 5px 0px 5px !important;
    margin-left: 0px !important;
    /*
    border : 3px solid {red} !important;
    */
}}

.shadow .app-logo {{
    background-color: {header_background} !important;
    height: {header_height}px !important;
    width: {header_height}px !important;
    font-color: {day} !important;
    /*
    border: 2px solid {alert_1} !important;
    changer la couleur du logo
    */
}}

.pn-toggle-theme {{
    /*
    background-color: {evergreen} !important;
    color: {urgency_green} !important;
    border: 4px solid {evergreen_tint_1} !important;
    border-radius: 4px !important;
    */
}}

.pn-busy-container {{
    margin-right: 10px !important;
    /*
    background-color: {evergreen} !important;
    color: {forest} !important;
    border-radius: 4px !important;
    border: 2px solid {red} !important;
    */
}}

/*
.pn-toggle-theme .checked {{
    background-color: {day} !important;
    border-radius: 4px !important;
    /*
    border: 4px solid {forest} !important;
    */
}}
*/

/*
.shadow .pn-busy-container .bk-panel-models-markup-HTML.loader.light {{
    /*background-color: {sky} !important;*/
    /*border: 4px solid {earth} !important;*/
}}
*/

:host path {{
    background-color: {alert_3} !important;
    color: {dark_forest} !important;
    border: 4px solid {earth} !important;
    border-radius: 4px !important;
}}


/* -------------------- Sidebar -------------------- */


.sidenav {{
    background-color: {dark_blue} !important;
    color: {urgency_green} !important;
    /*border: 3px solid {light_blue} !important;*/
    /*border-bottom: 3px solid {light_blue} !important;*/
    /*border-left: 3px solid {light_blue} !important;*/
    /*border-right: 3px solid {light_blue} !important;*/
    width: 300px !important;
}}

.nav.flex-column {{
    background-color: {dark_blue} !important;
    color: {light_blue} !important;
    width: auto !important;
}}

/* -------------------- Body -------------------- */

body {{
    display: flex !important;
    margin: 0px !important;
    padding: 0px !important;
    /*
    background-color: {orange} !important;
    height: 100% !important;
    width: 100% !important;
    */
}}

/* -------------------- Main, modal and notifications -------------------- */

.main {{
    padding : 0px 0px 0px !important;
    margin: 0px !important;
    /*
    background-color: {red} !important;
    border: 2px solid {red} !important;
    width: 100% !important;
    height: 100% !important;
    */
}}

.fullscreen-button {{
    border: 2px solid {red} !important;
    color: {green} !important;
}}

.pn-modal-content {{
    border: 2px solid {red} !important;
    border-radius: 0px !important;
}}

.pn-modal-close {{
    background-color: {other_dark_blue} !important;
    color: {white} !important;
    font-size: 20px !important;
    font-weight: bold !important;
    border: 2px solid {white} !important;
    border-radius: 0px 5px 0px 5px !important;
}}

.pn-wrapper {{
    /*background-color: {alert_1} !important;*/
    /*border: 2px solid {alert_1} !important;*/
    /*border-radius: 5px !important;*/
    /*width: auto !important;*/
}}

.notyf__toast.notyf__toast--dismissible.notyf__toast--lower {{
    background-color: {dark_blue} !important;
    color: {orange} !important;
    border: 2px solid {orange} !important;
    border-radius: 5px !important;
}}

.notyf__toast.notyf__toast--dismissible.notyf__toast--lower.notyf__toast--success {{
    color: {forest} !important;
    border: 2px solid {forest} !important;
}}

.notyf__toast.notyf__toast--dismissible.notyf__toast--lower.notyf__toast--error {{
    color: {alert_1} !important;
    border: 2px solid {alert_1} !important;
}}

.notyf__ripple {{
    background-color: {night} !important;
    border-radius: 5px !important;
}}

.notyf__wrapper{{
    font-family: Arial, sans-serif !important;
    font-size: 16px !important;
    font-weight: bold !important;
    background-color: {night} !important;
    border-radius: 5px !important;
    width: auto !important;
}}

.notyf__icon--success {{
    background-color: {night} !important;
    color: {forest} !important;
    border: 2px solid {forest} !important;
}}

.notyf__icon--error {{
    background-color: {night} !important;
    color: {alert_1} !important;
    border: 2px solid {alert_1} !important;
}}

.fas.fa-exclamation-triangle {{
    background-color: {night} !important;
    color: {orange} !important;
}}

.fas.fa-info-circle {{
    background-color: {night} !important;
    color: {sky} !important;
}}

.notyf__dismiss {{
    background-color: {night} !important;
    color: {urgency_green} !important;
}}

.notyf__dismiss-btn {{
    background-color: {night} !important;
    color: {urgency_green} !important;
}}
"""

#? ---------- Header CSS Styles ---------- ? #

stylesheet_header_gridStack = f"""
:host {{
    height: {header_height}px !important;
    border-radius: 0px !important;
    background-color: {header_background} !important;
    margin: 0px !important;
    padding: 0px !important;
    /*
    border: 2px solid {orange} !important;
    */
}}

.grid-stack-item-content {{
    display: flex !important;
    justify-content: end !important;
    align-items: center !important;
    padding: 0px !important;
    margin: 0px !important;
    /*
    border: 1px solid {red} !important;
    */
}}
"""

stylesheet_page_selector = f"""
:host {{
    align: center !important;
    padding: 0px !important;
    margin: 0px !important;
    /*
    border: 1px solid {evergreen} !important;
    background-color: {urgency_green} !important;
    */
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
    font-size: {header_height_text}px !important;
    font-weight: bold !important;
    padding: 5px !important;
    border: 1px solid {white} !important;
    border-radius: 15px !important;
    background-color: {lavender} !important;
    color: {night} !important;
    text-align: center !important;
}}

:host label {{
    display: none !important;
    font-family: Arial, sans-serif !important;
    font-weight: bold !important;
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

stylesheet_header_select = f"""
:host {{
    align: center !important;
    padding: 0px !important;
    margin: 0px !important;
    /*
    border: 1px solid {evergreen} !important;
    background-color: {urgency_green} !important;
    */
}}

.bk-input-group:has(> select) {{
    padding: 0px !important;
    margin: 0px !important;
}}

:host .bk-input-group {{
    /*position: relative; /* Ajouté pour permettre le chevauchement */*/
}}

:host .bk-input-group .bk-input {{
    font-family: Arial, sans-serif !important;
    font-size: {header_height_text}px !important;
    font-weight: normal !important;
    padding: 5px !important;
    border: 1.5px solid {white} !important;
    border-radius: 20px !important;
    background-color: {header_background} !important;
    color: {white} !important;
    text-align: center !important;
    /*
    font-weight: bold !important;
    */
}}

:host label {{
    display: none !important;
    font-family: Arial, sans-serif !important;
    font-weight: bold !important;
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

stylesheet_header_button = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    background: {day} !important;
    border-radius: 20px !important;
    padding: 0px !important;
    margin: 0px !important;
    /*
    border: 2px solid {alert_2} !important;
    */
}}

:host(.solid) .bk-btn.bk-btn-default {{
    background-color: {day} !important;
    border-radius: 20px !important;
    color: {night} !important;
    font-family: Arial, sans-serif !important;
    font-size: {header_height_text}px !important;
    font-weight: bold !important;
    transition: background-color 0s ease;
    /*
    padding: 10px 20px 10px !important;
    */
}}

:host(.solid) .bk-btn.bk-btn-primary {{
    background-color: {red} !important;
    color: {white} !important;
    font-family: Arial, sans-serif !important;
    font-size: {header_height_text}px !important;
    font-weight: bold !important;
    transition: background-color 0s ease;
    /*
    padding: 10px 20px 10px !important;
    */
}}
"""

stylesheet_id_button = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    border-radius: 0px !important;
    width: {header_height}px !important;
    height: {header_height}px !important
    padding: 0px !important;
    margin: 0px 10px 0px 0px !important;
    /*
    border: 2px solid {alert_2} !important;
    */
}}

.bk-TablerIcon {{
    background-color: {celtic_blue} !important;
    color: {day} !important;
    height: {header_height*0.8}px !important;
    width: {header_height*0.8}px !important;
    font-size: {header_height*0.8}px !important;
    border-radius: 20px !important;
}}

.bk-IconRow {{
    background-color: {header_background} !important;
    color: {day} !important;
    font-size: {header_height_text}px !important;
}}

.bk-IconLabel {{
    background-color: {celtic_blue} !important;
    color: {day} !important;
    font-size: {header_height_text}px !important;
    font-weight: bold !important;
}}

:host(.solid) .bk-btn.bk-btn-default {{
    background-color: {header_background} !important;
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

stylesheet_markdown_modal = f"""
:host {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
}}

:host a.header-anchor {{
    display: none !important;
    width: 0px !important;
    height: 0px !important;
}}

:host h3{{
    font-family: Arial, sans-serif !important;
    font-size: 14px !important;
    font-weight: bold !important;
    border-radius: 5px !important;
    margin: 0px auto !important;
    background-color: {medium_blue} !important;
    color: {white} !important;
    text-align: center !important;
    /*
    border: 3px solid {evergreen} !important;
    padding: 10px !important;
    */
}}

:host h2{{
    font-family: Arial, sans-serif !important;
    font-size: 20px !important;
    /*border: 3px solid {evergreen} !important;*/
    border-radius: 5px !important;
    padding: 10px 10px 10px !important;
    margin: 0px !important;
    background-color: {other_dark_blue_2} !important;
    color: {white} !important;
    text-align: center !important;
    width: auto !important;
}}

:host p{{
    font-family: Arial, sans-serif !important;
    font-size: 14px !important;
    /*border: 3px solid {gray_4} !important;*/
    border-radius: 5px !important;
    /*padding: 16px 10px 16px !important;*/
    margin: 0px !important;
    background-color: {gray_4} !important;
    color: {white} !important;
    text-align: center !important;
    width: auto !important;
}}

"""