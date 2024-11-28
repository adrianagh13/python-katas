class Dictionary:
    def __init__(self) -> None:
        self.words = {}

    def newentry(self, word, meaning):
        self.words[word] = meaning
    
    def look(self, word):
        return self.words.get(word, f"There's no such word on the dictionary {word}")