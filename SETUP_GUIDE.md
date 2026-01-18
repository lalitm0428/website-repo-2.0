# Portfolio Quick Start Guide

Welcome to your professional Data & Business Analytics Portfolio! This guide will help you get everything set up and running.

## 📁 Directory Structure

```
Website-Repo/
├── index.html                           # Main portfolio page
├── grand-prix-project.html              # Dedicated project page
├── css/
│   ├── style.css                        # Main styles
│   └── project.css                      # Project page styles
├── js/
│   └── main.js                          # JavaScript functionality
├── content/
│   ├── resume/
│   │   └── Lalit_Mohan_Resume-1.pdf    # Your resume
│   └── projects/
│       └── Grand Prix Project/          # Your project files
├── README.md                            # Main documentation
└── SETUP_GUIDE.md                       # This file
```

## 🚀 Getting Started

### 1. **View Your Portfolio**

The web server should already be running on `http://localhost:8000`

If not, start it with:
```bash
cd "/Users/apple/Documents/Uni/Personal /Website-Repo"
python3 -m http.server 8000
```

Then visit: **http://localhost:8000**

### 2. **Update Contact Information**

Edit `index.html` and replace:
- `your.email@example.com` with your actual email
- `https://linkedin.com` with your LinkedIn profile URL
- `https://github.com` with your GitHub profile URL

Search for the Contact section (around line 130) to make these changes.

### 3. **Customize Your About Section**

In `index.html`, update the About section (around line 50) to personalize it with:
- Your specific background
- Your career goals
- Any relevant internship preferences

## 🎯 Project Page Features

### Viewing Your Grand Prix Project

1. Navigate to the Projects section on the main page
2. Click **"View Full Project"** button
3. This opens `grand-prix-project.html` which includes:
   - Executive summary with key findings
   - Data cleaning code and explanation
   - Analysis methodology
   - Insights and recommendations
   - File structure and technologies
   - Download links for all project files

### Running the Interactive Dashboard

To see your interactive Streamlit dashboard in action:

```bash
cd content/projects/"Grand Prix Project"
pip install -r requirements.txt
streamlit run dashboard.py
```

Then visit: **http://localhost:8501**

**Dashboard Features:**
- Filter by Grand Prix event (Abu Dhabi, Miami, Singapore)
- Select tire compounds to analyze
- View pace evolution charts
- Analyze tire degradation curves
- Examine sector-by-sector performance

## 📝 Files You Can Download from the Website

All these files are available for download from the project page:

1. **1_Data_Cleaning.ipynb** - Jupyter notebook showing data processing
2. **2_analysis.ipynb** - Jupyter notebook with exploratory analysis
3. **dashboard.py** - Streamlit dashboard code
4. **f1_clean_data.csv** - Cleaned dataset

## 🎨 Customization Tips

### Change Colors

Edit `css/style.css` and modify the CSS variables at the top:

```css
:root {
    --primary-color: #2563eb;      /* Change this blue */
    --secondary-color: #1e40af;    /* Darker blue variant */
    --accent-color: #f59e0b;       /* Change this orange */
    --text-color: #1f2937;         /* Text color */
}
```

### Add More Projects

To add another project:

1. Create a new folder in `content/projects/`
2. Update the `projects` array in `js/main.js`:

```javascript
const projects = [
    {
        name: "Your Project Name",
        description: "Description here",
        tags: ["Python", "Pandas"],
        image: "📊",
        files: ["file1.ipynb", "file2.py"],
        pageUrl: "your-project.html"
    }
    // Add your new project here
];
```

3. Create a project page similar to `grand-prix-project.html`

### Add More Skills

Edit the Skills section in `index.html` to add or modify skills.

## 🔧 Technical Details

### Technologies

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with animations
- **JavaScript**: Vanilla JS (no frameworks needed)
- **Font Awesome**: Icons
- **Highlight.js**: Code syntax highlighting

### Browser Support

The portfolio works on:
- Chrome/Chromium (Latest)
- Firefox (Latest)
- Safari (Latest)
- Edge (Latest)

## 💼 For Internship Applications

### What to Highlight

1. **Your Resume**: 
   - Clearly visible in the Resume section
   - Downloadable as PDF
   - Embedded viewer for quick preview

2. **Your Project**:
   - Comprehensive overview with business context
   - Code samples showing your technical skills
   - Key insights demonstrating analytical thinking
   - Interactive dashboard showing visualization skills
   - All files available for download

3. **Your Skills**:
   - Python, Pandas, NumPy expertise
   - Data visualization with Seaborn & Plotly
   - Statistical analysis capabilities
   - Business analytics mindset

### Making the Most of It

1. **Keep it Updated**: Add new projects as you complete them
2. **Share the Link**: Include your portfolio URL in applications
3. **Reference the Project**: Talk about the Grand Prix project in interviews
4. **Show the Dashboard**: Demonstrate the interactive dashboard in interviews
5. **Explain the Process**: Be ready to discuss your data cleaning and analysis methodology

## 🐛 Troubleshooting

### Portfolio Page Won't Load

1. Check if server is running:
   ```bash
   python3 -m http.server 8000
   ```
2. Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
3. Try different port: `python3 -m http.server 8001`

### Dashboard Won't Run

1. Ensure Python packages are installed:
   ```bash
   pip install streamlit pandas plotly
   ```
2. Ensure you're in the correct directory:
   ```bash
   cd content/projects/"Grand Prix Project"
   ```
3. Check that `f1_clean_data.csv` exists in the directory

### Files Won't Download

1. Check file paths are correct
2. Ensure files exist in the expected locations
3. Use browser's Developer Tools (F12) to check console errors

## 📱 Mobile Optimization

Your portfolio is fully responsive:
- Hamburger menu on mobile devices
- Touch-friendly buttons
- Optimized images and text
- Works on all screen sizes

Test on mobile by:
1. Using browser DevTools (F12) → Toggle Device Toolbar
2. Or accessing from an actual mobile device using your computer's IP address

## 🔐 Privacy & Security

- All data is processed locally (no external analytics)
- Your email link uses standard mailto: (not exposed to bots)
- No tracking cookies or external scripts
- All files can be downloaded and hosted anywhere

## 📞 Support & Next Steps

1. **Deploy Your Portfolio**:
   - GitHub Pages (free, recommended)
   - Netlify (free with continuous deployment)
   - Vercel (free with custom domain)
   - Any web hosting service

2. **Share Your Portfolio**:
   - LinkedIn profile: Add link to portfolio
   - Cover letters: Include portfolio URL
   - Networking: Share with recruiters and mentors
   - GitHub: Link from your repositories

3. **Continuous Improvement**:
   - Add more projects as you complete them
   - Update your resume with new accomplishments
   - Refresh skills section with new technologies
   - Gather feedback from mentors and peers

---

**Good luck with your internship applications!** 🚀

Your portfolio is a powerful tool to showcase your data analytics skills. Keep it updated and be proud of what you've built!
