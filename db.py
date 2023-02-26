import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('projects.db')
        self.cursor = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        """Create tasks table"""
        with open('tables.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        self.cursor.executescript(sql_script)
        self.con.commit()

    def create_project(self, job_id, client, project_name, location):
        """Create a new project"""
        self.cursor.execute(
            "INSERT INTO project_information(job_id, client, project_name, location) VALUES(?, ?, ?, ?)",
            (job_id, client, project_name, location))
        self.con.commit()

    def delete_project(self, job_id):
        """Create a new project"""
        self.cursor.execute("DELETE FROM project_information WHERE job_id = ?", (job_id,))
        self.con.commit()

    #
    #    # GETTING THE LAST ENTERED ITEM SO WE CAN ADD IT TO THE TASK LIST
    #    created_task = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE task = ? and completed = 0",
    #                                       (task,)).fetchall()
    #    return created_task[-1]
    #
    def get_project_information(self):
        """Get tasks"""
        project_details = self.cursor.execute(
            "SELECT job_id, client, project_name, location FROM project_information").fetchall()
        # completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()

        return project_details

    def get_borehole_list(self, job_id_to_fetch):
        """Get tasks"""
        borehole_list = self.cursor.execute(
            "SELECT hole_id, easting, northing, date FROM collars WHERE hole_id LIKE ?;""",
            [f"%{job_id_to_fetch}%"]).fetchall()
        # completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()

        return borehole_list

    def get_specific_project_information(self, job_id_to_fetch):
        """Get tasks"""
        specific_project = self.cursor.execute(
            """SELECT job_id, client, project_name, location FROM project_information WHERE job_id = ?;""",
            (job_id_to_fetch,))
        # completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()
        # print(self.cursor.fetchall()[0])

        return self.cursor.fetchall()[0]

    def get_specific_borehole_information(self, borehole_id_to_fetch):
        """Get tasks"""
        specific_project = self.cursor.execute(
            """SELECT * FROM collars WHERE hole_id = ?;""", (borehole_id_to_fetch,))
        # print(self.cursor.fetchall()[0])
        return self.cursor.fetchall()[0]

    # def mark_task_as_complete(self, taskid):
    #    """Marking tasks as complete"""
    #    self.cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (taskid,))
    #    self.con.commit()
    #
    # def mark_task_as_incomplete(self, taskid):
    #    """Mark task as uncomplete"""
    #    self.cursor.execute("UPDATE tasks SET completed=0 WHERE id=?", (taskid,))
    #    self.con.commit()
    #
    #    # return the text of the task
    #    task_text = self.cursor.execute("SELECT task FROM tasks WHERE id=?", (taskid,)).fetchall()
    #    return task_text[0][0]
    #
    # def delete_task(self, taskid):
    #    """Delete a task"""
    #    self.cursor.execute("DELETE FROM tasks WHERE id=?", (taskid,))
    #    self.con.commit()

    def close_db_connection(self):
        self.con.close()

    def update_collar_data(self, h_id, north, east, ele, start, end, dip, azi, logger, date, drill,
                           barrel, fluid, diameter):
        self.cursor.execute(
            "UPDATE collars SET hole_id = ?, easting = ?, northing = ?, elevation = ?, starting_depth = ?, "
            "ending_depth = ?, inclination = ?, azimuth = ?, logged_by = ?, date = ?, drill_model = ?, barrel_type = "
            "?, fluid = ?, diameter = ? WHERE hole_id = ?",
            (h_id, north, east, ele, start, end, dip, azi, logger, date, drill,
             barrel, fluid, diameter, h_id))
        self.con.commit()
