// LLMNetOps - Home page news ticker (auto-scrolling)

// External media coverage (also listed on about.html)
const MEDIA_COVERAGE = [
    {
        title: 'DTI UB Holds LLMNetOps Pilot Test with IDREN Partner Universities',
        source: 'Universitas Brawijaya News',
        url: 'https://prasetya.ub.ac.id/en/dti-ub-gelar-pilot-test-llmnetops-bersama-universitas-mitra-idren/'
    },
    {
        title: 'UB Receives International Research Funding of USD 30,000 from ISIF Asia for Developing AI System',
        source: 'Universitas Brawijaya News',
        url: 'https://prasetya.ub.ac.id/en/ub-raih-pendanaan-riset-internasional-usd-30-000-dari-isif-asia-untuk-kembangkan-sistem-ai/'
    },
    {
        title: 'Universitas Brawijaya Secures US$30,000 Research Funding from ISIF Asia to Develop AI System',
        source: 'Bisnis Surabaya',
        url: 'https://surabaya.bisnis.com/read/20251029/531/1924246/kembangkan-sistem-ai-universtas-brawijaya-raih-pendanaan-riset-us30000-dari-isif-asia'
    },
    {
        title: 'LLMNetOps: Strengthening Network Operations Knowledge Through Locally-Hosted Generative AI',
        source: 'APNIC Foundation',
        url: 'https://apnic.foundation/projects/llmnetops/'
    }
];

document.addEventListener('DOMContentLoaded', initNewsTicker);

function escapeHTML(str) {
    const el = document.createElement('div');
    el.textContent = str;
    return el.innerHTML;
}

function formatNewsDate(dateString) {
    return new Date(dateString).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

async function initNewsTicker() {
    const track = document.getElementById('news-ticker-track');
    if (!track) return;

    let own = [];
    try {
        const res = await fetch('data/news.json');
        own = await res.json();
        own.sort((a, b) => new Date(b.date) - new Date(a.date));
    } catch (error) {
        console.error('Error loading news:', error);
    }

    const ownCards = own.map(a => `
        <a class="ticker-card ticker-card-own" href="news/${a.slug}.html">
            <div class="ticker-image"><img src="${a.image}" alt="" loading="lazy"></div>
            <div class="ticker-body">
                <span class="ticker-tag">${escapeHTML(a.category)} · ${formatNewsDate(a.date)}</span>
                <h3>${escapeHTML(a.title)}</h3>
            </div>
        </a>`);

    const mediaCards = MEDIA_COVERAGE.map(m => `
        <a class="ticker-card ticker-card-media" href="${m.url}" target="_blank" rel="noopener">
            <div class="ticker-body">
                <span class="ticker-tag">In the media · ${escapeHTML(m.source)}</span>
                <h3>${escapeHTML(m.title)}</h3>
            </div>
        </a>`);

    // Interleave: project news and media coverage alternate
    const cards = [];
    for (let i = 0; i < Math.max(ownCards.length, mediaCards.length); i++) {
        if (ownCards[i]) cards.push(ownCards[i]);
        if (mediaCards[i]) cards.push(mediaCards[i]);
    }

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const html = cards.join('');
    // Duplicate the set (hidden from assistive tech) for a seamless loop
    track.innerHTML = reduceMotion
        ? html
        : html + `<div class="ticker-dup" aria-hidden="true">${html.replace(/<a /g, '<a tabindex="-1" ')}</div>`;

    if (!reduceMotion) {
        // Constant speed regardless of how many items there are (~60px/s)
        const half = track.scrollWidth / 2;
        track.style.setProperty('--ticker-duration', Math.max(20, half / 60) + 's');
        track.classList.add('is-animated');
    }
}
