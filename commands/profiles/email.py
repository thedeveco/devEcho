import discord
from discord import app_commands
from database.profile import profiledb

def setup(bot):
    @bot.tree.command(name="email", description="Enter your email for your profile")
    @app_commands.describe(email="Your email address")
    async def email(interaction: discord.Interaction, email: str):
        profiledb.save_email(interaction.user.id, email)
        await interaction.response.send_message(
            f"✅ Your email has been saved as: `{email}`", ephemeral=True
        )
    @bot.tree.command(name = "removeemail", description = "Remove your email from your profile")
    async def remove_email(interaction: discord.Interaction):
        if not profiledb.get_email(interaction.user.id):
            await interaction.response.send_message(
                "❌ You don't have an email saved in your profile", ephemeral=True
            )
            return
        profiledb.delete_email(interaction.user.id)
        await interaction.response.send_message(
            "✅ Your email has been removed from your profile", ephemeral=True
        )