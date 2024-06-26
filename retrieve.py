import psycopg2
import json

# Database connection parameters
db_params = {
}


# Establish the connection
def connect(params):
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    print("Connected to the database")
    return conn, cursor


# Fetch the data from the database
# Execute the query
def fetc_data(cursor):
    cursor.execute("SELECT id, name, ST_AsGeoJSON(geom) as geom FROM countries;")
    rows = cursor.fetchall()
    return rows


# Construct GeoJSON FeatureCollection
def construct_geojson(rows):
    features = []
    for row in rows:
        feature = {
            "type": "Feature",
            "properties": {
                "id": row[0],
                "name": row[1]
            },
            "geometry": json.loads(row[2])
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    return geojson


# Deserialize the Json object into a dictionary
def deserialize_json(data):
    return json.loads(data)


# Close the database connection
def close(cur, conn):
    cur.close()
    conn.close()
    print("Connection closed")


# retrieve Data from the database and return GeoJSON as a dictionary
def retrieve_data():
    conn, cursor = connect(db_params)
    rows = fetc_data(cursor)
    geojson = construct_geojson(rows)
    close(cursor, conn)
    return geojson
