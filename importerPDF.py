
# Ruta del archivo PDF
pdf_path = 'Template_Crédito_Corporativo_Banco_BTG.pdf'


##sudo apt-get install imagemagick

from wand.api import library
from wand.image import Image

with Image(filename=pdf_path, resolution=200) as img:
    img.type = 'grayscale'
    img.compression = "lzw"
    # Manually iterate over all page, and turn off alpha channel.
    library.MagickResetIterator(img.wand)
    for idx in range(library.MagickGetNumberImages(img.wand)):
        library.MagickSetIteratorIndex(img.wand, idx)
        img.alpha_channel = 'off'
    img.save(filename="test.tiff")