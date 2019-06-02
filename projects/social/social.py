import random

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

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
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
    # Time Complexity: O(numUsers^2)
    # Space Complexity: O(numUsers^2)
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

        # Add user
        # Time Complexity: O(numUsers)
        # Space Complexity: O(numUsers)
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        # avgFriendships = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
        # Time Complexity: O(numUsers^2)
        # Space Complexity: O(numUsers^2)
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        # print(possibleFriendships)

        # Time Complexity: O(numUsers^2)
        # Space Complexity: O(1)
        random.shuffle(possibleFriendships)
        # print(possibleFriendships)

        # Time Complexity: O(avgFriendships * numUsers // 2)
        # Space Complexity: O(avgFriendships * numUsers // 2)
        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            # print(friendship)
            self.addFriendship(friendship[0], friendship[1])


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {userID: [userID]}  # Note that this is a dictionary, not a set
        friendship_network = []
        friendship_network.append([userID])

        while friendship_network:
            path = friendship_network.pop()
            #print(f"path {path}")
            user = path[-1]
            #print(f"user {user}")
            
            for friend in self.friendships[user]:
                if friend not in visited:
                    connected_path = path + [friend]
                    #print(f"connected_path {connected_path}")
                    visited[friend] = connected_path
                    friendship_network.append(connected_path)
                    #print(f"friendship_network {friendship_network}")
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # print(sg.users)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
