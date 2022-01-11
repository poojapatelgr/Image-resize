from PIL import Image
from resizeimage import resizeimage
import argparse
import os

def resizeimg(imgf,opts):
    fd_img = open(imgf, 'rb')
    img = Image.open(fd_img)
    imgbase = os.path.basename(imgf)
    imgnum = imgbase.split(".")
    print(imgnum)
    img = resizeimage.resize_contain(img, [365, 480])
    img = img.convert("RGB")
    oimg = f'{opts.output}/{opts.prefix}{imgnum[0]}.jpg'
    print(oimg)
    img.save(oimg, img.format)
    fd_img.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', help='Input folder')
    parser.add_argument('-o','--output', help='output folder')
    parser.add_argument('-p','--prefix', help='prefix')
    #opts = parser.parse_args('-i foo.pdf -o x.pdf -t 12 -p 6 1 2 12 3 5 2 8')
    opts = parser.parse_args()

    os.makedirs(opts.output, exist_ok=True)
    l = []
    for (root,dirs,files) in os.walk(opts.input):
        for f in files:
            l.append(f'{root}/{f}')
    print(l)

    for img in l:
        resizeimg(img, opts)


if __name__ == '__main__':
    main()
