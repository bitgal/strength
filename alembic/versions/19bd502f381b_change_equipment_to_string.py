"""change equipment to string

Revision ID: 19bd502f381b
Revises: fa1ec5fca55e
Create Date: 2025-11-06 21:42:22.296514

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19bd502f381b'
down_revision: Union[str, Sequence[str], None] = 'fa1ec5fca55e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


"""Change Exercise.equipment from ENUM to String

Revision ID: <new_revision_id>
Revises: fa1ec5fca55e
Create Date: 2025-11-06 21:50:00
"""


def upgrade():
    # Change column type from ENUM to VARCHAR(50)
    op.alter_column(
        'exercises',
        'equipment',
        type_=sa.String(length=50),
        existing_type=sa.Enum(
            'bands', 'barbell', 'cable', 'dumbbell', 'e-z curl bar',
            'exercise ball', 'foam roll', 'kettlebells', 'machine',
            'medicine ball', 'other accessory', 'no equipment',
            name='equipment'
        ),
        existing_nullable=True
    )

def downgrade():
    # Change it back to ENUM if needed
    op.alter_column(
        'exercises',
        'equipment',
        type_=sa.Enum(
            'bands', 'barbell', 'cable', 'dumbbell', 'e-z curl bar',
            'exercise ball', 'foam roll', 'kettlebells', 'machine',
            'medicine ball', 'other accessory', 'no equipment',
            name='equipment'
        ),
        existing_type=sa.String(length=50),
        existing_nullable=True
    )

