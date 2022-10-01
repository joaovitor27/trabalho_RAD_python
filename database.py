import sqlite3


def get_db():
    conn = sqlite3.connect('database.sqlite')
    return conn


def create_table(sql: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.close()
    return "Table created success"


def query_db(query: str, args: tuple = (), one: bool = False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def insert_db(query: str, args: tuple = ()):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    conn.close()
    return 'inserido com sucesso'


def create_table_pessoa():
    result = create_table('CREATE TABLE IF NOT EXISTS people (id_person INTEGER PRIMARY KEY AUTOINCREMENT, '
                          'cpf VARCHAR(14) UNIQUE, first_name TEXT, middle_name TEXT, last_name TEXT, age integer,'
                          ' conta INTEGER UNIQUE, FOREIGN KEY (conta) references conta (number_conta))')
    return result


def create_table_conta():
    result = create_table('CREATE TABLE IF NOT EXISTS conta (id_conta INTEGER PRIMARY KEY AUTOINCREMENT, '
                          'agency INTEGER, number_conta INTEGER UNIQUE, saldo REAL, gerente TEXT, '
                          'titular TEXT)')
    return result


def insert_conta(agency: int, number_conta: int, saldo: float, gerente: str, titular: str):
    result = insert_db('INSERT INTO conta(agency, number_conta, saldo, gerente, titular) values (?,?,?,?,?);',
                       (agency, number_conta, saldo, gerente, titular))
    return result


def insert_pessoa(cpf: str, first_name: str, middle_name: str, last_name: str, age: int, conta:int):
    result = insert_db('INSERT INTO people(cpf, first_name, middle_name, last_name, age, conta) values (?,?,?,?,?,?);',
                       (cpf, first_name, middle_name, last_name, age, conta))
    return result


def delete_conta():
    pass


def delete_pessoa():
    pass


def put_conta():
    pass


def put_pessoa():
    pass


def get_pessoa():
    pass


def get_conta():
    pass


def get_pessoa_conta():
    pass


if __name__ == '__main__':
    print(create_table_conta())
    print(create_table_pessoa())
    print(insert_pessoa('06924290345', "João", "Vitor", "Monteiro", 21, 27))
