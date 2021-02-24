if __name__ == '__main__':
    from src import create_app
    app = create_app()
    app.run(debug=True)
