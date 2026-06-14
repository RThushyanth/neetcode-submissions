class Twitter(object):

    def __init__(self):
        self.postdict = {}
        self.tweetcnt = 1
        self.followdict = {}
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        try:
            self.postdict[userId]
        except KeyError:
            self.postdict[userId] =[(self.tweetcnt,tweetId)]
        else:
            self.postdict[userId].append((self.tweetcnt,tweetId))
        
        self.tweetcnt = self.tweetcnt + 1

        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        try:
            self.postdict[userId]
        except KeyError:
            return []

        import heapq

        minheap = []
        tbc = min(10,len(self.postdict[userId]))
        if tbc > 0:
            minheap.extend([x for x in self.postdict[userId][-tbc:]])
            
        heapq.heapify(minheap)

        try:
            self.followdict[userId]
        except KeyError:
            maxheap = [(-1*x,y) for x,y in minheap]
            heapq.heapify(maxheap)

            ret = []

            for i in range(0,len(maxheap)):
                ret.append(heapq.heappop(maxheap)[1])
            return ret
        else:

            followerlist = list(self.followdict[userId].keys())

            for i in range(0,len(followerlist)):
                tbc = min(10,len(self.postdict[followerlist[i]]))
                for j in range(1,tbc+1):
                    tup = self.postdict[followerlist[i]][-1*j]
                    if len(minheap) == 10:
                        if tup[0] > minheap[0][0]:
                            heapq.heapreplace(minheap,tup)
                        else:
                            break
                    else:
                        heapq.heappush(minheap,tup)

            maxheap = [(-1*x,y) for x,y in minheap]
            heapq.heapify(maxheap)

            ret = []

            for i in range(0,len(maxheap)):
                ret.append(heapq.heappop(maxheap)[1])
            return ret

            


        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """

        if followerId == followeeId:
            return None

        try:
            self.followdict[followerId]
        except KeyError:
            self.followdict[followerId] = {}
            self.followdict[followerId][followeeId] = 1
        else:
            self.followdict[followerId][followeeId] = 1
        
        try:
            self.postdict[followerId]
        except KeyError:
            self.postdict[followerId] = []

        try:
            self.postdict[followeeId]
        except KeyError:
            self.postdict[followeeId] = []
            
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        try:
            self.followdict[followerId]
        except KeyError:
            return None
        else:
            try:
                self.followdict[followerId][followeeId]
            except KeyError:
                return None
            else:
                del self.followdict[followerId][followeeId]
                if len(self.followdict[followerId]) == 0:
                    del self.followdict[followerId]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)