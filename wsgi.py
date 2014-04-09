from app import create_app

app = create_app('config')


if __name__ == '__main__':
    """
    Enable debug support. The server will reload itself on code changes,
    and it will also provide you with a helpful debugger if things go wrong.
    This makes it a major security risk and therefore it must never be used
    on production machines.
    """
    app.run()
