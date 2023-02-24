from sqlalchemy.ext.asyncio import AsyncSession


async def make_investment(source, crud, session: AsyncSession):
    free_amount = source.full_amount
    while True:
        target = await crud.get_opened_for_investment(session)
        if target is None:
            break
        need_amount = min(
            target.full_amount - target.invested_amount,
            free_amount
        )
        await crud.update_invested_amount(
            target, need_amount, session
        )
        source = await crud.update_invested_amount(
            source, need_amount, session
        )
        if source.fully_invested:
            break
        free_amount -= need_amount
    await session.commit()
    await session.refresh(source)
    return source
