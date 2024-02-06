# TODO: unsure if threading is needed here
from discord import User, Client, Interaction
from controllers.point_history_controller import PointHistoryController
from db import DB
from db.models import (
    ChallengeType,
)
from models.transaction import Transaction

# TODO: should this be create_challenge, or specific to coin flip?
class ChallengeController:
    @staticmethod
    async def create_challenge(
        challenge: ChallengeType,
        opponent: User,
        channel_points: int,
        interaction: Interaction,
        client: Client,
    ) -> bool:
        if channel_points <= 0:
            return await interaction.response.send_message(
                "You must wager a positive number of points!", ephemeral=True
            )

        point_balance = DB().get_point_balance(interaction.user.id)
        if channel_points > point_balance:
            return await interaction.response.send_message(
                f"You can only wager up to {point_balance} points", ephemeral=True
            )
        
        result, new_balance = DB().withdraw_points(interaction.user.id, channel_points)
        if not result:
            return await interaction.response.send_message(
                "Unable to retrieve points for wager - please try again!", ephemeral=True
            )
        # TODO: probably need limit of 1 challenge at a time per user, or at least challenge per unique pair of users
        success = DB().create_challenge_entry(
            interaction.guild_id, interaction.user.id, channel_points, opponent
        )
        if not success:
            await interaction.response.send_message(
                "Unable to create wager - please try again!", ephemeral=True
            )
            return False
        
        PointHistoryController.record_transaction(
            Transaction(
                interaction.user.id,
                -channel_points,
                point_balance,
                new_balance,
                f"Challenge: ({challenge})",
            )
        )
        
