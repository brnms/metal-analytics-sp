import pandas as pd

# 1. Load dataset
df = pd.read_csv("bandas_metal_sp.csv")

# 2. Calculate percentage of SP listeners relative to global total
df["sp_listeners_pct"] = (
    df["ouvintes_sao_paulo"] / df["ouvintes_mensais_global"]
) * 100
df["sp_listeners_pct"] = df["sp_listeners_pct"].round(2)

# 3. Estimated ticket-buying audience (using a average conversion rate of 2.5% of local listeners)
CONVERSION_RATE = 0.025
df["estimated_audience"] = (df["ouvintes_sao_paulo"] * CONVERSION_RATE).astype(
    int
)


# 4. Classify suitable venue in São Paulo based on estimated attendance
def recommend_venue(audience: int) -> str:
    if audience < 300:
        return "House of Legends / Manifesto Bar (~250-400)"
    elif audience < 800:
        return "Carioca Club / Hangar 110 (~800-1000)"
    elif audience < 2500:
        return "VIP Station / Audio (~1500-3000)"
    elif audience < 7000:
        return "Espaço Unimed / Terra SP (~7000-8000)"
    else:
        return "Allianz Parque Hall / Mercado Livre Arena Pacaembu (>10000)"


df["recommended_venue"] = df["estimated_audience"].apply(recommend_venue)

# Display core metrics
output_columns = [
    "banda",
    "ouvintes_sao_paulo",
    "sp_listeners_pct",
    "estimated_audience",
    "recommended_venue",
]
print(df[output_columns].head())