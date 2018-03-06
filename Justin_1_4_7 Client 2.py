#testing 123
import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
Basketball_file = os.path.join(directory, 'Basketball.JPG')

# Open and show the student image in a new Figure window
Basketball_img = PIL.Image.open(Basketball_file)
fig, axes = plt.subplots(1, 1)

# Display image in second axes and set window to the right eye
fig.show()