import psycopg2

class FunctionManager:
    def __init__(self, host, dbname, user, password, port=5432):
        self.conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        self.cursor = self.conn.cursor()

        # Create the 'agent_tool' table if it does not exist
        self._create_table()

    def _create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS agent_tool (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    function TEXT NOT NULL,
                    schema JSONB NOT NULL,
                    is_safe BOOLEAN NOT NULL
                )
            """)
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error creating table: {e}")

    def insert_function(self, name, function_code, schema, is_safe):
        try:
            sql = "INSERT INTO agent_tool (name, function, schema, is_safe) VALUES (%s, %s, %s, %s) RETURNING id"
            self.cursor.execute(sql, (name, function_code, schema, is_safe))
            self.conn.commit()
            return self.cursor.fetchone()[0]
        except psycopg2.Error as e:
            print(f"Error inserting function: {e}")
            # Handle the error, raise an exception, or log it based on your application's requirements

    def retrieve_function_by_id(self, function_id):
        try:
            sql = "SELECT id, name, function, schema, is_safe FROM agent_tool WHERE id = %s"
            self.cursor.execute(sql, (function_id,))
            result = self.cursor.fetchone()
            return result
        except psycopg2.Error as e:
            print(f"Error retrieving function by ID: {e}")

    def retrieve_functions_by_name(self, name):
        try:
            sql = "SELECT id, name, function, schema, is_safe FROM agent_tool WHERE name = %s"
            self.cursor.execute(sql, (name,))
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"Error retrieving functions by name: {e}")

    def retrieve_function_is_safe_by_name(self, name):
        try:
            sql = "SELECT function, is_safe FROM agent_tool WHERE name = %s"
            self.cursor.execute(sql, (name,))
            result = self.cursor.fetchone()
            return result if result else None  # Return the tuple of 'function' and 'is_safe' or None if not found
        except psycopg2.Error as e:
            print(f"Error retrieving function by name: {e}")

    def retrieve_function_by_function(self, function_code):
        try:
            sql = "SELECT id, name, function, schema, is_safe FROM agent_tool WHERE function = %s"
            self.cursor.execute(sql, (function_code,))
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"Error retrieving functions by function: {e}")

    def retrieve_function_by_is_safe(self, is_safe):
        try:
            sql = "SELECT id, name, function, schema, is_safe FROM agent_tool WHERE is_safe = %s"
            self.cursor.execute(sql, (is_safe,))
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"Error retrieving functions by is_safe: {e}")

    def retrieve_all_functions(self):
        try:
            sql = "SELECT id, name, function, schema, is_safe FROM agent_tool"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"Error retrieving all functions: {e}")

    def update_function_by_id(self, function_id, name=None, function_code=None, schema=None, is_safe=None):
        try:
            set_clause = ""
            values = []

            if name is not None:
                set_clause += "name = %s, "
                values.append(name)

            if function_code is not None:
                set_clause += "function = %s, "
                values.append(function_code)

            if schema is not None:
                set_clause += "schema = %s, "
                values.append(schema)

            if is_safe is not None:
                set_clause += "is_safe = %s, "
                values.append(is_safe)

            set_clause = set_clause.rstrip(", ")
            sql = f"UPDATE agent_tool SET {set_clause} WHERE id = %s"
            values.append(function_id)

            self.cursor.execute(sql, tuple(values))
            self.conn.commit()
            return self.cursor.rowcount
        except psycopg2.Error as e:
            print(f"Error updating functions by {set_clause}: {e}")

    def delete_function_by_id(self, function_id):
        try:
            sql = "DELETE FROM agent_tool WHERE id = %s"
            self.cursor.execute(sql, (function_id,))
            self.conn.commit()
            return self.cursor.rowcount
        except psycopg2.Error as e:
            print(f"Error retrieving functions by function_id: {e}")
    
    def _close_connection(self):
        self.cursor.close()
        self.conn.close()

    def close_connection(self):
        try:
            self._close_connection()
        except psycopg2.Error as e:
            print(f"Error closing connection: {e}")

    def __del__(self):
        self.cursor.close()
        self.conn.close()