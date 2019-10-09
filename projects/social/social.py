"""
Objectives: Student should be able to demonstrate an 
            understanding of randomness and its applications.
"""

#
# Dependencies
#

import uuid
import random
from queue import Queue

#
# Define data structures
#

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself", userID, friendID)
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists", userID, friendID, self.friendships[userID], self.friendships[friendID])
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(numUsers):
            self.addUser(str(uuid.uuid4()))

        # Create friendships
        targetFriendCount = (numUsers * avgFriendships) // 2
        currentCount = 0
        collisions = 0

        count = 0
        while count < 20 and  currentCount < targetFriendCount:
            count += 1
            userID = random.randint(1, self.lastID)
            friendID = random.randint(1, self.lastID)

            if self.addFriendship(userID, friendID):
                currentCount += 2
            else:
                collisions += 1

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}

        q = Queue()
        q.enqueue(userID)

        while q.size() > 0:
            path = q.dequeue()
            friendID = path[-1]

            if friendID not in visited:
                visited[friendID] = path

                for friendID in self.friendships[friendID]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    print(f"SocialGraph users: {sg.users} friendships: {sg.friendships}")

    sg.populateGraph(10, 2)
    print(sg.friendships)

    # connections = sg.getAllSocialPaths(1)
    # print(connections)
