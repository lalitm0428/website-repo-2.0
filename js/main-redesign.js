// Load projects for the redesigned layout
async function loadProjects() {
    const projectsContainer = document.getElementById('projects-container');
    
    // Project data
    const projects = [
        {
            name: "Grand Prix Project",
            description: "Formula 1 telemetry analysis covering data cleaning, exploratory analysis, and visualization across Abu Dhabi, Miami, and Singapore Grand Prix events.",
            tags: ["Python", "Pandas", "Data Analysis", "Visualization"],
            pageUrl: "grand-prix-project.html"
        },
        {
            name: "Amazon Regression Project",
            description: "A machine learning project to predict product sales using regression models.",
            tags: ["Python", "Scikit-learn", "Streamlit", "Machine Learning"],
            pageUrl: "amazon-regression-project.html"
        },
        {
            name: "Netflix Project",
            description: "An in-depth analysis of the Netflix content library to identify trends and predict content success.",
            tags: ["Python", "Pandas", "Scikit-learn", "EDA"],
            pageUrl: "netflix-project.html"
        },
        {
            name: "Spotify Project",
            description: "A project to segment Spotify's top tracks into distinct clusters based on audio features.",
            tags: ["Python", "Scikit-learn", "Clustering", "Plotly"],
            pageUrl: "spotify-project.html"
        }
    ];

    projectsContainer.innerHTML = '';

    projects.forEach(project => {
        const projectCard = document.createElement('div');
        projectCard.className = 'project-card-new';
        projectCard.innerHTML = `
            <a href="${project.pageUrl}">
                <h3>${project.name}</h3>
                <p>${project.description}</p>
                <div class="project-tags-new">
                    ${project.tags.map(tag => `<span class="tag-new">${tag}</span>`).join('')}
                </div>
                <div style="color: var(--text-secondary); font-size: 0.875rem; font-weight: 600;">View Project →</div>
            </a>
        `;
        projectsContainer.appendChild(projectCard);
    });
}

// Mobile Menu Toggle (if needed in future)
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navMenu?.classList.toggle('active');
    });
}

// Close mobile menu when a link is clicked
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu?.classList.remove('active');
    });
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    loadProjects();
});

// Optional: Add parallax effect to watermark on scroll
window.addEventListener('scroll', () => {
    const watermark = document.querySelector('.page-watermark');
    if (watermark) {
        const scrollPos = window.scrollY * 0.5;
        watermark.style.transform = `translateY(calc(-50% + ${scrollPos}px)) rotate(-90deg)`;
    }
});
