# Day 05 — Display, Save, Resize and Crop Images with OpenCV

## Objective

In this lesson, I learned how to read, display, save, resize, and crop images using OpenCV.

These operations are fundamental parts of a Computer Vision preprocessing pipeline. Before sending an image to a model or an image processing algorithm, we often need to resize it, crop unnecessary regions, or prepare it in a suitable format.

## What I Learned

- How to read an image using `cv2.imread()`
- How to save an image using `cv2.imwrite()`
- How to resize an image using `cv2.resize()`
- How to crop an image using NumPy slicing
- How to understand `image.shape`
- The difference between BGR and RGB color formats
- Why OpenCV and Matplotlib display images differently

## Key Concepts

OpenCV reads images in BGR format by default:

```text
BGR = Blue, Green, Red
```

Matplotlib expects images in RGB format:

```text
RGB = Red, Green, Blue
```

Therefore, when displaying an OpenCV image with Matplotlib, the image should be converted from BGR to RGB:

```python
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
```

## Resize Logic

In OpenCV, resizing is done like this:

```python
resized_image = cv2.resize(image_bgr, (400, 300))
```

Here:

```text
400 = width
300 = height
```

However, `image.shape` returns values in this order:

```text
(height, width, channels)
```

This difference is important because OpenCV resize uses `(width, height)`, while NumPy shape returns `(height, width, channels)`.

## Crop Logic

Cropping is done using NumPy slicing:

```python
cropped_image = image_bgr[y1:y2, x1:x2]
```

Example:

```python
cropped_image = image_bgr[100:400, 200:600]
```

This means:

```text
y-axis: from 100 to 400
x-axis: from 200 to 600
```

So, in image slicing, the row range comes first, and the column range comes second.

## Output Files

After running the script, the following files are saved inside the `outputs/` folder:

```text
original_saved.jpg
resized_image.jpg
cropped_image.jpg
```

## How to Run

Install the required dependencies from the main project folder:

```bash
pip install -r requirements.txt
```

Go to the Day 05 folder:

```bash
cd day-05-resize-crop-image
```

Run the script:

```bash
python resize_crop.py
```

## Common Mistakes

1. Confusing width and height in `cv2.resize()`.
2. Confusing x and y coordinates while cropping.
3. Displaying a BGR image directly with Matplotlib without converting it to RGB.
4. Not checking whether the image was loaded successfully.
5. Using crop coordinates that are outside the actual image size.

## Result

In this lesson, I practiced basic image resizing and cropping operations. Resizing is useful for preparing images for models, while cropping helps focus on the important region of an image and remove unnecessary background.
