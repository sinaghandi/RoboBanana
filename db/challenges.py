from db.models import Challenge, ChallengeType
from sqlalchemy import select, update, insert, delete
from sqlalchemy.orm import sessionmaker     

def create_outgoing_challenge(
    user_id: int,
    opponent_id: int,
    channel_points: int,
    session: sessionmaker,
) -> None:
    if duplicate_challenge(user_id, opponent_id, session):
        raise Exception("There is already an ongoing prediction!")
    
    with session() as sess:
        sess.execute(
            insert(Challenge).values(
                user_id=user_id,
                opponent_id=opponent_id,
                channel_points=channel_points,
            )
        )

def accept_challenge(
    user_id: int,
    opponent_id: int,
    channel_points: int,
    challenge_type: ChallengeType,
    session: sessionmaker,
) -> bool:
    
def has_incoming_challenge(
    user_id: int,
    opponent_id: int,
    channel_points: int,
    challenge_type: ChallengeType,
    session: sessionmaker,
) -> bool:
    with session() as sess:
        stmt = (
            select(Challenge)
            .where(Challenge.user_id == opponent_id)
            .where(Challenge.opponent_id == user_id)
            .where(Challenge.accepted == True)
            .where(Challenge.ended == False)
            .where(Challenge.challenge_type == challenge_type)
        )
        result = sess.execute(stmt).all()


    if len(result) < 1:
        return False

def check_incoming_challenges(
    user_id: int,
    opponent_id: int,
    channel_points: int,
    session: sessionmaker,
) -> list:
    
def check_outgoing_challenges(
    user_id: int,
    opponent_id: int,
    channel_points: int,
    session: sessionmaker,
) -> list:
    
def duplicate_challenge(
    user_id: int,
    opponent_id: int,
    session: sessionmaker,
)