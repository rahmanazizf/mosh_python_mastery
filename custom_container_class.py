class TagCloud:
    """
    A custom container which is slightly smarter than an usual dictionary

    """
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        """
        Object method that adds counting in custom container.

        Parameter:
        self: a reference to the current object
        tag: tag to count (str)
        """
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    
    def __getitem__(self, tag):
        """
        Returns the counting of respective tag.
        
        Parameter
        tag: the key of a certain value (str)
        """
        return self.tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, nitems):
        """
        Declare the number of a tag.

        tag: a key of certain value (str)
        nitems: number of items (int)
        """
        self.tags[tag] = nitems

    def __len__(self):
        """
        Allowing the container to returns its number of elements.
        """
        return len(self.tags)
    
    def __iter__(self):
        """
        Makes the custom container to be an iterable.
        """
        return iter(self.tags)

    def __str__(self):
        """
        Returns elements in container in string.
        """
        return str(self.tags)





cloud = TagCloud()
cloud.add("python")
cloud.add("PyThon")
cloud.add("pYtHoN")


