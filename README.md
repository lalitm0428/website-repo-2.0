# Data & Business Analytics Portfolio Website

A professional, responsive portfolio website designed for data analysts and business analytics professionals seeking internship opportunities.

## 🎯 Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional interface with smooth animations
- **Skills Showcase**: Display your Python, Pandas, NumPy, Scikit-learn, and Seaborn expertise
- **Projects Section**: Highlight your data analysis and visualization projects
- **Resume Display**: Embed or link to your resume
- **Contact Information**: Easy ways for recruiters to reach you
- **Dark/Light Friendly**: Professional color scheme optimized for readability

## 📁 Folder Structure

```
Website-Repo/
├── index.html                 # Main website file
├── css/
│   └── style.css             # Styling and responsive design
├── js/
│   └── main.js               # Interactive features
├── content/
│   ├── resume/               # 📌 Add your resume here
│   │   └── (your_resume.pdf or image)
│   └── projects/             # 📌 Add your project folders here
│       └── (project-1-folder, project-2-folder, etc.)
└── README.md                 # This file
```

## 🚀 How to Add Your Content

### 1. **Add Your Resume**
- Navigate to `content/resume/`
- Add your resume in one of these formats:
  - PDF file: `resume.pdf`
  - Image: `resume.png` or `resume.jpg`
  
> The resume will be automatically detected and displayed on the Resume section

### 2. **Add Your Projects**
- Navigate to `content/projects/`
- Create a folder for each project (e.g., `Sales_Dashboard_Analysis`, `Customer_Segmentation`)
- Include:
  - Project files (Python scripts, Jupyter notebooks)
  - `README.md` with project description
  - Sample outputs or visualizations
  - `config.json` (optional) with metadata:
    ```json
    {
        "name": "Project Name",
        "description": "Brief description",
        "tags": ["Python", "Pandas", "Visualization"],
        "icon": "📊"
    }
    ```

### 3. **Update Contact Information**
- Open `index.html`
- Find the Contact section and update:
  - Email address
  - LinkedIn profile URL
  - GitHub profile URL

### 4. **Customize Skills**
- The Skills section is pre-filled with your mentioned skills
- Edit `index.html` to modify skills, add tools like Tableau, Power BI, SQL, etc.

## 🌐 Viewing Your Website

### Option 1: Local Server (Recommended)
```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js (if installed)
npx http-server
```
Then visit: `http://localhost:8000`

### Option 2: Direct File Opening
Simply open `index.html` in your browser (limited functionality)

## 🎨 Customization

### Colors
Edit the CSS variables in `css/style.css`:
```css
:root {
    --primary-color: #2563eb;      /* Main blue */
    --secondary-color: #1e40af;    /* Dark blue */
    --accent-color: #f59e0b;       /* Orange/Gold */
    --text-color: #1f2937;         /* Dark text */
}
```

### Fonts
Change font family in `css/style.css`:
```css
body {
    font-family: 'Your Font Name', sans-serif;
}
```

### Content
- Edit section titles and descriptions in `index.html`
- Modify hero message to highlight your unique value
- Add more sections as needed

## 💡 Pro Tips for Internship Applications

1. **Keep Projects Current**: Update projects with your latest work
2. **Add Descriptions**: Write clear, concise project descriptions highlighting:
   - Business problem solved
   - Tools and techniques used
   - Key insights discovered
   - Impact or results
3. **Professional Resume**: Ensure your resume is:
   - Well-formatted and readable
   - Updated with recent projects
   - Tailored for data/business analytics roles
4. **Add Social Links**: Link to:
   - LinkedIn profile
   - GitHub portfolio
   - Any published articles or blog posts

## 📱 Mobile Responsive

The website is fully responsive with:
- Hamburger menu for mobile navigation
- Optimized layouts for different screen sizes
- Touch-friendly buttons and links

## 🔧 Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with animations
- **Vanilla JavaScript**: No dependencies required
- **Font Awesome**: Icons for visual appeal

## 📞 Support

For questions or customization help, refer to:
- `index.html` for structure
- `css/style.css` for styling
- `js/main.js` for functionality

---

**Ready to impress recruiters? Upload your resume and projects now!** 🚀
