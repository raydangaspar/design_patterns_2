import MySQLdb


class ConnectionFactory:

    def get_connection(self):
        connection = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='',
            db='alura'
        )

        return connection
