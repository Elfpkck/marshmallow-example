from base_app import api
from rest_api import blp

api.register_blueprint(blp)

if __name__ == "__main__":
    from base_app import app, db

    db.create_all()
    app.run(debug=True, host="0.0.0.0", port=12124)
