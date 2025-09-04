from PIL import Image, ImageEnhance
import os

def create_white_logo(input_path, output_path):
    """Convert a color logo to white while maintaining transparency."""
    try:
        img = Image.open(input_path).convert("RGBA")
        
        # Create a new white image with the same size and alpha channel
        white_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
        
        # Get the alpha channel from the original image
        alpha = img.split()[3]
        
        # Create a white version of the image
        white_img.paste((255, 255, 255, 255), (0, 0), img)
        
        # Restore the alpha channel
        r, g, b, _ = white_img.split()
        white_img = Image.merge('RGBA', (r, g, b, alpha))
        
        # Save the result
        white_img.save(output_path, "PNG")
        print(f"Created white logo: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error creating white logo: {e}")
        return False

def create_favicon(input_path, output_path, size):
    """Create a favicon from the input image."""
    try:
        img = Image.open(input_path).convert("RGBA")
        
        # Resize the image
        img = img.resize((size, size), Image.LANCZOS)
        
        # Save the result
        img.save(output_path, "PNG")
        print(f"Created favicon ({size}x{size}): {output_path}")
        return True
        
    except Exception as e:
        print(f"Error creating favicon: {e}")
        return False

def main():
    # Define paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    images_dir = os.path.join(base_dir, 'images')
    
    # Create stacked white logo
    stacked_color_path = os.path.join(images_dir, 'logo_stacked_color.png')
    stacked_white_path = os.path.join(images_dir, 'logo_stacked_white.png')
    
    if os.path.exists(stacked_color_path) and not os.path.exists(stacked_white_path):
        create_white_logo(stacked_color_path, stacked_white_path)
    
    # Create favicons from the horizontal color logo
    favicon_sizes = [16, 32, 64]
    favicon_path = os.path.join(images_dir, 'logo_horizontal_color.png')
    
    if os.path.exists(favicon_path):
        for size in favicon_sizes:
            output_path = os.path.join(images_dir, f'favicon_{size}x{size}.png')
            if not os.path.exists(output_path):
                create_favicon(favicon_path, output_path, size)
    
    # Apple Touch Icon generation removed as per user request

if __name__ == "__main__":
    main()
