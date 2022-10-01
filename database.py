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
    return cur.rowcount


# def get_client_db(establishment, customer):
#     result = query_db('SELECT name FROM contacts WHERE number=? AND owner=? LIMIT 1',
#                       (str(customer.phone), establishment.owner), True)
#     return result
#
#
# def insert_client(customer, establishment):
#     result = insert_db('INSERT INTO contacts (owner, number, name) VALUES (?, ?, ?)',
#                        (str(establishment.owner), str(customer.phone), str(customer.name)))
#     return result


def create_table_pessoa():
    result = create_table('CREATE TABLE IF NOT EXISTS people (id_person INTEGER AUTO_INCREMENT, cpf VARCHAR(14), '
                          'first_name TEXT, middle_name TEXT, last_name TEXT, age integer,conta INTEGER, '
                          'FOREIGN KEY (conta) references conta (number_conta))')
    return result


def create_table_conta():
    result = create_table('CREATE TABLE IF NOT EXISTS conta (id_conta INTEGER AUTO_INCREMENT, agency INTEGER, '
                          'number_conta INTEGER, saldo REAL, gerente TEXT, titular TEXT)')
    return result


if __name__ == '__main__':
    print(create_table_conta())
    print(create_table_pessoa())
