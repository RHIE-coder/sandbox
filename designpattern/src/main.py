
TableName = str
Column = str
Value = str
Record = dict[Column, Value]
Table = list[Record]


class Context:

    __tables:dict[TableName, Table]

    def __init__(self):
        self.__tables = dict()

        users:Table = list()

        users.extend([
            dict(
                id = "1",
                name = "John",
                age = 30
            ),
            dict(
                id = "2",
                name = "Jane",
                age = 25
            )
        ])

        self.__tables['users'] = users
    
    def get_table(self, name:str)->Table:
        return self.__tables[name]
    
    def set_table(self, name:str, table:Table):
        self.__tables(name, table)

from abc import ABC, abstractmethod
from typing import Any

class Expression(ABC):
    @abstractmethod
    def interpret(ctx:Context)->Table:
        ...

class WhereExpression(Expression):
    __table_name:TableName
    __column:Column
    __operator:str
    __value:Any

    def __init__(self, table_name:str, column:str, operator:str, value:Any):
        self.__table_name = table_name
        self.__column = column
        self.__operator = operator
        self.__value = value
    
    def interpret(self, ctx:Context)->Table:
        result:Table = list()
        table:Table = ctx.get_table(self.__table_name)

        for record in table:
            if self.evaluate(record.get(self.__column), self.__operator, self.__value):
                result.append(record)
        
        return result
    
    def evaluate(self, column_value:Any, operator:str, value:str):
        if operator == '=':
            return column_value == value
        if operator == '>':
            return int(column_value) > int(value)
        if operator == '<':
            return int(column_value) < int(value)
        return False
    
class SelectExpression(Expression):
    __table_name:TableName
    __columns:list[Column]
    __where_clause:Expression

    def __init__(self, table_name:str, columns:list[str], where_clause:Expression):
        self.__table_name = table_name
        self.__columns = columns
        self.__where_clause = where_clause
    
    def interpret(self, ctx:Context)->Table:
        table:Table = ctx.get_table(self.__table_name)
        result:Table = list()

        for record in table:
            row_ctx:Context = Context()
            ...

class SQLParser:
    ...