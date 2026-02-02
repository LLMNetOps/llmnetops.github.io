# News Section - User Guide

The News & Progress section has been successfully added to your LLMNetOps website with WordPress-style individual post pages!

## What's Been Added

### New Files Created:
1. **news.html** - The main news page displaying all articles in a grid layout
2. **news/** - Directory containing individual article pages (like WordPress posts)
3. **js/news.js** - JavaScript for loading and displaying news articles
4. **data/news.json** - JSON file containing all news article data
5. **generate_news_pages.py** - Python script to automatically generate article pages
6. **CSS updates** - Complete styling for news cards and article pages

### Updates Made:
- Added "News" link to the navigation menu on all pages
- Updated footer Quick Links on all pages to include News
- Each article now has its own URL (e.g., `/news/kickoff-meeting-2025.html`)

## How to Add New News Articles

### Step 1: Add Article to JSON

Edit `data/news.json` and add your new article:

```json
{
    "id": 2,
    "slug": "workshop-march-2025",
    "title": "First Workshop Successfully Completed",
    "date": "2025-03-20",
    "category": "Workshop",
    "excerpt": "Brief summary (2-3 sentences)...",
    "image": "images/news/workshop-march.jpg",
    "content": "<h2>Workshop Highlights</h2><p>Full article...</p>",
    "photos": [
        {
            "url": "images/news/workshop-march-1.jpg",
            "caption": "Description"
        }
    ]
}
```

### Step 2: Generate Article Page

Run the Python script to automatically create the HTML page:

```bash
python3 generate_news_pages.py
```

This will:
- Read all articles from `data/news.json`
- Generate individual HTML pages in the `news/` directory
- Each page will have its own URL based on the `slug`

### Step 3: Done!

Your article is now live at: `http://localhost:8000/news/your-slug.html`

```json
{
    "id": 2,
    "title": "Your Article Title",
    "date": "2025-03-15",
    "category": "Meeting",
    "excerpt": "Short summary that appears on the card (2-3 sentences)",
    "image": "images/news/your-image.jpg",
    "content": "<h2>Main Heading</h2><p>Full article content with HTML formatting...</p>",
    "photos": [
        {
            "url": "images/news/photo1.jpg",
            "caption": "Description of this photo"
        },
        {
            "url": "images/news/photo2.jpg",
            "caption": "Description of another photo"
        }
    ]
}
```

### 📁 Image Organization

Store your news images in `images/news/` directory for better organization:
- Main article images: `images/news/article-name.jpg`
- Additional photos: `images/news/article-name-1.jpg`, `images/news/article-name-2.jpg`
- This keeps news images separate from other site images

### Field Descriptions:

- **id**: Unique number for each article (increment from the last one)
- **slug**: URL-friendly identifier (lowercase, hyphens instead of spaces) - used for the page URL
- **title**: Main headline for the article
- **date**: Publication date in YYYY-MM-DD format
- **category**: Type of article (e.g., "Meeting", "Workshop", "Milestone", "Update")
- **excerpt**: Brief summary shown on the card (keep it concise)
- **image**: Path to the main image (shown on the card) - use `images/news/filename.jpg`
- **content**: Full article content using HTML tags (h2, h3, p, ul, li, etc.)
- **photos**: Optional array of additional photos with captions (also from `images/news/`)

### Example: Adding a Workshop Report

```json
{
    "slug": "workshop-april-2025",
    "id": 2,
    "title": "First Workshop Successfully Completed",
    "date": "2025-04-20",
    "category": "Workshop",
    "excerpt": "Our first hands-on workshop on locally-hosted LLMs brought together 25 network administrators from across Indonesia.",
    "image": "images/news/workshop-1.jpg",
    "content": "<h2>Workshop Highlights</h2><p>On April 20, 2025, we conducted our first hands-on workshop...</p><h3>Topics Covered</h3><ul><li>Introduction to LLMs</li><li>Privacy considerations</li><li>Local hosting setup</li></ul>",
    "photos": [
        {
            "url": "images/news/workshop-1-group.jpg",
            "caption": "Participants during the hands-on session"
        },
        {
            "url": "images/news/workshop-1-demo.jpg",
            "caption": "Live demonstration of LLM setup"
        }
    ]
}
```

## Tips for Writing Content
Choose a good slug** - Keep it short, descriptive, and URL-friendly (e.g., "kickoff-meeting-2025")
2. **Keep excerpts concise** - They show on the card, so 2-3 sentences max
3. **Use clear dates** - Format: YYYY-MM-DD (e.g., 2025-03-15)
4. **Choose good images** - Use high-quality photos (recommended: 800x600px or larger)
5. **Choose good images** - Use high-quality photos (recommended: 800x600px or larger)
4. **Format content properly** - Use HTML tags for structure:
   - `<h2>` for main sections
   - `<h3>` for subsections
   - `<p>` for paragraphs
   - `<ul>` and `<li>` for lists
5. **Add captions to photos** - Help readers understand what they're seeing

## Categories You Can Use

- Meeting
- Workshop
- Milestone
- Update
- Announcement
- Report
- Event

Feel free to create new categories as needed!

## Tesadding to `news.json`:
1. Run: `python3 generate_news_pages.py`
2. Refresh the news page: http://localhost:8000/news.html
3. Click on your article to view the full page

## Workflow Summary

```bash
# 1. Add photos to images/news/
cp my-photo.jpg images/news/

# 2. Edit news.json with your article data
nano data/news.json

# 3. Generate the HTML page
python3 generate_news_pages.py

# 4. View in browser
# Open http://localhost:8000/news.html
```

## Benefits of This Approach

✅ **SEO-Friendly** - Each article has its own URL and metadata  
✅ **Shareable** - Direct links to individual articles  
✅ **Fast Loading** - No modal, faster page loads  
✅ **Better UX** - Users can bookmark specific articles  
✅ **Easy to Update** - Just run the script after editing JSON
2. Refresh the news page
3. Click "Read More" to view the full article in the modal

## Current Sample Article

The `news.json` file includes a sample kickoff meeting article. You can:
- Edit it to match your actual kickoff meeting
- Delete it and add your own articles
- Keep it as a reference

## Need Help?

If you need to:
- Change the layout or styling
- Add new features
- Modify the modal behavior
- Update the grid display

Just let me know!
