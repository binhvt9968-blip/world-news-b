"""Original typographic poster for verified news of 21 November 2026.

Drawn from scratch. No photographs, logos, or existing artwork.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (243, 234, 215)
INK = (22, 21, 19)
RED = (163, 32, 21)
MUTED = (92, 86, 76)
LINE = (210, 196, 170)

FONT = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def glyph(draw, kind, cx, cy):
    """Small geometric marks, drawn as plain strokes."""
    ink = INK
    if kind == "orbit":
        draw.ellipse((cx - 16, cy - 16, cx + 16, cy + 16), outline=ink, width=3)
        draw.ellipse((cx - 4, cy - 4, cx + 4, cy + 4), fill=RED)
        draw.ellipse((cx - 34, cy - 10, cx + 34, cy + 10), outline=ink, width=2)
    elif kind == "talks":
        draw.arc((cx - 28, cy - 20, cx + 8, cy + 16), 200, 80, fill=ink, width=3)
        draw.arc((cx - 8, cy - 16, cx + 28, cy + 20), 100, 340, fill=RED, width=3)
    elif kind == "rain":
        for i, dy in enumerate((-16, 0, 16)):
            color = RED if i == 2 else ink
            draw.arc((cx - 26, cy + dy - 8, cx + 26, cy + dy + 8), 200, 340, fill=color, width=3)
    elif kind == "pitch":
        draw.ellipse((cx - 20, cy - 20, cx + 20, cy + 20), outline=ink, width=3)
        draw.line((cx, cy - 20, cx, cy + 20), fill=ink, width=2)
        draw.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), outline=RED, width=3)
    elif kind == "down":
        draw.line((cx - 26, cy - 16, cx - 8, cy - 4), fill=ink, width=3)
        draw.line((cx - 8, cy - 4, cx + 6, cy + 8), fill=ink, width=3)
        draw.line((cx + 6, cy + 8, cx + 26, cy + 18), fill=RED, width=3)
        draw.polygon(
            [(cx + 16, cy + 8), (cx + 28, cy + 20), (cx + 12, cy + 22)],
            fill=RED,
        )
    elif kind == "link":
        draw.rounded_rectangle((cx - 30, cy - 12, cx - 2, cy + 12), radius=8, outline=ink, width=3)
        draw.rounded_rectangle((cx + 2, cy - 12, cx + 30, cy + 12), radius=8, outline=RED, width=3)


def main():
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, W, 18), fill=INK)
    draw.rectangle((0, H - 18, W, H), fill=INK)

    date_font = font(FONT, 58)
    sub_font = font(FONT_REG, 28)
    kicker_font = font(FONT, 20)
    label_font = font(FONT, 32)
    num_font = font(FONT, 22)

    date = "21 tháng 11 năm 2026"
    draw.text((56, 48), date, font=date_font, fill=INK)
    draw.text((56, 118), "Thứ Bảy", font=sub_font, fill=MUTED)
    draw.rectangle((56, 168, 968, 174), fill=RED)

    rows = [
        ("01", "Khoa học", "BepiColombo vào quỹ đạo Sao Thủy", "orbit"),
        ("02", "Khí hậu", "COP31 bế tắc vì nhiên liệu hóa thạch", "talks"),
        ("03", "Thiên tai", "Mưa tiếp diễn, lũ Florida", "rain"),
        ("04", "Thể thao", "Chelsea 1-4 Leeds, Ngoại hạng Anh", "pitch"),
        ("05", "Kinh tế", "Cổ phiếu AI giảm mạnh trong tuần", "down"),
        ("06", "Chính trị", "Anh–EU: nông sản, carbon, thanh niên", "link"),
    ]

    top = 198
    row_h = 118
    for i, (num, kicker, label, kind) in enumerate(rows):
        y = top + i * row_h
        if i:
            draw.line((56, y, 968, y), fill=LINE, width=1)
        draw.text((56, y + 28), num, font=num_font, fill=RED)
        draw.text((112, y + 22), kicker.upper(), font=kicker_font, fill=MUTED)
        draw.text((112, y + 52), label, font=label_font, fill=INK)
        glyph(draw, kind, 910, y + 58)

    note_font = font(FONT_REG, 18)
    note = "Mỗi dòng đã đối chiếu từ ít nhất hai nguồn. Hình vẽ gốc, không ảnh, không logo."
    draw.text((56, 968), note, font=note_font, fill=MUTED)

    out = "poster-21-11-2026.png"
    image.save(out, "PNG", optimize=True)
    print(out, image.size)


if __name__ == "__main__":
    main()
