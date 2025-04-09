import discord

def setup(bot):
    @bot.tree.command(name="ping", description="Replies with Pong and bot latency!")
    async def ping(interaction: discord.Interaction):
        latency = round(bot.latency * 1000)  
        await interaction.response.send_message(f"🏓 Pong! Latency: `{latency}ms`")
