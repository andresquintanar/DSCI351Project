import sys
from pymongo import MongoClient

# argv[1] is the dataCollection
# argv[2] is the attribute 
# argv[3] is what to compare to

def find(db, attr, test):
  listOfAttributes = ['firstName', 'lastName', 'uscID', 'uscEmail', 'major', 'gradYear', 'occupation', 'gpa', 'username', 'password']
  outputList = []
  if attr not in listOfAttributes:
    return ["Error, invalid attribute input!"]

  
def main():
  find(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
  main()
