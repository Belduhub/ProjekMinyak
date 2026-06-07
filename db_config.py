import mysql.connector
from mysql.connector import Error
import streamlit as st

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  
    'database': 'oil_gas_projects'
}

def get_database_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

def save_project(project_data):
    """Save project data to database"""
    connection = get_database_connection()
    if connection is None:
        return False
    
    try:
        cursor = connection.cursor()
        
        # Check if project name already exists
        check_query = "SELECT id FROM projects WHERE project_name = %s"
        cursor.execute(check_query, (project_data['project_name'],))
        existing = cursor.fetchone()
        
        if existing:
            # Update existing project
            update_query = """
                UPDATE projects SET
                    project_duration = %s,
                    capital_investment = %s,
                    non_capital_investment = %s,
                    production_year_1 = %s,
                    production_year_2 = %s,
                    production_year_3 = %s,
                    production_year_4 = %s,
                    production_year_5 = %s,
                    production_year_6 = %s,
                    production_year_7 = %s,
                    decline_rate = %s,
                    oil_price = %s,
                    opex_per_year = %s,
                    depreciation_method = %s,
                    tax_rate = %s,
                    discount_rate = %s
                WHERE project_name = %s
            """
            values = (
                project_data['project_duration'],
                project_data['capital_investment'],
                project_data['non_capital_investment'],
                project_data['production_year_1'],
                project_data['production_year_2'],
                project_data['production_year_3'],
                project_data['production_year_4'],
                project_data['production_year_5'],
                project_data['production_year_6'],
                project_data['production_year_7'],
                project_data['decline_rate'],
                project_data['oil_price'],
                project_data['opex_per_year'],
                project_data['depreciation_method'],
                project_data['tax_rate'],
                project_data['discount_rate'],
                project_data['project_name']
            )
            cursor.execute(update_query, values)
        else:
            # Insert new project
            insert_query = """
                INSERT INTO projects (
                    project_name, project_duration, capital_investment, non_capital_investment,
                    production_year_1, production_year_2, production_year_3, production_year_4,
                    production_year_5, production_year_6, production_year_7,
                    decline_rate, oil_price, opex_per_year, depreciation_method,
                    tax_rate, discount_rate
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                project_data['project_name'],
                project_data['project_duration'],
                project_data['capital_investment'],
                project_data['non_capital_investment'],
                project_data['production_year_1'],
                project_data['production_year_2'],
                project_data['production_year_3'],
                project_data['production_year_4'],
                project_data['production_year_5'],
                project_data['production_year_6'],
                project_data['production_year_7'],
                project_data['decline_rate'],
                project_data['oil_price'],
                project_data['opex_per_year'],
                project_data['depreciation_method'],
                project_data['tax_rate'],
                project_data['discount_rate']
            )
            cursor.execute(insert_query, values)
        
        connection.commit()
        return True
    except Error as e:
        st.error(f"Error saving project: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def load_project(project_name):
    """Load project data from database"""
    connection = get_database_connection()
    if connection is None:
        return None
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM projects WHERE project_name = %s"
        cursor.execute(query, (project_name,))
        result = cursor.fetchone()
        return result
    except Error as e:
        st.error(f"Error loading project: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_all_project_names():
    """Get list of all saved project names"""
    connection = get_database_connection()
    if connection is None:
        return []
    
    try:
        cursor = connection.cursor()
        query = "SELECT project_name FROM projects ORDER BY updated_at DESC"
        cursor.execute(query)
        results = cursor.fetchall()
        return [row[0] for row in results]
    except Error as e:
        st.error(f"Error fetching projects: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_project(project_name):
    """Delete a project from database"""
    connection = get_database_connection()
    if connection is None:
        return False
    
    try:
        cursor = connection.cursor()
        query = "DELETE FROM projects WHERE project_name = %s"
        cursor.execute(query, (project_name,))
        connection.commit()
        return True
    except Error as e:
        st.error(f"Error deleting project: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
