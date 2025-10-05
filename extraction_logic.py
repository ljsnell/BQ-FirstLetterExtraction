import string

def extract_first_letters(input_string, output_file='first_letters.txt'):
    """
    Extract the first letter of each word from a string and write to a file.
    Preserves punctuation from the original string.
    
    Args:
        input_string: The string to process
        output_file: The name of the output text file (default: 'first_letters.txt')
    """
    result_chars = []
    words = input_string.split()
    
    for word in words:
        if word:
            # Get the first character (letter or punctuation)
            result_chars.append(word[0])
            
            # Check if there's trailing punctuation and add it
            for char in word[1:]:
                if char in string.punctuation:
                    result_chars.append(char)
    
    # Join the letters with spaces between them
    result = ' '.join(result_chars)
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(result)
    
    print(f"First letters extracted: {result}")
    print(f"Saved to: {output_file}")
    
    return result


# Example usage
if __name__ == "__main__":
    # Example string
    text = "Hello World!"
    
    # Extract and save first letters
    extract_first_letters(text)
    
    # You can also specify a custom output file
    # extract_first_letters(text, 'output.txt')