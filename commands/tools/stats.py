import discord
import datetime

def setup(bot):
    @bot.tree.command(name="stats", description="Shows the bot's statistics.")
    async def stats(interaction: discord.Interaction):
        guild_count = len(bot.guilds)
        user_count = sum(guild.member_count for guild in bot.guilds)
        command_count = len(bot.tree.get_commands())
        
        uptime = datetime.datetime.utcnow() - bot.start_time
        uptime_str = str(uptime).split(".")[0]
        
        embed = discord.Embed(title="Bot Statistics", color=discord.Color.blue())
        embed.add_field(name="Guild Count", value=guild_count, inline=True)
        embed.add_field(name="User Count", value=user_count, inline=True)
        embed.add_field(name="Command Count", value=command_count, inline=True)
        embed.add_field(name="Ping", value=f"{round(bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="Uptime", value=uptime_str, inline=True)
        
        await interaction.response.send_message(embed=embed)
