"""create task table

Revision ID: bb080af8e7c3
Revises: 
Create Date: 2024-02-07 18:23:43.516969

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bb080af8e7c3"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    status_table = op.create_table(
        "status",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
    )
    op.bulk_insert(status_table, [{"name": "not started"}, {"name": "complete"}])
    op.create_table(
        "task",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(1000), nullable=False),
        sa.Column(
            "status_id",
            sa.Integer,
            sa.ForeignKey("status.id"),
            nullable=False,
            default=1,
        ),
    )


def downgrade() -> None:
    op.drop_table("task")
    op.drop_table("status")
