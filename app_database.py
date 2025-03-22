import sqlite3
import pandas as pd

import re
from IPython.display import display

import os

# Dynamically locate the path to database.db relative to this file
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
database_path = os.path.join(BASE_DIR, 'database.db')

def create_database():
    conn = sqlite3.connect(database_path)
    conn.close()

def drop_all_tables():
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    tables = [table for table in tables if table[0] != 'sqlite_sequence']
    for table in tables:
        if table[0][0].isdigit():
            table_name = '"' + table[0] + '"'
        else:
            table_name = table[0]
        c.execute("DROP TABLE " + table_name)
    conn.commit()
    conn.close()

def create_and_fill_table(table_name, column_definitions, data_list):
    create_table(table_name, column_definitions)
    data = [(i+1, data_list[i]) for i in range(len(data_list))]
    fill_table(table_name, data)

def create_table(table_name, columns):
    """
    Create a table in the database with the given name and columns.

    Parameters:
    table_name (str): The name of the table to create.
    columns (str): The columns of the table to create. 
    The columns should be formatted as a string with the column names and types separated by commas. 
    For example, "id INTEGER PRIMARY KEY, name TEXT, value INTEGER".

    Returns:
    None
    """
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS " + table_name)
    c.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (" + columns + ")")
    conn.commit()
    conn.close()

def create_table_from_dataframe(dataframe, table_name):
    """
    Create a table in the database with the given name and columns based on a pandas DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame to create the table from.
    table_name (str): The name of the table to create.

    Returns:
    None
    """
    conn = sqlite3.connect(database_path)
    columns = dataframe.columns
    types = dataframe.dtypes
    column_defs = []
    for col, typ in zip(columns, types):
        if pd.api.types.is_integer_dtype(typ):
            sql_type = "INTEGER"
        elif pd.api.types.is_float_dtype(typ):
            sql_type = "REAL"
        elif pd.api.types.is_bool_dtype(typ):
            sql_type = "INTEGER"
        else:
            sql_type = "TEXT"
        col_quoted = f'"{col}"'
        column_defs.append(f"{col_quoted} {sql_type}")
    column_defs_str = ", ".join(column_defs)
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs_str})"
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS " + table_name)
    c.execute(create_table_sql)
    insert_dataframe_into_table(dataframe, table_name)
    conn.commit()
    conn.close()

def delete_table(table_name):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS " + table_name)
    conn.commit()
    conn.close()

def insert_dataframe_into_table(dataframe, table_name):
    conn = sqlite3.connect(database_path)
    columns = dataframe.columns
    columns_quoted = [f'"{col}"' for col in columns]
    columns_str = ", ".join(columns_quoted)
    placeholders = ", ".join("?" * len(columns))
    insert_sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
    c = conn.cursor()
    for row in dataframe.itertuples(index=False, name=None):
        c.execute(insert_sql, row)
    conn.commit()

def create_and_insert_table_from_dataframe(dataframe, table_name):
    conn = sqlite3.connect(database_path)
    columns = dataframe.columns
    types = dataframe.dtypes
    column_defs = []
    for col, typ in zip(columns, types):
        if pd.api.types.is_integer_dtype(typ):
            sql_type = "INTEGER"
        elif pd.api.types.is_float_dtype(typ):
            sql_type = "REAL"
        elif pd.api.types.is_bool_dtype(typ):
            sql_type = "INTEGER"
        else:
            sql_type = "TEXT"
        col_quoted = f'"{col}"'
        column_defs.append(f"{col_quoted} {sql_type}")
    column_defs_str = ", ".join(column_defs)
    table_name = table_name.replace(',', '_')
    table_name = table_name.replace('?', '_')
    table_name = table_name.replace(' ', '_')
    if table_name[0].isdigit():
        table_name = '"' + table_name + '"'
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs_str});"
    c = conn.cursor()
    c.execute(f"DROP TABLE IF EXISTS {table_name}")
    c.execute(create_table_sql)
    conn.commit()
    columns_quoted = [f'"{col}"' for col in columns]
    columns_str = ", ".join(columns_quoted)
    placeholders = ", ".join("?" * len(columns))
    insert_sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
    for row in dataframe.itertuples(index=False, name=None):
        row_list = list(row)
        row_list = [None if pd.isna(value) else value for value in row_list]
        if any(row_list):
            c.execute(insert_sql, row_list)
    conn.commit()
    conn.close()

def print_all_columns_in_table(table_name):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("PRAGMA table_info(" + table_name + ")")
    columns = c.fetchall()
    print('\n----- Columns of table: ' + table_name + ' -----')
    for column in columns:
        print(column)
    conn.close()

def fill_table(table_name, values):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("PRAGMA table_info(" + table_name + ")")
    columns = c.fetchall()
    values_string = ''
    for i in range(len(columns)):
        values_string += '?,'
    values_string = values_string[:-1]
    c.executemany("INSERT INTO " + table_name + " VALUES (" + values_string + ")", values)
    conn.commit()
    conn.close()

def fill_table_with_dataList(table_name, data):
    try:
        placeholders = ', '.join(['?'] * len(data[0]))
        sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.executemany(sql, data)
        conn.commit()
        print(f"Data inserted successfully into '{table_name}'.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def close(self):
    self.conn.close()

def count_elements_in_table(table_name):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM " + table_name)
    number = c.fetchone()[0]
    conn.close()
    return number

def get_number_of_columns(table_name):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("PRAGMA table_info(" + table_name + ")")
    columns = c.fetchall()
    conn.close()
    return len(columns)

def print_table_by_name(table_name):
    # affichage pas sûr de fonctionner
    conn = sqlite3.connect(database_path)
    print('\n----- Table: ' + table_name + ' -----')
    df = get_table_as_df(table_name)
    styles = [
        {'selector': 'th:not(:first-child)', 'props': 'background-color: black;'},
        {'selector': 'th', 'props': 'text-align: center;'},
        {'selector': 'tr:nth-child(odd)', 'props': 'background-color: #2B2B2B;'},
        {'selector': 'tr:nth-child(even)', 'props': 'background-color: #423F3E;'},
        {'selector': 'td', 'props': 'text-align: center; border:'},
    ]
    styled_df = df.style.set_table_styles(styles)
    styled_df = styled_df.map(lambda x: 'background-color: #950101; font-style: italic;' if (pd.isna(x)) or (str(x).lower() == 'nan') else '')
    display(styled_df)
    conn.close()

def query_table_by_name(table_name):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    if table_name[0].isdigit():
        table_name = '"' + table_name + '"'
    c.execute('SELECT * FROM ' + table_name)
    elements = c.fetchall()
    elements = [element[0] for element in elements]
    conn.close()
    return elements

def get_elements_by_column(table_name, column):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute('SELECT ' + column + ' FROM ' + table_name)
    elements = c.fetchall()
    elements = [element[0] for element in elements]
    conn.close()
    return elements

def get_columns_names(table_name):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("PRAGMA table_info(" + table_name + ")")
    columns = c.fetchall()
    columns = [column[1] for column in columns]
    conn.close()
    return columns

def select_element_by_field(table_name, field, value):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute('SELECT * FROM ' + table_name + ' WHERE ' + field + ' = ?', (value,))
    elements = c.fetchall()
    conn.close()
    return elements

def get_all_tables_names():
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    tables = [table[0] for table in tables if table[0] != 'sqlite_sequence']
    conn.close()
    return tables

def print_all_tables():
    print('database_path: ' + database_path)
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    for table in tables:
        print_table_by_name(table[0])
    conn.close()

def get_number_of_tables():
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    conn.close()
    return len(tables)

def add_column_to_table(table_name, column_name, column_type):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    try:
        c.execute("ALTER TABLE {} ADD COLUMN {} {};".format(table_name, column_name, column_type))
        conn.commit()
        print("La colonne {} a été ajoutée à la table {} avec succès.".format(column_name, table_name))
    except sqlite3.Error as e:
        print("Erreur lors de l'ajout de la colonne à la table:", e)
    conn.close()

def fill_table_column_with_values(table_name, column_name, values):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    for value in values:
        c.execute("UPDATE {} SET {} = ? WHERE name = ?;".format(table_name, column_name), (value[1], value[0]))
    conn.commit()
    conn.close()

def update_column_set_value(table_name, column_to_change, data_to_change, column_to_match, data_to_match):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("UPDATE {} SET {} = ? WHERE {} = ?;".format(table_name, column_to_change, column_to_match), (data_to_change, data_to_match))
    conn.commit()
    conn.close()

def get_last_id_from_table(table_name):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("SELECT id FROM " + table_name + " ORDER BY id DESC LIMIT 1")
    last_id = c.fetchone()[0]
    conn.close()
    return last_id

def get_value_where_column_matches(table_name, column_to_match, data_to_match, column_to_return):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("SELECT {} FROM {} WHERE {} = ?;".format(column_to_return, table_name, column_to_match), (data_to_match,))
    value = c.fetchone()[0]
    conn.close()
    return value

def add_element_to_table(table_name, values, refactor_values=False, conflict_mode='error'):
    """
    Add a new element to a table in the database.

    Parameters:
    - table_name (str): The name of the table to add the element to.
    - values (list): A list of values to add to the table.
    - refactor_values (bool): If True, sanitize values (replace special characters with underscores).
    - conflict_mode (str): What to do on UNIQUE constraint conflict. Options:
        'error'   -> Raise IntegrityError (default),
        'ignore'  -> Do nothing if conflict,
        'replace' -> Replace the existing row entirely (⚠ will reset id).

    Returns:
    - None
    """
    conn = sqlite3.connect(database_path)
    try:
        c = conn.cursor()
        c.execute("PRAGMA table_info(" + table_name + ")")
        columns = c.fetchall()

        column_names_list = [column[1] for column in columns if column[1] != 'id']
        if len(values) != len(column_names_list):
            raise ValueError("Number of values doesn't match number of columns (excluding 'id').")
        
        column_names = ', '.join(column_names_list)
        placeholders = ', '.join(['?' for _ in values])

        if refactor_values:
            #values = [re.sub(r' ', '_', str(value)) for value in values]                # Replace spaces with underscores
            #values = [re.sub(r'\?', '_', str(value)) for value in values]               # Replace question marks with underscores
            values = [re.sub(r'[^a-zA-Z0-9_]', '_', str(value)) for value in values]    # Replace special characters with underscores, only keep letters, numbers and underscores

        if conflict_mode == 'ignore':
            sql = f"INSERT OR IGNORE INTO {table_name} ({column_names}) VALUES ({placeholders})"
        elif conflict_mode == 'replace':
            sql = f"INSERT OR REPLACE INTO {table_name} ({column_names}) VALUES ({placeholders})"
        else:
            sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"

        c.execute(sql, values)
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"⚠ IntegrityError in table '{table_name}': {e} | Values: {values}")
        if conflict_mode == 'error':
            raise e
    finally:
        conn.close()

def delete_element_from_table(table_name, column, value):
    """
    Supprime un élément de la table en fonction de la valeur d'une colonne.

    Paramètres:
    - table_name (str): Le nom de la table dans la base de données.
    - column (str): Le nom de la colonne à vérifier.
    - value (str): La valeur de la colonne à vérifier.
    """
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("DELETE FROM " + table_name + " WHERE " + column + " = ?", (value,))
    conn.commit()   
    conn.close()

def delete_elements_from_table_with_2_conditions(table_name, column1, value1, column2, value2):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("DELETE FROM " + table_name + " WHERE " + column1 + " = ? AND " + column2 + " = ?", (value1, value2))
    conn.commit()   
    conn.close()

def delete_elements_from_table_with_3_conditions(table_name, column1, value1, column2, value2, column3, value3):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("DELETE FROM " + table_name + " WHERE " + column1 + " = ? AND " + column2 + " = ? AND " + column3 + " = ?", (value1, value2, value3))
    conn.commit()   
    conn.close()

def delete_elements_from_table_with_4_conditions(table_name, column1, value1, column2, value2, column3, value3, column4, value4):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("DELETE FROM " + table_name + " WHERE " + column1 + " = ? AND " + column2 + " = ? AND " + column3 + " = ? AND " + column4 + " = ?", (value1, value2, value3, value4))
    conn.commit()   
    conn.close()

def delete_row_from_table(table_name, id):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("DELETE FROM " + table_name + " WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update_cell_in_table(table_name, column, row_id, new_value):
    """
    Met à jour une cellule dans la table en fonction de la valeur d'une colonne.

    Paramètres:
    - table_name (str): Le nom de la table dans la base de données.
    - column (str): Le nom de la colonne à vérifier.
    - row_id (int): L'identifiant de la ligne à mettre à jour.
    - value (str): La valeur de la colonne à vérifier.
    """
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    print("table_name: " + str(table_name))
    print("column: " + str(column))
    print("row_id: " + str(row_id))
    print("new_value: " + str(new_value))

    # check les types de la table et met a jour la valeur en fonction
    c.execute("PRAGMA table_info(" + table_name + ")")
    columns = c.fetchall()
    for col in columns:
        if col[1] == column:
            if col[2] == 'INTEGER':
                updated_value = int(new_value)
            elif col[2] == 'REAL':
                updated_value = float(new_value)
            elif col[2] == 'BOOLEAN':
                if str(new_value).lower() in ['0', 'false', 'no', '', 'none']:
                    updated_value = 0
                else:
                    updated_value = 1
            elif col[2] == 'TEXT':
                updated_value = str(new_value)
            else:
                print("Colunm type not recognized.")
            break
    
    print("updated_value : ", updated_value)
    c.execute("UPDATE " + table_name + " SET " + column + " = ? WHERE id = ?", (updated_value, row_id))

    conn.commit()
    conn.close()

def edit_row_with_conditions(table_name, conditions, new_values):
    """
    Met à jour une ligne entière dans la table en fonction de conditions dynamiques.

    Paramètres:
    - table_name (str): Le nom de la table dans la base de données.
    - conditions (dict): Dictionnaire des conditions WHERE (colonne: valeur).
    - new_values (dict): Dictionnaire des nouvelles valeurs (colonne: nouvelle valeur).

    Retourne:
    - None
    """
    # Connexion à la base de données
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    # Création des clauses SET et WHERE
    set_clause = ", ".join([f"{col} = ?" for col in new_values.keys()])
    set_values = list(new_values.values())
    where_clause = " AND ".join([f"{col} = ?" for col in conditions.keys()])
    where_values = list(conditions.values())

    # Construction et exécution de la requête SQL
    query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
    try:
        c.execute(query, set_values + where_values)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erreur lors de la mise à jour de la table {table_name}: {e}")
    finally:
        conn.close()

def run_query(query):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    try:
        c.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Query error: {e}")
    finally:
        conn.close()

def get_Code_From_Name_And_Value(table_name, name, value):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    if type(value) == bool:
        value = int(value)
    name = str(name)
    value = str(value)
    c.execute('SELECT code FROM ' + table_name + ' WHERE name = ? AND value = ?', (name, value))
    result = c.fetchone()
    if result is not None:
        code = result[0]
    else:
        code = None
    return code

def get_Code_From_MF(MF):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    table_name = 'CodeTraduction'
    c.execute('SELECT code FROM ' + table_name + ' WHERE MF = ?', (MF,))
    result = c.fetchone()
    if result is not None:
        code = result[0]
    else:
        code = None
    return code

def get_table_as_df(table_name):
    conn = sqlite3.connect(database_path)
    df = pd.read_sql_query("SELECT * FROM " + table_name, conn)
    conn.close()
    return df

def check_if_exists_in_table(table_name, conditions):
    """
    Vérifie si un enregistrement correspondant aux conditions existe dans la table.

    Paramètres:
    - table_name (str): Le nom de la table à vérifier.
    - conditions (dict): Dictionnaire des conditions WHERE (colonne: valeur).

    Retourne:
    - bool: True si un enregistrement existe, sinon False.
    """
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    where_clause = " AND ".join([f"{col} = ?" for col in conditions.keys()])
    where_values = list(conditions.values())
    query = f"SELECT EXISTS(SELECT 1 FROM {table_name} WHERE {where_clause} LIMIT 1)"
    c.execute(query, where_values)
    exists = c.fetchone()[0] == 1
    conn.close()
    return exists

def check_if_exists_in_table_with_2_conditions(table_name, column1, value1, column2, value2):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("SELECT EXISTS(SELECT 1 FROM {} WHERE {} = ? AND {} = ? LIMIT 1)".format(table_name, column1, column2), (value1, value2))
    exists = c.fetchone()[0] == 1
    conn.close()
    return exists


def close_database():
    conn = sqlite3.connect(database_path)
    conn.close()

if __name__ == '__main__':
    nb_tables = get_number_of_tables()
    print('Nombre de tables: ' + str(nb_tables))
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Layers_rules")
    c.execute("DROP TABLE IF EXISTS DXF_Layers")
    c.execute("DROP TABLE IF EXISTS Layer")
    conn.commit()
    conn.close()
    nb_tables = get_number_of_tables()
    print('Nombre de tables: ' + str(nb_tables))
