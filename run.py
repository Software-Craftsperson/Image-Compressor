from app import app, db
from app.routes import main

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.register_blueprint(main)
    app.run(host='0.0.0.0', port=5000, debug=True)
