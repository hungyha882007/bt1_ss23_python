import os


def create_log_dir(dir_name):
    """
    Tạo thư mục nếu chưa tồn tại
    """

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Đã tạo thư mục: {dir_name}")
    else:
        print(f"Thư mục '{dir_name}' đã tồn tại")