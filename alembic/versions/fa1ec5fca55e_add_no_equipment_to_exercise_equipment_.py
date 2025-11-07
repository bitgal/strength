"""Add NO_EQUIPMENT to Exercise.equipment enum

Revision ID: fa1ec5fca55e
Revises: 629606464aeb
Create Date: 2025-11-06 21:17:37.638484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'fa1ec5fca55e'
down_revision: Union[str, Sequence[str], None] = '629606464aeb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# revision identifiers, used by Alembic.
revision = 'fa1ec5fca55e'
down_revision = '629606464aeb'
branch_labels = None
depends_on = None

def upgrade():
    op.execute(
        "ALTER TABLE exercises MODIFY COLUMN equipment "
        "ENUM('bands', 'barbell', 'cable', 'dumbbell', 'e-z curl bar', "
        "'exercise ball', 'foam roll', 'kettlebells', 'machine', "
        "'medicine ball', 'other accessory', 'no equipment') NULL;"
    )

def downgrade():
    op.execute(
        "ALTER TABLE exercises MODIFY COLUMN equipment "
        "ENUM('bands', 'barbell', 'cable', 'dumbbell', 'e-z curl bar', "
        "'exercise ball', 'foam roll', 'kettlebells', 'machine', "
        "'medicine ball', 'other accessory') NULL;"
    )