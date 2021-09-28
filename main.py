import discord
import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio

Create a backup
        __Examples__
        ```{c.prefix}backup create```
        """
        backup_count = await ctx.db.backups.count_documents({"creator": ctx.author.id})
        if backup_count >= max_backups:
            raise cmd.CommandError("You have **exceeded the maximum count** of backups.\n\n"
                                   f"Upgrade to Pro (`x!pro`) to be able to create more than **{max_backups}**. "
                                   f"backups **or delete one of your old backups** (`x!backup list` "
                                   f"& `x!backup delete <id>`).")

        status = await ctx.send(**ctx.em("**Creating backup** ... Please wait", type="working"))
        handler = BackupSaver(self.bot, self.bot.session, ctx.guild)
        backup = await handler.save()
        id = await self._save_backup(ctx.author.id, backup)

        embed = ctx.em(f"Successfully **created backup** with the id `{id}`.\n", type="success")["embed"]
        embed.add_field(name="Usage",
                        value=f"```{ctx.prefix}backup load {id}```\n```{ctx.prefix}backup info {id}```")
        await status.edit(embed=embed)
        try:
            if ctx.author.is_on_mobile():
                await ctx.author.send(f"{ctx.prefix}backup load {id}")

            else:
                embed = ctx.em(
                    f"Created backup of **{ctx.guild.name}** with the backup id `{id}`\n", type="info")["embed"]
                embed.add_field(name="Usage",
                                value=f"```{ctx.prefix}backup load {id}```\n```{ctx.prefix}backup info {id}```")
                await ctx.author.send(embed=embed)

        except Exception:
            pass

    @backup.command(aliases=["l"])
    @cmd.guild_only()
    @cmd.has_permissions(administrator=True)
    @cmd.bot_has_permissions(administrator=True)
    @checks.bot_has_managed_top_role()
    @cmd.cooldown(1, 5 * 60, cmd.BucketType.guild)
    async def load(self, ctx, backup_id, *options):
        """
        Load a backup
        __Arguments__
        **backup_id**: The id of the backup or the guild id of the latest automated backup
        **options**: A list of options (See examples)
        __Examples__
        Default options: ```{c.prefix}backup load oj1xky11871fzrbu```
        Only roles: ```{c.prefix}backup load oj1xky11871fzrbu !* roles```
        Everything but bans: ```{c.prefix}backup load oj1xky11871fzrbu !bans```
        """
        backup_id = str(ctx.guild.id) if backup_id.lower() == "interval" else backup_id
        backup = await self._get_backup(backup_id)
        if backup is None or backup.get("creator") != ctx.author.id:
            raise cmd.CommandError(f"You have **no backup** with the id `{backup_id}`.")

client.run(os.getenv('ODg0NjY1NDk1MTg0MzQzMDgw.YTby8g.nF94UTk_TA8hfQu290DCpipxS-E'))
