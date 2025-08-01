import subprocess
import pandas as pd
import json
from datetime import datetime

def scrape_twitter(username, max_tweets=50):
    tweets = []
    try:
        # Exécute snscrape en CLI
        command = f"snscrape --jsonl --max-results {max_tweets} twitter-user {username}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Vérifie s'il y a une erreur
        if result.returncode != 0:
            print("Erreur d'exécution snscrape :")
            print(result.stderr)
            return pd.DataFrame()

        # Parse chaque ligne JSON
        for line in result.stdout.strip().split('\n'):
            data = json.loads(line)
            tweets.append({
                "source": "twitter",
                "text": data['content'],
                "date": datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m-%d %H:%M:%S"),
                "url": data['url']
            })

    except Exception as e:
        print(f"Erreur de scraping : {e}")

    return pd.DataFrame(tweets)
