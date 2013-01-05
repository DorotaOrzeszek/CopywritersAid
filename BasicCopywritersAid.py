import pygtk
pygtk.require("2.0")
import gtk
import pango

labelFont = pango.FontDescription("lucida bold 34")
textBoxFont = pango.FontDescription("lucida sans 56")

# Functions

def countWords(widget, data):
  global textBuffer
  start, end = textBuffer.get_bounds()
  text = textBuffer.get_text(start,end)
  wordlist = text.split()
  wordCount = len(wordlist)
  wordCounter.set_text("Words: " + str(wordCount))

def countChars(widget, data):
  global textBuffer
  start, end = textBuffer.get_bounds()
  text = textBuffer.get_text(start,end)
  charCount = len(text)
  charCounter.set_text("Chars: " + str(charCount))

def countLetters(widget, data):
  global textBuffer
  start, end = textBuffer.get_bounds()
  text = textBuffer.get_text(start,end)
  wordlist = text.split()
  textNoSpaces = "".join(wordlist)
  letterCount = len(textNoSpaces)
  letterCounter.set_text("Letters: " + str(letterCount))

# Main window

screen = gtk.VBox()
screen.set_size_request(1680,1050)
screen.set_border_width(30)

topRow = gtk.HBox(homogeneous=True)
wordCounter = gtk.Label("Words: 0")
wordCounter.modify_font(labelFont)
charCounter = gtk.Label("Chars: 0")
charCounter.modify_font(labelFont)
letterCounter = gtk.Label("Letters: 0")
letterCounter.modify_font(labelFont)

topRow.pack_start(wordCounter)
topRow.pack_start(charCounter)
topRow.pack_start(letterCounter)

mainRow = gtk.ScrolledWindow()

mainRow.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
mainRow.set_size_request(1000,800)

# Text box

textBox = gtk.TextView()
textBox.set_wrap_mode(gtk.WRAP_WORD)
textBox.modify_font(textBoxFont)
mainRow.add(textBox)

textBuffer = textBox.get_buffer()
textBuffer.connect("changed", countWords, None)
textBuffer.connect("changed", countChars, None)
textBuffer.connect("changed", countLetters, None)

screen.pack_start(topRow)
screen.pack_start(mainRow)

mainWindow = gtk.Window()
mainWindow.set_title("Basic Copywriter's Aid")
mainWindow.set_resizable(gtk.TRUE)
mainWindow.connect("destroy",gtk.mainquit,None)

mainWindow.add(screen)
mainWindow.show_all()
gtk.main()
