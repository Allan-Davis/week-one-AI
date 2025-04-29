# CryptoBuddy: Your AI-Powered Financial Sidekick

# Step 1: Bot Personality
print("👋 Hey there! I'm CryptoBuddy — your eco-smart crypto sidekick! 💸🌱")
print("Ask me about trending coins, sustainability, or what’s best for long-term growth.")

# Step 2: Predefined Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Step 3–4: Rule-Based Logic
user_query = input("\n🤔 You: ").lower()

if "sustainable" in user_query:
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    print(f"🌱 CryptoBuddy: Go for {recommend}! It’s eco-friendly and has long-term potential!")
elif "trending" in user_query or "profit" in user_query:
    for coin, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["market_cap"] == "high":
            print(f"🚀 CryptoBuddy: {coin} is on the rise and popular! Might be worth watching.")
            break
elif "long-term" in user_query or "growth" in user_query:
    for coin, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["sustainability_score"] > 7:
            print(f"📈 CryptoBuddy: {coin} is trending up and ranks high in sustainability!")
            break
else:
    print("🤷 CryptoBuddy: I’m not sure about that. Try asking about trends or sustainability!")

# Step 5: Ethical Disclaimer
print("\n⚠️ Disclaimer: Crypto investments are risky — always do your own research before making financial decisions.")
