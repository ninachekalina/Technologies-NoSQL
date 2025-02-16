from cassandra.cluster import Cluster

def test_insert_and_read():
    cluster = Cluster(['localhost'])
    session = cluster.connect('my_keyspace')
    
    session.execute("INSERT INTO users (id, name) VALUES (1, 'Katerina')")
    rows = session.execute("SELECT name FROM users WHERE id = 1")

    assert rows.one().name == 'Katerina'

