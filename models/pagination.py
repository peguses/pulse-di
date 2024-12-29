import strawberry


@strawberry.type
class PaginationInfo:
    total_count: int
    page: int
    page_size: int
    total_pages: int
