import discord
import requests

# Paste your NEW Discord Bot Token here
TOKEN = "YOUR_TOKEN_HERE"

# Your GaiaNet Chemistry Endpoint
GAIA_ENDPOINT = "http://127.0.0.1:9068/v1/chat/completions"
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    print("🤖 Rag Bot is online!")


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    question = message.content

    try:
        response = requests.post(
            GAIA_ENDPOINT,
            headers={
                "Content-Type": "application/json"
            },
            json={
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                "max_tokens": 300
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        answer = data["choices"][0]["message"]["content"]

        if len(answer) > 1900:
            answer = answer[:1900] + "..."

        await message.channel.send(answer)

    except Exception as e:
        await message.channel.send(
            f"❌ Error contacting chemistry model:\n{str(e)}"
        )


client.run(TOKEN)
