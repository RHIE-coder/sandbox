from abc import ABC, abstractmethod

class Connection(ABC):
    def open(self):
        ...
    def close(self):
        ...

class Command(ABC):
    def execute(self, query:str):
        ...

class ResultSet(ABC):
    def get_results(self):
        ...


class DatabaseFactory(ABC):
    def create_connection(self)->Connection:
        ...
    def create_command(self)->Command:
        ...
    def create_resultset(self)->ResultSet:
        ...

class MySQLConnection(Connection):
    def open(self):
        print("MySQL connection is opened")
    
    def close(self):
        print("MySQL connection is closed")

class MySQLCommand(Command):
    def execute(self, query:str):
        print(f"Executing MySQl query: {query}")

class MySQLResultSet(ResultSet):
    def get_results(self):
        print("Getting results from MySQL database")


class PostgreSQLConnection(Connection):
    def open(self):
        print("PostgreSQL connection is opened")
    
    def close(self):
        print("PostgreSQL connection is closed")

class PostgreSQLCommand(Command):
    def execute(self, query:str):
        print(f"Executing PostgreSQL query: {query}")

class PostgreSQLResultSet(ResultSet):
    def get_results(self):
        print("Getting results from PostgreSQL database")

class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self)->Connection:
        ...
    
    @abstractmethod
    def create_command(self)->Command:
        ...

    @abstractmethod
    def create_resultset(self)->ResultSet:
        ...

class MySQLFactory(DatabaseFactory):
    def create_connection(self)->MySQLConnection:
        return MySQLConnection()
    
    def create_command(self)->MySQLCommand:
        return MySQLCommand()
    
    def create_resultset(self)->MySQLResultSet:
        return MySQLResultSet()
    
class PostgreFactory(DatabaseFactory):
    def create_connection(self)->PostgreSQLConnection:
        return PostgreSQLConnection()
    
    def create_command(self)->PostgreSQLCommand:
        return PostgreSQLCommand()
    
    def create_resultset(self)->PostgreSQLResultSet:
        return PostgreSQLResultSet()


class DatabaseClient:
    __connection:Connection
    __command:Command
    __resultset:ResultSet

    def __init__(self, factory: DatabaseFactory):
        self.__connection = factory.create_connection()
        self.__command = factory.create_command()
        self.__resultset = factory.create_resultset()
    
    def perform_database_operations(self):
        self.__connection.open()
        self.__command.execute("SELECT * FROM users")
        self.__resultset.get_results()
        self.__connection.close()

if __name__ == "__main__":
    mysql_client = DatabaseClient(MySQLFactory())
    mysql_client.perform_database_operations()

    postgre_client = DatabaseClient(PostgreFactory())
    postgre_client.perform_database_operations()

    