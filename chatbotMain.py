import psycopg2
from formDatabaseConnection import testDatabaseConnection

def openingMoves():
    print("")

def createResponse():
    print("Get Response")


def FirstResponse():
    print("Hello My Name Rok. What is your name?")
    getResponse()

def chatBotResponse():
    print()


def getResponse():
    userResponse = input()
    createResponse(userResponse)

if __name__ == '__main__':
    connectionResult = testDatabaseConnection()
    if (connectionResult):
        FirstResponse()
    else:
        print("Can not establish a connection")
