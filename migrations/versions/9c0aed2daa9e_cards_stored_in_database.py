"""cards stored in database

Revision ID: 9c0aed2daa9e
Revises: d987f66e94bb
Create Date: 2018-08-30 18:17:02.980353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c0aed2daa9e'
down_revision = 'd987f66e94bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rank', sa.Enum('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', name='cardranks'), nullable=True),
    sa.Column('suit', sa.Enum('Heart', 'Spade', 'Club', 'Diamond', name='cardsuit'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('card_set',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('game', 'deck')
    op.drop_column('game', 'dealer_hand')
    op.drop_column('game', 'player_hand')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('player_hand', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('game', sa.Column('dealer_hand', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('game', sa.Column('deck', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_table('card_set')
    op.drop_table('card')
    # ### end Alembic commands ###
