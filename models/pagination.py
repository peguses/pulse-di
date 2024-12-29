from pydantic import BaseModel


class PaginationInfo(BaseModel):
    total_count: int
    page: int
    page_size: int
    total_pages: int
