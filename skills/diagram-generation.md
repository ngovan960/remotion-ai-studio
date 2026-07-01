# Diagram Generation Skill

> Hướng dẫn AI vẽ diagram từ data

## Khi Nào Cần Diagram

| Situaction | Diagram Type | Ví dụ |
|------------|--------------|-------|
| Quy trình | Flowchart | Quy trình sản xuất |
| Timeline | Timeline | Lịch sử, sự kiện |
| So sánh | Bar chart | Số liệu đối chiếu |
| Tỷ lệ | Pie chart | Phần trăm |
| Xu hướng | Line graph | Dữ liệu theo thời gian |
| Cấu trúc | Hierarchy | Organization |
| Mối quan hệ | ERD | Database |

## Diagram Template

```yaml
diagram:
  type: [timeline|bar|pie|line|flowchart|hierarchy]
  title: "Tiêu đề"
  
  # Cho Timeline
  events:
    - time: "2020"
      label: "Sự kiện 1"
      icon: "star"
    - time: "2025"
      label: "Sự kiện 2"
      icon: "rocket"
  
  # Cho Bar/Pie
  data:
    - label: "Mục 1"
      value: 45
      color: "#3498db"
    - label: "Mục 2"
      value: 30
      color: "#e74c3c"
  
  # Cho Flowchart
  steps:
    - id: "start"
      label: "Bắt đầu"
      next: "step1"
    - id: "step1"
      label: "Bước 1"
      next: "end"
  
  # Style
  colors: ["#3498db", "#e74c3c", "#2ecc71", "#f39c12"]
  style: "modern"
```

## Diagram Rendering

### FFmpeg Commands

```bash
# Tạo ảnh diagram từ text
ffmpeg -f lavfi -i "color=c=white:s=1920x1080:d=1" \
  -vf "drawtext=text='Timeline':fontsize=72:x=960:y=540" \
  diagram.png
```

### Python (Pillow)

```python
from PIL import Image, ImageDraw, ImageFont

def create_timeline(events, output_path):
    img = Image.new('RGB', (1920, 1080), 'white')
    draw = ImageDraw.Draw(img)
    
    # Vẽ timeline
    y = 100
    for event in events:
        draw.text((100, y), event['time'], fill='black')
        draw.line([(200, y+10), (1800, y+10)], fill='gray', width=2)
        draw.text((250, y), event['label'], fill='black')
        y += 100
    
    img.save(output_path)
```

## Prompt Template

```
Create a [type] diagram showing [topic],
with [data points], colors: [palette],
modern clean style, 1920x1080
```
