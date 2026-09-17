import json

with open('projects_data.json', 'r', encoding='utf-8') as f:
    projects = json.load(f)

projects_json_str = json.dumps(projects, ensure_ascii=False)

# 1. GENERATE index.html
index_html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ankit Kumar | AI & Data Science Engineer | IIT Kanpur</title>
  <meta name="description" content="Portfolio of Ankit Kumar — M.Tech DoMS, IIT Kanpur. AI, Machine Learning, Deep Learning, GenAI & Autonomous Agents, Time Series Forecasting, and Business Analytics Engineer.">
  <meta name="keywords" content="Ankit Kumar, IIT Kanpur, Machine Learning, Generative AI, LangChain, LangGraph, PyTorch, Data Science, Portfolio">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Stylesheet -->
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- Ambient Glow Elements -->
  <div class="glow-orb orb-1"></div>
  <div class="glow-orb orb-2"></div>
  <div class="glow-orb orb-3"></div>

  <!-- Navigation Bar -->
  <header class="navbar-wrapper">
    <nav class="navbar container">
      <a href="#hero" class="nav-logo">
        <span class="logo-badge">AK</span>
        <span class="logo-text">Ankit Kumar</span>
      </a>

      <div class="nav-links" id="navLinks">
        <a href="#about" class="nav-link">About</a>
        <a href="#experience" class="nav-link">Experience</a>
        <a href="#skills" class="nav-link">Skills</a>
        <a href="#projects" class="nav-link">Projects <span class="nav-count">45</span></a>
        <a href="#achievements" class="nav-link">Achievements</a>
        <a href="#contact" class="nav-link">Contact</a>
      </div>

      <div class="nav-actions">
        <span class="status-indicator" title="Open for Full-time Roles & Projects">
          <span class="status-dot"></span> Available
        </span>
        <a href="main.pdf" target="_blank" class="btn btn-outline btn-sm">Resume (PDF) ↗</a>
        <button class="theme-toggle" id="themeToggleBtn" onclick="toggleTheme()" aria-label="Toggle Dark/Light Mode">
          <span id="themeIcon">🌙</span>
        </button>
      </div>
    </nav>
  </header>

  <!-- Main Content Container -->
  <main>
    <!-- HERO SECTION -->
    <section class="hero-section container" id="hero">
      <div class="hero-content">
        <div class="hero-badge">
          <span class="badge-icon">🎓</span>
          <span>M.Tech, Department of Management Sciences (DoMS) &bull; IIT Kanpur</span>
        </div>

        <h1 class="hero-title">
          Engineering Scalable <span class="gradient-text">AI Systems</span>, Autonomous Agents & <span class="gradient-text-alt">Predictive Intelligence</span>.
        </h1>

        <p class="hero-subtitle">
          Data Science & Machine Learning Engineer with deep expertise in <strong>Generative AI & Multi-Agent RAG</strong>, <strong>Computer Vision</strong>, <strong>Time Series Forecasting</strong>, and <strong>Enterprise Decision Intelligence</strong>. Proven track record with a <strong>TCS AI Internship</strong>, <strong>GATE 98.48 percentile</strong>, and <strong>45+ end-to-end production & academic projects</strong>.
        </p>

        <!-- Quick Credentials Ticker -->
        <div class="hero-credentials">
          <div class="cred-chip"><span class="cred-icon">🏛️</span> <strong>IIT Kanpur</strong> (M.Tech)</div>
          <div class="cred-chip"><span class="cred-icon">🥇</span> <strong>GATE 98.48 %ile</strong></div>
          <div class="cred-chip"><span class="cred-icon">🥈</span> <strong>Chancellor's Silver Medal</strong></div>
          <div class="cred-chip"><span class="cred-icon">💼</span> <strong>TCS AI Intern</strong> (CV & ML)</div>
          <div class="cred-chip"><span class="cred-icon">🗼</span> <strong>Univ of Tokyo GCI</strong></div>
          <div class="cred-chip"><span class="cred-icon">📜</span> <strong>Oracle Certified DS</strong></div>
        </div>

        <!-- Hero Call to Action Buttons -->
        <div class="hero-cta-row">
          <a href="#projects" class="btn btn-primary btn-lg">
            Explore 45 Projects &darr;
          </a>
          <a href="main.pdf" target="_blank" class="btn btn-secondary btn-lg">
            View Harvard Resume (PDF) ↗
          </a>
          <div class="hero-social-links">
            <a href="https://github.com/Ankitiitk369" target="_blank" class="social-icon-btn" title="GitHub Profile">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.1-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z"/></svg>
            </a>
            <a href="https://linkedin.com/in/ankit-kumar" target="_blank" class="social-icon-btn" title="LinkedIn Profile">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 8.76a1.45 1.45 0 1 0 0-2.9 1.45 1.45 0 0 0 0 2.9m1.4 9.74V9.93H5.06v8.57h2.8z"/></svg>
            </a>
            <a href="https://sites.google.com/view/ankit369portfolio/home" target="_blank" class="social-icon-btn" title="Google Sites Portfolio">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- LIVE STATS IMPACT SECTION -->
    <section class="stats-overview-section container">
      <div class="stats-overview-grid">
        <div class="overview-stat-box">
          <span class="overview-stat-number" data-target="45">45</span>
          <span class="overview-stat-label">Unique AI/ML Projects</span>
          <span class="overview-stat-sub">Zero repeated repositories</span>
        </div>
        <div class="overview-stat-box">
          <span class="overview-stat-number" data-target="98.48">98.48%</span>
          <span class="overview-stat-label">GATE 2025 Percentile</span>
          <span class="overview-stat-sub">National Top 1.5% rank</span>
        </div>
        <div class="overview-stat-box">
          <span class="overview-stat-number">0.996</span>
          <span class="overview-stat-label">TCS Model R² Metric</span>
          <span class="overview-stat-sub">RMSE: 3.12 g/km &bull; 17 Tests</span>
        </div>
        <div class="overview-stat-box">
          <span class="overview-stat-number">96.8%</span>
          <span class="overview-stat-label">RAG Faithfulness Score</span>
          <span class="overview-stat-sub">Zero clinical hallucinations</span>
        </div>
      </div>
    </section>

    <!-- ABOUT & TRAJECTORY SECTION -->
    <section class="section container" id="about">
      <div class="section-header">
        <span class="section-tag">About Me</span>
        <h2 class="section-title">Bridging Advanced Algorithms with Real-World Engineering</h2>
        <p class="section-desc">From agricultural engineering optimization to advanced management sciences and generative AI systems at IIT Kanpur.</p>
      </div>

      <div class="about-grid">
        <div class="about-card narrative-card">
          <h3>My Engineering Philosophy</h3>
          <p>
            I am currently pursuing my <strong>M.Tech in the Department of Management Sciences (DoMS) at the Indian Institute of Technology Kanpur (CPI: 7.18 / 10.0)</strong>, graduating in 2027. Previously, I earned my <strong>B.Tech in Agricultural Engineering (CPI: 8.25 / 10.0)</strong>, where I was honored with the prestigious <strong>Chancellor's Silver Medal</strong> for academic excellence.
          </p>
          <p>
            My interdisciplinary journey combines rigorous quantitative optimization with high-performance software engineering. Whether designing <strong>autonomous agentic workflows with LangGraph and ReAct</strong>, fine-tuning deep convolutional networks for defect detection, or forecasting daily fuel prices with PyTorch LSTMs, I build systems that are <strong>verifiably accurate, latency-optimized, and production-ready</strong>.
          </p>
          <div class="about-highlights-row">
            <div class="about-mini-tag">&bull; IIT Kanpur Postgraduate</div>
            <div class="about-mini-tag">&bull; Systems & LLMOps Focus</div>
            <div class="about-mini-tag">&bull; Quantitative Analytics</div>
          </div>
        </div>

        <div class="about-card education-card">
          <h3>Academic Foundations</h3>
          <div class="edu-item">
            <div class="edu-top">
              <span class="edu-degree">M.Tech in Management Sciences (DoMS)</span>
              <span class="edu-year">2025 &ndash; Present</span>
            </div>
            <span class="edu-school">Indian Institute of Technology, Kanpur</span>
            <p class="edu-cpi">CPI: <strong>7.18 / 10.0</strong> &bull; Focus: Applied Machine Learning, SMBA, Data Mining, Operations Research</p>
          </div>

          <div class="edu-item">
            <div class="edu-top">
              <span class="edu-degree">B.Tech in Agricultural Engineering</span>
              <span class="edu-year">2021 &ndash; 2025</span>
            </div>
            <span class="edu-school">C.S.A. University of Agriculture and Technology</span>
            <p class="edu-cpi">CPI: <strong>8.25 / 10.0</strong> &bull; <strong class="highlight-text">Awarded Chancellor's Silver Medal</strong> (Rank 1st)</p>
          </div>

          <div class="edu-item">
            <div class="edu-top">
              <span class="edu-degree">UP State Board (Class XII & X)</span>
              <span class="edu-year">2018 &ndash; 2021</span>
            </div>
            <span class="edu-school">Government Inter College, Kadaura, Jalaun</span>
            <p class="edu-cpi">Class XII: 77.20% &bull; Class X: 80.83%</p>
          </div>
        </div>
      </div>
    </section>

    <!-- WORK EXPERIENCE SECTION -->
    <section class="section container" id="experience">
      <div class="section-header">
        <span class="section-tag">Career History</span>
        <h2 class="section-title">Professional & Engineering Experience</h2>
        <p class="section-desc">Hands-on production machine learning, computer vision, and enterprise software engineering.</p>
      </div>

      <div class="timeline">
        <!-- TCS Experience Card -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <div>
                <span class="timeline-company">Tata Consultancy Services (TCS)</span>
                <h3 class="timeline-role">Data Science & AI Intern &bull; Computer Vision & Machine Learning</h3>
              </div>
              <span class="timeline-date">May 2026 &ndash; July 2026 &bull; Remote / India</span>
            </div>
            <ul class="timeline-bullets">
              <li>Engineered an automated end-to-end vehicle CO₂ emission tracking pipeline from real-time CCTV feeds to monitor urban carbon footprints for enterprise ESG reporting.</li>
              <li>Integrated <strong>YOLOv8</strong> object localization paired with <strong>OpenCV</strong> image preprocessing (Bilateral Filtering, CLAHE, Otsu thresholding) and <strong>EasyOCR</strong> with custom regex syntax correction.</li>
              <li>Trained dual-stage ensemble estimators: <strong>Gradient Boosting</strong> (R² = 0.996, RMSE = 3.12 g/km) and <strong>Random Forest</strong> (R² = 0.989) for trip emission modeling.</li>
              <li>Delivered an interactive <strong>Streamlit</strong> monitoring dashboard paired with an automated <strong>17-test Pytest</strong> CI/CD test suite.</li>
            </ul>
            <div class="timeline-tech-row">
              <span class="tech-pill">YOLOv8</span>
              <span class="tech-pill">OpenCV</span>
              <span class="tech-pill">EasyOCR</span>
              <span class="tech-pill">Gradient Boosting</span>
              <span class="tech-pill">Streamlit</span>
              <span class="tech-pill">Pytest CI/CD</span>
            </div>
          </div>
        </div>

        <!-- Global Procurement Experience Card -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <div>
                <span class="timeline-company">Global Procurement Enterprise Web Application</span>
                <h3 class="timeline-role">Frontend & Asset Automation Contributor</h3>
              </div>
              <span class="timeline-date">Feb 2026 &ndash; Apr 2026</span>
            </div>
            <ul class="timeline-bullets">
              <li>Contributed to the Asset Receiving Automation Module for an enterprise Global Procurement System, digitizing manual tracking across 100+ inventory categories.</li>
              <li>Engineered responsive <strong>Angular</strong> interfaces for capturing asset metadata, PO numbers, quantities, and storage locations with real-time client-side validation schemas.</li>
              <li>Implemented secure <strong>Role-Based Access Control (RBAC)</strong>, session authentication, and dynamic validation schemas, cutting manual asset ingestion latency by <strong>40%</strong>.</li>
            </ul>
            <div class="timeline-tech-row">
              <span class="tech-pill">Angular 16</span>
              <span class="tech-pill">TypeScript</span>
              <span class="tech-pill">REST APIs</span>
              <span class="tech-pill">RBAC</span>
              <span class="tech-pill">Form Validation</span>
            </div>
          </div>
        </div>

        <!-- Leadership Experience Card -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <div>
                <span class="timeline-company">Positions of Responsibility & Leadership</span>
                <h3 class="timeline-role">IIT Kanpur & Institutional Initiatives</h3>
              </div>
              <span class="timeline-date">2021 &ndash; Present</span>
            </div>
            <ul class="timeline-bullets">
              <li><strong>Alumni & Corporate Relations Coordinator, IIT Kanpur</strong> (July 2025 &ndash; Present): Driving corporate engagement, guest lectures, and alumni collaborations; organized 10+ departmental technical webinars.</li>
              <li><strong>Campus Coordinator, Mimamsa 2025</strong> (IISER Pune): Directed institutional outreach across northern Indian universities; managed regional logistics.</li>
              <li><strong>NSS Student Volunteer (2 Years)</strong>: Spearheaded advocacy campaigns for girls' education and digital literacy under <em>"Ek Bharat Shreshtha Bharat"</em>.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- TECHNICAL SKILLS SECTION -->
    <section class="section container" id="skills">
      <div class="section-header">
        <span class="section-tag">Technical Arsenal</span>
        <h2 class="section-title">Core Skills, Frameworks & Tooling</h2>
        <p class="section-desc">Comprehensive technology stack used to build production AI and data-driven systems.</p>
      </div>

      <div class="skills-grid">
        <!-- Skills Category 1 -->
        <div class="skills-card">
          <div class="skills-card-icon" style="background: rgba(139, 92, 246, 0.15); color: #c4b5fd;">🧠</div>
          <h3 class="skills-card-title">Generative AI & LLMOps</h3>
          <p class="skills-card-desc">Production RAG pipelines, agentic orchestration, and safety guardrails.</p>
          <div class="skills-tags">
            <span class="skill-tag">LangChain</span>
            <span class="skill-tag">LangGraph</span>
            <span class="skill-tag">LlamaIndex</span>
            <span class="skill-tag">CrewAI</span>
            <span class="skill-tag">Pinecone</span>
            <span class="skill-tag">FAISS</span>
            <span class="skill-tag">Groq API</span>
            <span class="skill-tag">Gemini 2.5</span>
            <span class="skill-tag">RAGAS</span>
            <span class="skill-tag">Multimodal RAG</span>
            <span class="skill-tag">ReAct Agents</span>
            <span class="skill-tag">Prompt Engineering</span>
          </div>
        </div>

        <!-- Skills Category 2 -->
        <div class="skills-card">
          <div class="skills-card-icon" style="background: rgba(6, 182, 212, 0.15); color: #67e8f9;">📈</div>
          <h3 class="skills-card-title">Machine Learning & Stats</h3>
          <p class="skills-card-desc">Supervised classification, regression, clustering, and hypothesis testing.</p>
          <div class="skills-tags">
            <span class="skill-tag">Scikit-learn</span>
            <span class="skill-tag">XGBoost</span>
            <span class="skill-tag">LightGBM</span>
            <span class="skill-tag">CatBoost</span>
            <span class="skill-tag">Optuna</span>
            <span class="skill-tag">SMOTE</span>
            <span class="skill-tag">A/B Testing</span>
            <span class="skill-tag">Two-Way ANOVA</span>
            <span class="skill-tag">Chi-Square</span>
            <span class="skill-tag">VIF Multicollinearity</span>
            <span class="skill-tag">SHAP (XAI)</span>
            <span class="skill-tag">Feature Engineering</span>
          </div>
        </div>

        <!-- Skills Category 3 -->
        <div class="skills-card">
          <div class="skills-card-icon" style="background: rgba(244, 63, 94, 0.15); color: #fda4af;">⏱️</div>
          <h3 class="skills-card-title">Time Series & Deep Learning</h3>
          <p class="skills-card-desc">Temporal modeling, commodity forecasting, and neural architectures.</p>
          <div class="skills-tags">
            <span class="skill-tag">PyTorch</span>
            <span class="skill-tag">TensorFlow</span>
            <span class="skill-tag">Keras</span>
            <span class="skill-tag">Stacked LSTM</span>
            <span class="skill-tag">ARIMA / SARIMAX</span>
            <span class="skill-tag">Meta Prophet</span>
            <span class="skill-tag">Statsmodels</span>
            <span class="skill-tag">CNNs</span>
            <span class="skill-tag">MobileNetV2</span>
            <span class="skill-tag">EfficientNetB0</span>
            <span class="skill-tag">Transfer Learning</span>
          </div>
        </div>

        <!-- Skills Category 4 -->
        <div class="skills-card">
          <div class="skills-card-icon" style="background: rgba(245, 158, 11, 0.15); color: #fcd34d;">👁️</div>
          <h3 class="skills-card-title">Vision & Document AI</h3>
          <p class="skills-card-desc">Real-time object localization, OCR extraction, and speech processing.</p>
          <div class="skills-tags">
            <span class="skill-tag">OpenCV</span>
            <span class="skill-tag">YOLOv8</span>
            <span class="skill-tag">EasyOCR</span>
            <span class="skill-tag">Tesseract OCR</span>
            <span class="skill-tag">Image Preprocessing</span>
            <span class="skill-tag">Spatial Localization</span>
            <span class="skill-tag">SpeechRecognition</span>
            <span class="skill-tag">GloVe 100d</span>
          </div>
        </div>

        <!-- Skills Category 5 -->
        <div class="skills-card">
          <div class="skills-card-icon" style="background: rgba(16, 185, 129, 0.15); color: #6ee7b7;">📊</div>
          <h3 class="skills-card-title">SQL, BI & Analytics</h3>
          <p class="skills-card-desc">Relational querying, data modeling, and interactive dashboards.</p>
          <div class="skills-tags">
            <span class="skill-tag">PostgreSQL</span>
            <span class="skill-tag">MySQL</span>
            <span class="skill-tag">Advanced SQL (CTEs, Window)</span>
            <span class="skill-tag">Power BI (Advanced DAX)</span>
            <span class="skill-tag">Tableau</span>
            <span class="skill-tag">Pandas</span>
            <span class="skill-tag">NumPy</span>
            <span class="skill-tag">Plotly</span>
            <span class="skill-tag">Seaborn</span>
            <span class="skill-tag">Advanced Excel</span>
          </div>
        </div>

        <!-- Skills Category 6 -->
        <div class="skills-card">
          <div class="skills-card-icon" style="background: rgba(236, 72, 153, 0.15); color: #f472b6;">⚡</div>
          <h3 class="skills-card-title">Software & Production Tooling</h3>
          <p class="skills-card-desc">Backend deployment, testing frameworks, and version control.</p>
          <div class="skills-tags">
            <span class="skill-tag">Python (Advanced)</span>
            <span class="skill-tag">FastAPI</span>
            <span class="skill-tag">Streamlit</span>
            <span class="skill-tag">Docker</span>
            <span class="skill-tag">Git & GitHub</span>
            <span class="skill-tag">Linux</span>
            <span class="skill-tag">Pytest</span>
            <span class="skill-tag">Angular</span>
            <span class="skill-tag">TypeScript</span>
            <span class="skill-tag">LaTeX</span>
          </div>
        </div>
      </div>
    </section>

    <!-- COMPLETE PROJECTS SHOWCASE GALLERY (ALL 45 PROJECTS) -->
    <section class="section container" id="projects">
      <div class="section-header">
        <span class="section-tag">Project Showcase</span>
        <h2 class="section-title">Explore All 45 Production & Academic Systems</h2>
        <p class="section-desc">Every single unique project from GitHub and master resume with live repositories, benchmarks, and architectural details.</p>
      </div>

      <!-- Controls & Filter Toolbar -->
      <div class="projects-control-bar">
        <!-- Top Search and Sort -->
        <div class="search-sort-row">
          <div class="search-field-container">
            <svg class="search-svg-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            <input type="text" id="projectSearchInput" placeholder="Filter by technology, keyword, model (e.g., PyTorch, LangChain, XGBoost, SQL, YOLO)..." oninput="applyFilters()">
            <button class="clear-search" id="clearSearchBtn" onclick="resetSearch()">✕</button>
          </div>
          <div class="sort-field-container">
            <select id="sortDropdown" onchange="applyFilters()">
              <option value="featured">Sort: Flagship / Recommended</option>
              <option value="alpha">Sort: Alphabetical (A-Z)</option>
              <option value="domain">Sort: By Domain</option>
            </select>
          </div>
        </div>

        <!-- Domain Filter Tabs -->
        <div class="filter-tabs-row" id="filterTabs">
          <button class="domain-tab active" data-category="all" onclick="setCategoryFilter('all')">All Projects <span class="tab-badge">45</span></button>
          <button class="domain-tab" data-category="genai" onclick="setCategoryFilter('genai')">GenAI & Agents <span class="tab-badge">11</span></button>
          <button class="domain-tab" data-category="ml" onclick="setCategoryFilter('ml')">Machine Learning <span class="tab-badge">10</span></button>
          <button class="domain-tab" data-category="timeseries" onclick="setCategoryFilter('timeseries')">Time Series <span class="tab-badge">6</span></button>
          <button class="domain-tab" data-category="cv" onclick="setCategoryFilter('cv')">Vision & NLP <span class="tab-badge">6</span></button>
          <button class="domain-tab" data-category="bi" onclick="setCategoryFilter('bi')">SQL & BI Analytics <span class="tab-badge">10</span></button>
          <button class="domain-tab" data-category="exp" onclick="setCategoryFilter('exp')">Enterprise <span class="tab-badge">2</span></button>
        </div>

        <!-- Quick Tech Filter Chips -->
        <div class="tech-chips-row">
          <span class="chips-label">Popular Filters:</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('PyTorch', this)">PyTorch</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('LangChain', this)">LangChain</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('LangGraph', this)">LangGraph</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('XGBoost', this)">XGBoost</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('FastAPI', this)">FastAPI</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('Streamlit', this)">Streamlit</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('PostgreSQL', this)">PostgreSQL</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('Power BI', this)">Power BI</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('Tableau', this)">Tableau</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('OpenCV', this)">OpenCV</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('SMOTE', this)">SMOTE</span>
          <span class="tech-chip" onclick="toggleTechChipFilter('ARIMA', this)">ARIMA</span>
        </div>
      </div>

      <!-- Active Filter Status Message -->
      <div class="filter-status-banner" id="filterStatusBanner">
        <span id="filterStatusText">Showing all projects</span>
        <button class="reset-link-btn" onclick="clearAllFilters()">Reset All Filters</button>
      </div>

      <!-- Projects Grid Output -->
      <div class="projects-gallery-grid" id="projectsGalleryGrid">
        <!-- Rendered dynamically by JavaScript -->
      </div>
    </section>

    <!-- SCHOLASTIC ACHIEVEMENTS & CERTIFICATIONS -->
    <section class="section container" id="achievements">
      <div class="section-header">
        <span class="section-tag">Honors & Credentials</span>
        <h2 class="section-title">Scholastic Achievements & Global Certifications</h2>
        <p class="section-desc">Demonstrated academic excellence and validated industry credentials.</p>
      </div>

      <div class="achievements-grid">
        <div class="achievement-card">
          <div class="ach-icon-box">🏆</div>
          <div class="ach-content">
            <span class="ach-badge">National Exam</span>
            <h3 class="ach-title">GATE 2025: 98.48 Percentile</h3>
            <p class="ach-org">Conducted by Indian Institute of Technology, Roorkee</p>
            <p class="ach-desc">Secured a nationwide top 1.5% percentile rank in Agricultural Engineering, demonstrating elite technical problem-solving capabilities.</p>
          </div>
        </div>

        <div class="achievement-card">
          <div class="ach-icon-box">🥈</div>
          <div class="ach-content">
            <span class="ach-badge">Academic Honor</span>
            <h3 class="ach-title">Chancellor's Silver Medal Award</h3>
            <p class="ach-org">Awarded by University Chancellor, C.S.A. University</p>
            <p class="ach-desc">Bestowed the Silver Medal for Rank 1st academic performance across the B.Tech program (CPI: 8.25 / 10.0).</p>
          </div>
        </div>

        <div class="achievement-card">
          <div class="ach-icon-box">🌐</div>
          <div class="ach-content">
            <span class="ach-badge">Global AI Program</span>
            <h3 class="ach-title">GCI World April 2026 (Tokyo, Japan)</h3>
            <p class="ach-org">Matsuo-Iwasawa Laboratory, The University of Tokyo</p>
            <p class="ach-desc">Selected and successfully cleared the comprehensive Data Science and AI evaluation organized by University of Tokyo's premier AI lab.</p>
          </div>
        </div>

        <div class="achievement-card">
          <div class="ach-icon-box">📜</div>
          <div class="ach-content">
            <span class="ach-badge">Professional Certification</span>
            <h3 class="ach-title">Oracle Certified Data Science Professional</h3>
            <p class="ach-org">Oracle University</p>
            <p class="ach-desc">Demonstrated proficiency in enterprise machine learning pipelines, model monitoring, MLOps, and scalable cloud deployments.</p>
          </div>
        </div>

        <div class="achievement-card">
          <div class="ach-icon-box">🤖</div>
          <div class="ach-content">
            <span class="ach-badge">AI Foundations</span>
            <h3 class="ach-title">Oracle Certified AI Foundations Associate</h3>
            <p class="ach-org">Oracle University</p>
            <p class="ach-desc">Validated core competencies in generative AI, deep neural networks, natural language processing, and ethical AI practices.</p>
          </div>
        </div>

        <div class="achievement-card">
          <div class="ach-icon-box">📈</div>
          <div class="ach-content">
            <span class="ach-badge">Financial Markets</span>
            <h3 class="ach-title">SEBI &ndash; Investor Certification</h3>
            <p class="ach-org">National Institute of Securities Markets (NISM)</p>
            <p class="ach-desc">Qualified the national regulatory examination in securities markets, portfolio management principles, and risk management.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CONTACT & HIRE ME SECTION -->
    <section class="section container" id="contact">
      <div class="contact-box">
        <span class="section-tag">Let's Connect</span>
        <h2 class="contact-title">Interested in building transformative AI systems together?</h2>
        <p class="contact-subtitle">
          I am actively exploring Full-Time roles in <strong>Machine Learning Engineering</strong>, <strong>Generative AI / LLMOps</strong>, and <strong>Data Science</strong>. Feel free to reach out directly!
        </p>

        <div class="contact-details-row">
          <div class="contact-detail-item" onclick="copyEmail()">
            <span class="detail-label">Institute Email</span>
            <span class="detail-value">ankitk25@iitk.ac.in <span class="copy-hint">(Click to Copy)</span></span>
          </div>

          <a href="https://linkedin.com/in/ankit-kumar" target="_blank" class="contact-detail-item">
            <span class="detail-label">LinkedIn</span>
            <span class="detail-value">linkedin.com/in/ankit-kumar ↗</span>
          </a>

          <a href="https://github.com/Ankitiitk369" target="_blank" class="contact-detail-item">
            <span class="detail-label">GitHub</span>
            <span class="detail-value">github.com/Ankitiitk369 ↗</span>
          </a>
        </div>

        <div class="contact-btn-group">
          <a href="mailto:ankitk25@iitk.ac.in" class="btn btn-primary btn-lg">Send an Email &rarr;</a>
          <a href="main.pdf" target="_blank" class="btn btn-secondary btn-lg">Download Harvard Resume (PDF)</a>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="footer-wrapper">
    <div class="footer container">
      <div class="footer-left">
        <p>&copy; 2026 Ankit Kumar. All rights reserved.</p>
        <p class="footer-sub">M.Tech, Department of Management Sciences (DoMS), Indian Institute of Technology Kanpur.</p>
      </div>
      <div class="footer-right">
        <span class="footer-badge">Built with Vanilla HTML5, CSS3 & Modern JS</span>
      </div>
    </div>
  </footer>

  <!-- Executive Deep-Dive Modal Window -->
  <div class="modal-backdrop" id="projectModal" onclick="handleModalBackdropClick(event)">
    <div class="modal-dialog">
      <button class="modal-close-icon" onclick="closeProjectModal()" aria-label="Close modal">✕</button>
      
      <div class="modal-badges-row" id="modalCategoryBadges"></div>
      <h2 class="modal-project-title" id="modalProjectTitle"></h2>
      
      <div class="modal-metrics-callout" id="modalProjectMetrics"></div>

      <h4 class="modal-subheading">Architectural Overview & Engineering Highlights</h4>
      <ul class="modal-bullets-list" id="modalProjectBullets"></ul>

      <h4 class="modal-subheading">Tech Stack & Dependencies</h4>
      <div class="modal-tech-pills-row" id="modalProjectTech"></div>

      <div class="modal-actions-bar">
        <button class="btn btn-secondary btn-sm" onclick="copyProjectCardInfo()">📋 Copy Project Summary</button>
        <div class="modal-right-actions" id="modalActionButtons"></div>
      </div>
    </div>
  </div>

  <!-- Toast Alert -->
  <div class="toast-popup" id="toast">
    <span id="toastText">✓ Copied to clipboard!</span>
  </div>

  <!-- Embed Master Projects Data -->
  <script>
    const MASTER_PROJECTS_DATA = {projects_json_str};
  </script>
  <!-- Application Logic -->
  <script src="app.js"></script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Generated index.html successfully!")
