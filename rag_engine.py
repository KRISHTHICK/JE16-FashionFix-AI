import random

# Simulate RAG engine using predefined knowledge (or load from PDF in real use)
def fetch_repair_suggestions(query):
    samples = {
        "image_based_repair": "It looks like this could benefit from fabric patches or embroidery to cover the damage.",
        "torn sleeve": "You can cut the sleeves evenly for a sleeveless look or stitch them with a contrasting fabric.",
        "faded jeans": "Try dyeing them darker or upcycle them into shorts or bags.",
    }
    for key in samples:
        if key in query.lower():
            return samples[key]
    return "Try adding modern accessories or use denim patches to refresh the look."
