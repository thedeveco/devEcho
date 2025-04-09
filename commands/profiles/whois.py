import discord
from discord import app_commands
from database.profile import profiledb

def setup(bot):
    @bot.tree.command(name="whois", description="Get information about a user")
    @app_commands.describe(user="The user to lookup")
    async def whois(interaction: discord.Interaction, user: discord.User):
        email = profiledb.get_email(user.id)

        embed = discord.Embed(title=f"User Info: {user.name}", color=discord.Color.blue())
        embed.set_thumbnail(url=user.avatar.url if user.avatar else discord.Embed.Empty)
        embed.add_field(name="ID", value=user.id, inline=False)
        embed.add_field(name="Username", value=user.name, inline=False)
        embed.add_field(name="Email", value=email if email else "Not set", inline=False)

        await interaction.response.send_message(embed=embed)
