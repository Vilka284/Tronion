from server import app

'''
main code to run app.py
'''

if __name__ == "__main__":
    app.create_app().run(port=5500)
