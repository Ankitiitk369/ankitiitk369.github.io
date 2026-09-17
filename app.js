/**
 * ANKIT KUMAR - PORTFOLIO INTERACTIVITY ENGINE
 * Features: Instant Search, Multi-Filter, Tech Chips, Modal Viewer, Theme Toggle, Clipboard
 */

let currentCategory = 'all';
let currentSearch = '';
let currentTechFilter = null;
let currentSort = 'featured';
let activeModalProject = null;

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  // Load saved theme preference
  const savedTheme = localStorage.getItem('ak_portfolio_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  // Initial render
  renderGallery();
});

// Render Projects Gallery
function renderGallery() {
  const container = document.getElementById('projectsGalleryGrid');
  if (!container) return;
  container.innerHTML = '';

  // Filter projects
  let filtered = MASTER_PROJECTS_DATA.filter(project => {
    // 1. Category check
    const matchesCategory = (currentCategory === 'all') || (project.category === currentCategory);

    // 2. Search query check
    const query = currentSearch.toLowerCase().trim();
    const matchesSearch = !query || 
      project.title.toLowerCase().includes(query) ||
      project.domain.toLowerCase().includes(query) ||
      project.badge.toLowerCase().includes(query) ||
      project.metrics.toLowerCase().includes(query) ||
      project.tech.some(t => t.toLowerCase().includes(query)) ||
      project.desc.some(d => d.toLowerCase().includes(query));

    // 3. Tech chip check
    const matchesTech = !currentTechFilter ||
      project.tech.some(t => t.toLowerCase() === currentTechFilter.toLowerCase());

    return matchesCategory && matchesSearch && matchesTech;
  });

  // Sort projects
  if (currentSort === 'alpha') {
    filtered.sort((a, b) => a.title.localeCompare(b.title));
  } else if (currentSort === 'domain') {
    filtered.sort((a, b) => a.domain.localeCompare(b.domain));
  }
  // 'featured' keeps original curated flagship order

  // Update Status Banner
  updateStatusBanner(filtered.length);

  // Empty state handling
  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 70px 20px; color: var(--text-muted);">
        <div style="font-size: 40px; margin-bottom: 12px;">🔍</div>
        <h3 style="font-size: 20px; font-weight: 700; color: var(--text-main); margin-bottom: 8px;">No projects matched your criteria</h3>
        <p style="font-size: 14px; max-width: 480px; margin: 0 auto 20px auto;">Try clearing your search term, switching categories, or resetting the technology filter.</p>
        <button class="btn btn-primary" onclick="clearAllFilters()">Reset All Filters</button>
      </div>
    `;
    return;
  }

  // Render cards
  filtered.forEach(p => {
    const card = document.createElement('article');
    card.className = 'project-card';
    card.onclick = (e) => {
      // Prevent opening modal if clicking direct action links
      if (e.target.tagName === 'A' || e.target.closest('a')) return;
      openProjectModal(p);
    };

    // Tech pills (show first 5 + indicator)
    const techPills = p.tech.slice(0, 5).map(t => 
      `<span class="card-tech-pill" onclick="event.stopPropagation(); filterBySingleTech('${t}')">${t}</span>`
    ).join('');

    const extraTechCount = p.tech.length > 5 ? `<span class="card-tech-pill">+${p.tech.length - 5}</span>` : '';

    // Action buttons
    let actionButtons = '';
    if (p.github) {
      actionButtons += `<a href="${p.github}" target="_blank" class="card-action-btn btn-gh" onclick="event.stopPropagation()">GitHub ↗</a>`;
    }
    if (p.demo) {
      actionButtons += `<a href="${p.demo}" target="_blank" class="card-action-btn btn-live" onclick="event.stopPropagation()">Live App ↗</a>`;
    }
    if (!p.github && !p.demo) {
      actionButtons += `<span style="font-size: 11.5px; color: #f472b6; font-weight: 600;">Enterprise System</span>`;
    }

    card.innerHTML = `
      <div>
        <div class="card-top-row">
          <span class="domain-badge-pill badge-${p.category}">${p.domain}</span>
          <span class="card-academic-badge" title="${p.badge}">${p.badge}</span>
        </div>
        <h3 class="card-project-title">${p.title}</h3>
        <p class="card-summary-snippet">${p.desc[0]}</p>
        <div class="card-metrics-box">${p.metrics}</div>
        <div class="card-tech-chips-row">
          ${techPills}
          ${extraTechCount}
        </div>
      </div>
      <div class="card-actions-bar">
        <div style="display: flex; gap: 6px;">
          ${actionButtons}
        </div>
        <button class="view-details-link" onclick="event.stopPropagation(); openProjectModal(MASTER_PROJECTS_DATA[${MASTER_PROJECTS_DATA.indexOf(p)}])">
          Deep Dive &rarr;
        </button>
      </div>
    `;

    container.appendChild(card);
  });
}

// Category Filter Trigger
function setCategoryFilter(cat) {
  currentCategory = cat;
  document.querySelectorAll('.domain-tab').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-category') === cat);
  });
  renderGallery();
}

// Search Filter Trigger
function applyFilters() {
  const searchInput = document.getElementById('projectSearchInput');
  const sortDropdown = document.getElementById('sortDropdown');
  const clearBtn = document.getElementById('clearSearchBtn');

  currentSearch = searchInput ? searchInput.value : '';
  currentSort = sortDropdown ? sortDropdown.value : 'featured';

  if (clearBtn) {
    clearBtn.style.display = currentSearch ? 'block' : 'none';
  }

  renderGallery();
}

function resetSearch() {
  const searchInput = document.getElementById('projectSearchInput');
  if (searchInput) searchInput.value = '';
  applyFilters();
}

// Tech Filter Chip Toggle
function toggleTechChipFilter(tech, chipEl) {
  if (currentTechFilter === tech) {
    currentTechFilter = null;
    chipEl.classList.remove('active');
  } else {
    currentTechFilter = tech;
    document.querySelectorAll('.tech-chip').forEach(c => c.classList.remove('active'));
    chipEl.classList.add('active');
  }
  renderGallery();
}

function filterBySingleTech(tech) {
  currentTechFilter = tech;
  document.querySelectorAll('.tech-chip').forEach(c => {
    c.classList.toggle('active', c.innerText.toLowerCase() === tech.toLowerCase());
  });
  triggerToast(`Filtering by technology: ${tech}`);
  renderGallery();
  // Smooth scroll to projects section
  const projectsSec = document.getElementById('projects');
  if (projectsSec) projectsSec.scrollIntoView({ behavior: 'smooth' });
}

// Status Banner Update
function updateStatusBanner(count) {
  const banner = document.getElementById('filterStatusBanner');
  const bannerText = document.getElementById('filterStatusText');
  if (!banner || !bannerText) return;

  const isFiltered = (currentCategory !== 'all') || (currentSearch !== '') || (currentTechFilter !== null);

  if (isFiltered) {
    banner.style.display = 'flex';
    const conditions = [];
    if (currentCategory !== 'all') conditions.push(`Domain: ${currentCategory.toUpperCase()}`);
    if (currentSearch) conditions.push(`Query: "${currentSearch}"`);
    if (currentTechFilter) conditions.push(`Tech: ${currentTechFilter}`);
    bannerText.innerHTML = `Showing <strong>${count}</strong> matching projects (${conditions.join(' &bull; ')})`;
  } else {
    banner.style.display = 'none';
  }
}

// Reset All Filters
function clearAllFilters() {
  currentCategory = 'all';
  currentSearch = '';
  currentTechFilter = null;
  currentSort = 'featured';

  const searchInput = document.getElementById('projectSearchInput');
  if (searchInput) searchInput.value = '';

  const sortDropdown = document.getElementById('sortDropdown');
  if (sortDropdown) sortDropdown.value = 'featured';

  const clearBtn = document.getElementById('clearSearchBtn');
  if (clearBtn) clearBtn.style.display = 'none';

  document.querySelectorAll('.domain-tab').forEach(b => {
    b.classList.toggle('active', b.getAttribute('data-category') === 'all');
  });

  document.querySelectorAll('.tech-chip').forEach(c => c.classList.remove('active'));

  renderGallery();
  triggerToast('Reset all filters — Showing all 45 projects');
}

// Executive Modal Controls
function openProjectModal(project) {
  activeModalProject = project;
  const modal = document.getElementById('projectModal');
  if (!modal) return;

  document.getElementById('modalProjectTitle').innerText = project.title;
  document.getElementById('modalCategoryBadges').innerHTML = `
    <span class="domain-badge-pill badge-${project.category}">${project.domain}</span>
    <span class="card-academic-badge" style="font-size: 12.5px;">${project.badge}</span>
  `;
  document.getElementById('modalProjectMetrics').innerText = project.metrics;

  const bulletsHtml = project.desc.map(item => `<li>${item}</li>`).join('');
  document.getElementById('modalProjectBullets').innerHTML = bulletsHtml;

  const techHtml = project.tech.map(t => 
    `<span class="card-tech-pill" style="font-size: 12px; padding: 4px 10px;">${t}</span>`
  ).join('');
  document.getElementById('modalProjectTech').innerHTML = techHtml;

  let actionsHtml = '';
  if (project.github) {
    actionsHtml += `<a href="${project.github}" target="_blank" class="btn btn-secondary btn-sm">View on GitHub ↗</a>`;
  }
  if (project.demo) {
    actionsHtml += `<a href="${project.demo}" target="_blank" class="btn btn-primary btn-sm">Open Live App ↗</a>`;
  }
  document.getElementById('modalActionButtons').innerHTML = actionsHtml;

  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeProjectModal() {
  const modal = document.getElementById('projectModal');
  if (modal) modal.classList.remove('active');
  document.body.style.overflow = 'auto';
}

function handleModalBackdropClick(e) {
  if (e.target.id === 'projectModal') {
    closeProjectModal();
  }
}

// Close modals on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeProjectModal();
    closeResumeModal();
  }
});

// Resume Lightbox Controller
let currentLightboxMasterPage = 1;

function openResumeLightbox(imageSrc, title, pdfUrl, masterPageNum = 0) {
  const modal = document.getElementById('resumeLightboxModal');
  const img = document.getElementById('lightboxResumeImg');
  const titleEl = document.getElementById('lightboxResumeTitle');
  const downloadBtn = document.getElementById('lightboxDownloadBtn');
  const pageControls = document.getElementById('lightboxPageControls');
  const btnP1 = document.getElementById('btnPage1');
  const btnP2 = document.getElementById('btnPage2');

  if (!modal || !img) return;

  img.src = imageSrc;
  if (titleEl) titleEl.innerText = title;
  if (downloadBtn && pdfUrl) {
    downloadBtn.href = pdfUrl;
  }

  if (masterPageNum > 0) {
    currentLightboxMasterPage = masterPageNum;
    if (pageControls) pageControls.style.display = 'inline-flex';
    if (btnP1 && btnP2) {
      if (masterPageNum === 1) {
        btnP1.className = 'btn btn-primary btn-sm';
        btnP2.className = 'btn btn-secondary btn-sm';
      } else {
        btnP1.className = 'btn btn-secondary btn-sm';
        btnP2.className = 'btn btn-primary btn-sm';
      }
    }
  } else {
    if (pageControls) pageControls.style.display = 'none';
  }

  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function switchResumeLightboxPage(pageNum) {
  currentLightboxMasterPage = pageNum;
  const img = document.getElementById('lightboxResumeImg');
  const titleEl = document.getElementById('lightboxResumeTitle');
  const btnP1 = document.getElementById('btnPage1');
  const btnP2 = document.getElementById('btnPage2');

  if (pageNum === 1) {
    if (img) img.src = 'preview_main-1.png';
    if (titleEl) titleEl.innerText = 'Master Resume — Page 1';
    if (btnP1) btnP1.className = 'btn btn-primary btn-sm';
    if (btnP2) btnP2.className = 'btn btn-secondary btn-sm';
  } else {
    if (img) img.src = 'preview_main-2.png';
    if (titleEl) titleEl.innerText = 'Master Resume — Page 2';
    if (btnP1) btnP1.className = 'btn btn-secondary btn-sm';
    if (btnP2) btnP2.className = 'btn btn-primary btn-sm';
  }
}

function closeResumeModal() {
  const modal = document.getElementById('resumeLightboxModal');
  if (modal) modal.classList.remove('active');
  document.body.style.overflow = 'auto';
}

function handleResumeBackdropClick(e) {
  if (e.target.id === 'resumeLightboxModal') {
    closeResumeModal();
  }
}


// Copy Project Card Info
function copyProjectCardInfo() {
  if (!activeModalProject) return;
  const copyString = `${activeModalProject.title}
Domain: ${activeModalProject.domain} (${activeModalProject.badge})
Stack: ${activeModalProject.tech.join(', ')}
Key Metrics: ${activeModalProject.metrics}
Highlights:
${activeModalProject.desc.map(d => '- ' + d).join('\n')}
${activeModalProject.github ? 'Repository: ' + activeModalProject.github : 'Enterprise System'}`;

  navigator.clipboard.writeText(copyString).then(() => {
    triggerToast('✓ Full project summary copied to clipboard!');
  });
}

// Copy Email
function copyEmail() {
  const email = 'ankitk25@iitk.ac.in';
  navigator.clipboard.writeText(email).then(() => {
    triggerToast(`✓ Copied email: ${email}`);
  });
}

// Toast Alert
function triggerToast(message) {
  const toast = document.getElementById('toast');
  const toastText = document.getElementById('toastText');
  if (!toast || !toastText) return;

  toastText.innerText = message;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2800);
}

// Dark/Light Theme Switcher
function toggleTheme() {
  const html = document.documentElement;
  const current = html.getAttribute('data-theme') || 'dark';
  const target = current === 'dark' ? 'light' : 'dark';

  html.setAttribute('data-theme', target);
  localStorage.setItem('ak_portfolio_theme', target);
  updateThemeIcon(target);
  triggerToast(`Switched to ${target === 'dark' ? 'Dark Obsidian' : 'Executive Light'} mode`);
}

function updateThemeIcon(theme) {
  const icon = document.getElementById('themeIcon');
  if (icon) {
    icon.innerText = theme === 'dark' ? '🌙' : '☀️';
  }
}
