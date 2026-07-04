import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


# 1. Fayl yolları
image_path = "data/raw/sample.jpg"
output_dir = "outputs/day03"

os.makedirs(output_dir, exist_ok=True)


# 2. Şəkili oxu
img = cv2.imread(image_path)


# 3. Şəkil oxunubmu yoxla
if img is None:
    raise FileNotFoundError(f"Şəkil oxunmadı. Path-i yoxla: {image_path}")


# 4. Əsas array məlumatları
print("Type:", type(img))
print("Shape:", img.shape)
print("Dtype:", img.dtype)
print("Number of dimensions:", img.ndim)
print("Total number of elements:", img.size)


# 5. Shape məlumatını ayrı dəyişənlərə böl
height, width, channels = img.shape

print("Height:", height)
print("Width:", width)
print("Channels:", channels)


# 6. Pixel statistikası
print("Min pixel value:", img.min())
print("Max pixel value:", img.max())
print("Mean pixel value:", img.mean())
print("Standard deviation:", img.std())


# 7. Konkret pixel dəyərləri
top_left_pixel = img[0, 0]
center_pixel = img[height // 2, width // 2]
bottom_right_pixel = img[height - 1, width - 1]

print("Top-left pixel BGR:", top_left_pixel)
print("Center pixel BGR:", center_pixel)
print("Bottom-right pixel BGR:", bottom_right_pixel)


# 8. Kanalları ayır
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]

print("Blue channel shape:", blue_channel.shape)
print("Green channel shape:", green_channel.shape)
print("Red channel shape:", red_channel.shape)

print("Blue mean:", blue_channel.mean())
print("Green mean:", green_channel.mean())
print("Red mean:", red_channel.mean())


# 9. Slicing ilə crop et
y1, y2 = height // 4, height // 2
x1, x2 = width // 4, width // 2

crop = img[y1:y2, x1:x2]

print("Crop shape:", crop.shape)


# 10. Crop nəticəsini saxla
cv2.imwrite(f"{output_dir}/crop.jpg", crop)


# 11. Kanalları grayscale kimi saxla
cv2.imwrite(f"{output_dir}/blue_channel.jpg", blue_channel)
cv2.imwrite(f"{output_dir}/green_channel.jpg", green_channel)
cv2.imwrite(f"{output_dir}/red_channel.jpg", red_channel)


# 12. RGB çevirmə — matplotlib üçün
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
crop_rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)


# 13. Original şəkili saxla
plt.figure()
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")
plt.savefig(f"{output_dir}/original_rgb.png")
plt.close()


# 14. Crop şəkili saxla
plt.figure()
plt.imshow(crop_rgb)
plt.title("Cropped Region")
plt.axis("off")
plt.savefig(f"{output_dir}/crop_rgb.png")
plt.close()


# 15. Sadə histogram hesabla
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.plot(hist)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel intensity")
plt.ylabel("Frequency")
plt.savefig(f"{output_dir}/histogram.png")
plt.close()


# 16. Kiçik NumPy yoxlaması
manual_mean = np.sum(gray) / gray.size

print("Gray mean with OpenCV/NumPy:", gray.mean())
print("Gray mean manually:", manual_mean)


print("Day 03 analiz tamamlandı. Nəticələr outputs/day03 qovluğundadır.")