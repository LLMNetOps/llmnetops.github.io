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
