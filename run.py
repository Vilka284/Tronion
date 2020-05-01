from server.app import create_app, sio

'''
main code to run app.py
'''

if __name__ == "__main__":
    sio.run(create_app())
