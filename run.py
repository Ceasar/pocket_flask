import os

from app import create_app


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    """
    Enable debug support. The server will reload itself on code changes,
    and it will also provide you with a helpful debugger if things go wrong.
    This makes it a major security risk and therefore it must never be used
    on production machines.
    """
    app = create_app()
    app.debug = True
    app.run(host='0.0.0.0', port=port)
