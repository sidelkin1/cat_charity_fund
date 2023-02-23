from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):

    async def get_by_user(
            self,
            session: AsyncSession,
            user: User,
    ) -> List[Donation]:
        donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return donations.scalars().all()

    async def get_opened_for_investment(
            self,
            session: AsyncSession,
    ) -> List[Donation]:
        donations = await session.execute(
            select(Donation).where(
                Donation.fully_invested.is_(False)
            )
        )
        return donations.scalars().all()


donation_crud = CRUDDonation(Donation)
