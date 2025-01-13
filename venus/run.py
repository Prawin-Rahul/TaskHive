# Entry point for the backend
# import sys
# import os

# # Debugging: Print the current sys.path
# print(sys.path)

# # Add TaskHive directory to the module search path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app , db

app = create_app()

if __name__ == '__main__':

	with app.app_context():
		app.run(debug=True)
		db.create_all()
