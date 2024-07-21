import pyperclip

def copy_to_clipboard(input_text):
    # Copy the input text to the clipboard
    pyperclip.copy(input_text)
    print("Text copied to clipboard:", input_text)

if __name__ == "__main__":
    user_input = input("Enter the text you want to copy: ")
    copy_to_clipboard(user_input)
