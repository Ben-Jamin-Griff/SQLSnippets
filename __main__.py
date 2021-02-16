from google.cloud import bigquery

fd = open('case-per-population.sql', 'r')
sqlFile = fd.read()
fd.close()

def query_stackoverflow():
    client = bigquery.Client()
    query_job = client.query(sqlFile)
    results = query_job.result()
    for row in results:
        print(row)

if __name__ == "__main__":
    query_stackoverflow()