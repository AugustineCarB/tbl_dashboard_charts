        import io
        import pandas as pd
        import requests

        def fetch_metric_data(api_key, metric_name):
            url = f"https://api.bitcoinmagazinepro.com/metrics/{metric_name}"
            headers = {'Authorization': f'Bearer {api_key}'}
        
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
                data = response.json()
                return data
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data: {e}")
                return None
        
        # Replace 'YOUR_API_KEY' with your actual API key
        api_key = 'aGVsbG9AbWlzZml0c2xpZnRpbmcuY2x1Yg==PUAuQD0=NzhkYTRiNTk='
        metric_name = 'realized-price'
        
        metric_data = fetch_metric_data(api_key, metric_name)
        if metric_data:
            print(f"\nData for metric '{metric_name}':", end="\n\n")
            # Load the data into a pandas DataFrame
            df = pd.read_csv(
                io.StringIO(metric_data),
                index_col=0,
            )
            print(df)
