from app import create_app

app = create_app()
app.run(debug=app.config['DEBUG'], port=5000, host='0.0.0.0')
