# coding: utf-8

from app import create_app

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(
        debug=True,
        host='localhost',
        port=3000
    )
