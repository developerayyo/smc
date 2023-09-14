from PIL import Image
import os

# Replace 'input_folder' with the path to your folder containing images
input_folder = 'path_to_your_input_folder'

# Replace 'output_folder' with the path where you want to save optimized images
output_folder = 'path_to_your_output_folder'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Define the maximum width and height for your optimized images
max_width = 1200
max_height = 800

# Iterate through the files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        try:
            # Open the image
            img = Image.open(os.path.join(input_folder, filename))
            
            # Resize the image while preserving the aspect ratio
            img.thumbnail((max_width, max_height))
            
            # Save the optimized image to the output folder
            img.save(os.path.join(output_folder, filename))
            
            print(f"Optimized: {filename}")
        
        except Exception as e:
            print(f"Error optimizing {filename}: {e}")

print("Optimization complete.")
