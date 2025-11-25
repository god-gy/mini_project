from sqlalchemy.ext.asyncio import AsyncSession
from my_blog_api.app.schemas.post import PostCreate

async def get_posts_from_db(db: AsyncSession):
        return [
                {"id": 1, "title": "title 1", "content": "content 1", "owner_id": 1},
                {"id": 2, "title": "title 2", "content": "content 2", "owner_id": 2},
        ]


async def create_post(
        db: AsyncSession,
        data: PostCreate,
        owner_id: int,
        ):
        title = data.title
        content = data.content
        user_id = owner_id

        # sqlalchemy 써서 save 했다고 치고

        return True
