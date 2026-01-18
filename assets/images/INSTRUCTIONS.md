# Adding Your Profile Picture

## Where to Place Your Picture

Your profile picture should be placed in:
```
/Users/apple/Documents/Uni/Personal /Website-Repo/assets/images/
```

## File Requirements

**Filename**: `profile.jpg` or `profile.png`
- The website looks for `profile.jpg` by default
- If using PNG, you can change the filename in `index.html`

**Image Specifications**:
- **Recommended size**: 300x300 pixels (square recommended)
- **Format**: JPG or PNG
- **File size**: Keep under 1MB for fast loading
- **Quality**: High quality, clear headshot or professional photo

## How to Add Your Picture

1. **Prepare your image**
   - Take or select a professional headshot photo
   - Crop it to be square (300x300px recommended)
   - Save it as `profile.jpg` or `profile.png`

2. **Place the file**
   - Copy or drag your image to: `/Users/apple/Documents/Uni/Personal /Website-Repo/assets/images/`
   - Name it exactly as: `profile.jpg` (or `profile.png`)

3. **Verify it displays**
   - Open your portfolio at http://localhost:8000
   - Scroll to the "About Me" section
   - Your picture should now appear on the left side

## If You Use a Different Filename

If your image filename is different (e.g., `photo.jpg`, `portrait.png`), edit `index.html`:

1. Open `index.html`
2. Find this line (around line 50):
   ```html
   <img id="profile-pic" src="assets/images/profile.jpg" alt="Profile Picture" class="profile-image">
   ```
3. Replace `profile.jpg` with your filename, e.g., `photo.jpg`
4. Save the file
5. Refresh your browser

## Image Format Recommendations

**For best results:**
- Use a recent, clear photo
- Professional headshot or business casual photo
- Good lighting, clear face visible
- Neutral or blurred background
- Square crop (300x300 or larger square dimensions)

**Professional Tips:**
- Wear business casual or formal attire
- Use good lighting (natural light preferred)
- Center your face in the frame
- Smile naturally
- Avoid distracting backgrounds
- Professional haircut and grooming

## Troubleshooting

**Image not showing up?**
1. Check filename is exactly `profile.jpg` or update `index.html`
2. Verify file is in `/assets/images/` directory
3. Clear browser cache (Ctrl+Shift+Delete)
4. Refresh the page

**Image looks stretched or distorted?**
1. Ensure your image is square or close to square
2. The CSS will automatically crop it to fit
3. Recommended: Use a 300x300px square image

**Image file too large?**
1. Compress the image before uploading
2. Use online tools like TinyPNG or ImageOptim
3. Aim for files under 500KB for faster loading

## File Organization

```
Website-Repo/
├── assets/
│   └── images/
│       ├── profile.jpg          ← Your profile picture goes here
│       └── README.md            ← This file
```

---

**Quick Start**: 
1. Add your professional headshot as `profile.jpg` 
2. Place it in `assets/images/` folder
3. Refresh your portfolio page at http://localhost:8000
4. Your picture will appear in the "About Me" section!
