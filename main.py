from PIL import Image

def layer_images(base_path, overlay_path, output_path):
    # Open the base image
    base_image = Image.open(base_path)

    # Open the overlay image
    overlay_image = Image.open(overlay_path)

    # Ensure both images have the same mode and size
    overlay_image = overlay_image.convert('RGBA')
    overlay_image = overlay_image.resize(base_image.size)

    # Composite the images using paste
    result = Image.new('RGBA', base_image.size)
    result.paste(base_image.convert('RGBA'), (0, 0))
    result.paste(overlay_image, (0, 0), overlay_image)

    # Save the result
    result.save(output_path, 'PNG')

if __name__ == "__main__":
    base_image_path = "base.png"
    overlay_image_path = "made_by_mifella_gang.png"
    output_image_path = "result_image.png"

    layer_images(base_image_path, overlay_image_path, output_image_path)

    print(f"Images layered successfully. Result saved to {output_image_path}")
