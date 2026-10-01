// LLMNetOps - News JavaScript

document.addEventListener('DOMContentLoaded', function() {
    loadNews();
});

// Load news articles
async function loadNews() {
    try {
        const response = await fetch('data/news.json');
        const newsData = await response.json();
        
        // Sort by date descending (newest first)
        newsData.sort((a, b) => new Date(b.date) - new Date(a.date));
        
        renderNews(newsData);
        loadMedia();
    } catch (error) {
        console.error('Error loading news:', error);
        document.getElementById('news-container').innerHTML = 
            '<p class="error-message">Unable to load news articles. Please try again later.</p>';
    }
}

// Render news articles
function renderNews(newsData) {
    const container = document.getElementById('news-container');
    
    if (newsData.length === 0) {
        container.innerHTML = '<p class="no-content">No news articles available yet. Check back soon!</p>';
        return;
    }
    
    const newsHTML = newsData.map(article => `
        <article class="news-card" data-news-id="${article.id}">
            <div class="news-image">
                <img src="${article.image}" alt="${article.title}" loading="lazy">
                <span class="news-category">${article.category}</span>
            </div>
            <div class="news-content">
                <time class="news-date" datetime="${article.date}">
                    ${formatDate(article.date)}
                </time>
                <h3 class="news-title">${article.title}</h3>
                <p class="news-excerpt">${article.excerpt}</p>
                <a href="news/${article.slug}.html" class="btn btn-outline read-more">
                    Read More
                </a>
            </div>
        </article>
    `).join('');
    
    container.innerHTML = newsHTML;
}

// Format date for display
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

// Load external media coverage
async function loadMedia() {
    const container = document.getElementById('media-container');
    if (!container) return;
    try {
        const response = await fetch('data/media.json');
        const media = await response.json();
        // Sort by date descending where available
        media.sort((a, b) => {
            if (!a.date && !b.date) return 0;
            if (!a.date) return 1;
            if (!b.date) return -1;
            return new Date(b.date) - new Date(a.date);
        });
        container.innerHTML = media.map(m => `
            <article class="news-item">
                <h3><a href="${m.url}" target="_blank" rel="noopener">${m.title}</a></h3>
                <p class="news-meta">${m.source}${m.date ? ' · ' + formatDate(m.date) : ''}</p>
                ${m.summary ? `<p>${m.summary}</p>` : ''}
            </article>
        `).join('');
    } catch (error) {
        console.error('Error loading media coverage:', error);
    }
}
