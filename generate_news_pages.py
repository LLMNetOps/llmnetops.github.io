#!/usr/bin/env python3
"""
Generate individual HTML pages for news articles from news.json
Usage: python3 generate_news_pages.py
"""

import json
import os
from datetime import datetime

# Template for news article page
ARTICLE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{excerpt}">
    <title>{title} - LLMNetOps</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/responsive.css">
    <link rel="stylesheet" href="../css/components.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div class="nav-container">
            <a href="../index.html" class="logo">
                <img src="../images/llmnetops-logo-formal.png" alt="LLMNetOps Logo">
            </a>
            <button class="mobile-menu-btn" aria-label="Toggle navigation menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-links">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../about.html">About</a></li>
                <li><a href="../activities.html">Activities</a></li>
                <li><a href="../workshops.html">Workshops</a></li>
                <li><a href="../news.html" class="active">News</a></li>
                <li><a href="../resources.html">Resources</a></li>
                <li><a href="../contact.html">Contact</a></li>
            </ul>
            <a href="https://github.com/LLMNetOps" class="nav-github" target="_blank" rel="noopener noreferrer" aria-label="LLMNetOps on GitHub" title="LLMNetOps on GitHub">
                <svg viewBox="0 0 16 16" width="22" height="22" aria-hidden="true" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
                <span>GitHub</span>
            </a>
        </div>
    </nav>

    <!-- Page Header -->
    <section class="page-header">
        <div class="breadcrumb">
            <a href="../index.html">Home</a>
            <span>/</span>
            <a href="../news.html">News</a>
            <span>/</span>
            <span>{breadcrumb_title}</span>
        </div>
    </section>

    <!-- Article Content -->
    <section class="about">
        <div class="container">
            <article class="article-full news-article-page">
                <div class="article-header">
                    <span class="news-category">{category}</span>
                    <time class="news-date" datetime="{date}">
                        {formatted_date}
                    </time>
                </div>
                <h1>{title}</h1>
                
                <div class="article-featured-image">
                    <img src="../{image}" alt="{title}" loading="lazy">
                </div>

                <div class="article-content">
                    {content}

                    {photos_html}
                </div>

                <div class="article-footer">
                    <a href="../news.html" class="btn btn-outline">← Back to News</a>
                </div>
            </article>
        </div>
    </section>

    <!-- Back to Top Button -->
    <button id="back-to-top" class="back-to-top" aria-label="Back to top">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 15l-6-6-6 6"/>
        </svg>
    </button>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>About LLMNetOps</h3>
                <p>Building foundational AI knowledge through locally-hosted open-source LLMs for network operations.</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="../index.html">Home</a></li>
                    <li><a href="../about.html">About</a></li>
                    <li><a href="../activities.html">Activities</a></li>
                    <li><a href="../workshops.html">Workshops</a></li>
                    <li><a href="../news.html">News</a></li>
                    <li><a href="../resources.html">Resources</a></li>
                    <li><a href="../contact.html">Contact</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Funded By</h3>
                <div class="partner-logos">
                    <img src="../images/APNIC-Foundation-and-ISIF-Logo-white-stacked-01.svg" alt="APNIC Foundation and ISIF Logo">
                </div>
            </div>
            <div class="footer-section">
                <h3>Implemented By</h3>
                <div class="partner-logos">
                    <img src="../images/Logo_Universitas_Brawijaya.png" alt="Universitas Brawijaya Logo">
                    <img src="../images/logo-idren.png" alt="IDREN Logo">
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; <span class="current-year">2025</span> LLMNetOps. Funded by ISIF Asia 2025. All rights reserved.</p>
        </div>
    </footer>

    <script src="../js/navigation.js"></script>
    <script src="../js/animations.js"></script>
    <script src="../js/main.js"></script>
</body>
</html>
"""


def format_date(date_string):
    """Format date to 'Month DD, YYYY' format"""
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    return date_obj.strftime('%B %d, %Y')


def generate_photos_html(photos):
    """Generate HTML for photo gallery"""
    if not photos or len(photos) == 0:
        return ""
    
    photos_items = []
    for photo in photos:
        photos_items.append(f"""
                        <figure class="article-photo">
                            <img src="../{photo['url']}" alt="{photo['caption']}" loading="lazy">
                            <figcaption>{photo['caption']}</figcaption>
                        </figure>""")
    
    return f"""
                    <div class="article-photos">
{''.join(photos_items)}
                    </div>"""


def generate_article_page(article, output_dir):
    """Generate individual HTML page for an article"""
    
    # Generate breadcrumb title (shorter version)
    breadcrumb_title = article['title']
    if len(breadcrumb_title) > 50:
        breadcrumb_title = breadcrumb_title[:47] + "..."
    
    # Format date with location if available
    formatted_date = format_date(article['date'])
    if 'location' in article and article['location']:
        formatted_date = f"{formatted_date} | {article['location']}"
    
    # Generate photos HTML
    photos_html = generate_photos_html(article.get('photos', []))
    
    # Fill in the template
    html_content = ARTICLE_TEMPLATE.format(
        title=article['title'],
        excerpt=article['excerpt'],
        category=article['category'],
        date=article['date'],
        formatted_date=format_date(article['date']),
        breadcrumb_title=breadcrumb_title,
        image=article['image'],
        content=article['content'],
        photos_html=photos_html
    )
    
    # Write to file
    filename = f"{article['slug']}.html"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Generated: {filepath}")


def main():
    # Read news.json
    json_path = 'data/news.json'
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found!")
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        articles = json.load(f)
    
    # Create news directory if it doesn't exist
    output_dir = 'news'
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate page for each article
    print(f"\nGenerating {len(articles)} article page(s)...\n")
    
    for article in articles:
        if 'slug' not in article:
            print(f"Warning: Article '{article['title']}' has no slug, skipping...")
            continue
        generate_article_page(article, output_dir)
    
    print(f"\n✓ Done! Generated {len(articles)} page(s) in {output_dir}/")
    print(f"\nYou can now access articles at:")
    for article in articles:
        if 'slug' in article:
            print(f"  - http://localhost:8000/news/{article['slug']}.html")


if __name__ == '__main__':
    main()
