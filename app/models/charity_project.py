from sqlalchemy import Column, String, Text

from app.core.db import Base
from app.models.base import InvestmentMixin


class CharityProject(InvestmentMixin, Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
