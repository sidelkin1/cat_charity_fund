import itertools
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession


def update_amount(target, amount: int) -> bool:
    target.invested_amount += amount
    if target.full_amount == target.invested_amount:
        target.fully_invested = True
        target.close_date = datetime.now()
        return True
    return False


async def make_investment(source, crud, session: AsyncSession):
    targets = await crud.get_opened_for_investment(session)
    if not targets:
        return source

    free_amount = source.full_amount
    for last, target in enumerate(targets):
        need_amount = min(
            target.full_amount - target.invested_amount,
            free_amount
        )
        update_amount(target, need_amount)
        if update_amount(source, need_amount):
            break
        free_amount -= need_amount

    session.add_all(itertools.chain([source], targets[:last + 1]))
    await session.commit()
    await session.refresh(source)
    return source