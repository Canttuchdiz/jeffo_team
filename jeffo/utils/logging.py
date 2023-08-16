from discord import Member, Embed, Color


class Logging:

    @staticmethod
    def ban_log(user: Member, reason: str) -> Embed:
        embed = Embed(title="Member Ban", color=Color.red())
        embed.set_author(name=user.name, icon_url=user.avatar.url)
        embed.add_field(name="Status", value="Banned")
        embed.add_field(name="Reason", value=reason)
        embed.set_footer(text=f"ID · {user.id}")
        return embed
