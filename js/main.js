// Mobile Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });
}

// Close mobile menu when a link is clicked
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
    });
});

// Load projects from content/projects folder
async function loadProjects() {
    const projectsContainer = document.getElementById('projects-container');
    
    // Project data
    const projects = [
        {
            name: "Grand Prix Project",
            description: "Comprehensive Formula 1 data analysis project covering data cleaning, exploratory analysis, and visualization of Grand Prix race data. Includes analysis of multiple Grand Prix events (Abu Dhabi, Miami, Singapore) with Python-based data processing pipeline.",
            tags: ["Python", "Pandas", "Data Analysis", "Visualization", "Jupyter Notebooks"],
            image: "F1",
            path: "content/projects/Grand Prix Project",
            files: ["1_Data_Cleaning.ipynb", "2_analysis.ipynb", "dashboard.py", "f1_clean_data.csv"],
            pageUrl: "grand-prix-project.html"
        }
    ];

    projectsContainer.innerHTML = '';

    projects.forEach(project => {
        const projectCard = document.createElement('div');
        projectCard.className = 'project-card';
        projectCard.innerHTML = `
            <a href="${project.pageUrl}" class="project-card-link">
                <div class="project-image">${project.image}</div>
                <div class="project-content">
                    <h3>${project.name}</h3>
                    <p>${project.description}</p>
                    <div class="project-tags">
                        ${project.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                    </div>
                    <div class="project-files">
                        <h4>Project Files:</h4>
                        <ul>
                            ${project.files.map(file => `<li>📄 ${file}</li>`).join('')}
                        </ul>
                    </div>
                    <div class="view-project-btn">
                        View Full Project <i class="fas fa-arrow-right"></i>
                    </div>
                </div>
            </a>
        `;
        projectsContainer.appendChild(projectCard);
    });
}

// Load resume
async function loadResume() {
    const resumeContainer = document.getElementById('resume-container');
    const resumeLink = document.getElementById('resume-link');
    
    // Resume file path
    const resumePath = 'content/resume/Lalit_Mohan_Resume-1.pdf';
    
    // Create a PDF viewer iframe
    resumeContainer.innerHTML = `
        <div class="pdf-viewer">
            <iframe src="${resumePath}#toolbar=0" width="100%" height="800px" style="border: none; border-radius: 8px;"></iframe>
        </div>
        <p class="pdf-note">📄 PDF Viewer - Scroll to see full resume</p>
    `;
    
    // Update download link
    resumeLink.href = resumePath;
    resumeLink.style.display = 'inline-block';
}

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
    loadResume();
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.skill-card, .project-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});
