# A class representing a book file that has been read.
# The stored state are the title, author, isbn, and a map from word to
# frequency.
class TextDoc:
  def __init__(self, filepath):
    doc = open(filepath, 'r')
    # Note: rstrip gets rid of trailing newline
    # (either \n on Unix or \r\n on Windows)
    self.title = doc.readline().rstrip()
    self.author = doc.readline().rstrip()
    self.isbn = doc.readline().rstrip()
    d = doc.readline()
    if d != ">>>>>\n" and d != ">>>>>\r\n":
      print "File not formatted correctly."

    self.frequencies = {}
    # Read the actual content of the story.
    for line in doc:
      # Convert all words to lowercase
      words = map(lambda s: s.lower(), line.split())
      for word in words:
        w = word
        # Get rid of starting punctuation
        while len(w) > 0 and not w[0].isalpha():
          w = w[1:]
        # Get rid of trailing punctuation
        while len(w) > 0 and not w[-1].isalpha():
          w = w[:-1]
        if len(w) == 0:
          continue
        if w in self.frequencies:
          self.frequencies[w] += 1
        else:
          self.frequencies[w] = 1
    doc.close()      

  def get_frequencies(self):
    return self.frequencies

  def get_author(self):
    return self.author

  def get_title(self):
    return self.title

  def get_isbn(self):
    return self.isbn

# Test
#t = TextDoc("./data/books/Brown Bear, Brown Bear, What Do You See.txt")
#print t.frequencies
#print t.get_author()
#print t.get_title()
