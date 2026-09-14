from api_client import fetch_data

def run_pipeline():
    limit = 100

    for page in range(3):
        offset = page * limit

        print(f"\nFetching page {page + 1}")
        print(f"Offset: {offset}")

        data = fetch_data(
            limit=limit,
            offset=offset
        )

        if data is None:
            print("Pipeline stopped: no data received.")
            return

        records = data
        print("Records received:", len(records))
        
if __name__ == "__main__":
    run_pipeline()