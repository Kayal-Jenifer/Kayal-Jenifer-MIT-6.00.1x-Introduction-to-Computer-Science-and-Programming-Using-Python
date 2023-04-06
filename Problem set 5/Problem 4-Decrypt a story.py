# For this problem, the graders will use our implementation of the Message,
# PlaintextMessage, and CiphertextMessage classes, so don't worry if you did not
# get the previous parts correct.

# Now that you have all the pieces to the puzzle, please use them to decode the
# file story.txt. The file ps6.py contains a helper function get_story_string()
# that returns the encrypted version of the story as a string. Create a
# CiphertextMessage object using the story string and use decrypt_message to
# return the appropriate shift value and unencrypted story string.

# Paste your code here...

def decrypt_story():
    x = CiphertextMessage(get_story_string())
    return x.decrypt_message()
