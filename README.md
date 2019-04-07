# Per-evaluation test for web developer


Upload an image crop and download

Create a client web page with the following fields:

File select (Image: any image)

Submit button

Create a python app (Django/Flask)

On submit receive an image 

Crop an image by 3x3, as a result we expect 9 pieces of the image with same size.

Return zip archive that contains all pieces of the image.

## Running Locally

```bash
git clone https://github.com/perryyo/up.git
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```