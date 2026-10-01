class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = []
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follows[userId].add(userId)
        c = 0
        feed = []

        for i in range(len(self.tweets) - 1, -1, -1):
            if self.tweets[i][0] in self.follows[userId]:
                feed.append(self.tweets[i][1])
                c += 1
            
            if c == 10:
                break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
