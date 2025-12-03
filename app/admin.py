from sqladmin import Admin, ModelView
from app.database.database import engine
from app.models.image import Image
from fastapi import FastAPI


class ImageView(ModelView, model=Image):
    column_list = [
        "id",
        "filename",
        "original_filename",
        "file_path",
        "file_size",
        "mime_type",
        "title",
        "description",
        "width",
        "height",
        "created_at",
        "is_active",
        "storage_type",
        "storage_path",
    ]
    column_searchable_list = ["filename", "title", "description"]
    column_sortable_list = ["id", "created_at", "file_size"]
    column_default_sort = ("created_at", True)


def init_admin(app: FastAPI):
    admin = Admin(app, engine)
    admin.add_view(ImageView)
