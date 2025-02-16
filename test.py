import uuid
from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel

def test_insert_and_read():
    cluster = Cluster(['localhost'])
    session = cluster.connect('test_keyspace')
	
    session.execute("INSERT INTO users (id, name) VALUES (1, 'Ekaterina')")
    # Проверяем, что запись вставлена
    rows = session.execute("SELECT id, name FROM users")

    for row in rows:
        print(f"Inserted row: id={row.id}, name={row.name}")  # Этот вывод появится в логах GitHub Actions

   
