import qrcode
from PIL import Image
import matplotlib.pyplot as plt


def get_qrcode(strs, logo, name):
    """
    Generate a QRcode with a logo on it
    :param strs: QrCode content
    :param logo: logo image file(*.png)
    :param name: result file(*.png)
    :return: image
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=16,
        border=2,
    )
    # 添加数据
    qr.add_data(strs)
    # 填充数据
    qr.make(fit=True)
    # 生成图片
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("RGBA")  # RGBA
    # 添加logo
    icon = Image.open(logo)
    # 获取图片的宽高
    img_w, img_h = img.size
    factor = 5
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), icon)
    # 显示图片
    plt.imshow(img)
    plt.show()
    img.save(name)
    return img


def simple_qr(str, name):
    """
    Generate a simple QrCode
    :param str: content
    :param name: filename(*.png)
    :return: image
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
    qr.add_data(str)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(name)
    return img


if __name__ == '__main__':
    get_qrcode("https://m.viinet.com/activity/unlogin", "./logo.png", './at_qrimage.png')
