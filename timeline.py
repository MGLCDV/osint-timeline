from modules.twitter_scraper import scrape_twitter
import matplotlib.pyplot as plt
import pandas as pd
import os

# Crée les dossiers si besoin
os.makedirs("output", exist_ok=True)

# Utilisateur cible
username = "elonmusk"
max_tweets = 50

# Récupération des données Twitter
df = scrape_twitter(username, max_tweets)

# Tri par date
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Affichage d'une timeline simple
plt.figure(figsize=(10, 5))
plt.plot(df["date"], range(len(df)), marker='o', linestyle='-', color='blue')
plt.title(f"Timeline d'activité Twitter - @{username}")
plt.xlabel("Date")
plt.ylabel("Tweet #")
plt.grid(True)
plt.tight_layout()
plt.savefig(f"output/timeline_{username}.png")
plt.show()
