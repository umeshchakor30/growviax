# Growviax Global - Complete Website Architecture & Functionality Manual

> **Purpose:** Single source of truth for all website features, architecture, interactive components, SEO configuration, favicon rules, and deployment procedures. Refer to this document instead of inspecting multiple code files.

---

## 1. Project Overview & Hosting Architecture

* **Official Domain:** [`https://growviaxglobal.com`](https://growviaxglobal.com/)
* **Platform:** Static HTML5 / CSS3 / Vanilla ES6 JavaScript
* **Hosting Provider:** GitHub Pages
* **Repository:** `umeshchakor30/growviax`
* **Production Branch:** `main`
* **Custom Domain Config:** Defined via the root [`CNAME`](file:///d:/mearn/Growviax/CNAME) file (`growviaxglobal.com`).
* **Deployment Trigger:** Automatic build & deployment triggered on every push to `origin/main`.

---

## 2. Directory Structure & Key Files

```text
Growviax/
├── CNAME                  # Custom domain routing for GitHub Pages (growviaxglobal.com)
├── favicon.ico            # Root multi-layer favicon (16x16, 32x32, 48x48) for Googlebot & browsers
├── favicon.png            # High-resolution 192x192 PNG icon for modern devices & Google Search
├── robots.txt             # Search crawler permissions and sitemap pointer
├── sitemap.xml            # XML sitemap indexing all public pages with priority weighting
├── SITE_DOCUMENTATION.md  # Complete project architecture & maintenance manual (This file)
│
├── css/
│   ├── style.css          # Core design tokens, theme colors, typography & layout styling
│   ├── components.css     # Buttons, badges, glassmorphism cards, modals, and navbar/footer styles
│   └── responsive.css     # Mobile, tablet, and ultra-wide display media queries
│
├── js/
│   ├── main.js            # Core interactive logic (filtering, quick-view modal, swiper, scroll)
│   └── animations.js      # Scroll-triggered animations and UI micro-interactions
│
├── images/                # Visual assets, branding logos, product photos, category thumbnails
│   └── products/          # High-resolution export commodity imagery
│
└── HTML Pages/
    ├── index.html         # Homepage: Hero section, product categories, certifications, trust metrics
    ├── products.html      # Full product catalog with dynamic category filters & quick-view modals
    ├── about.html         # Company history, export certifications, farm-to-port supply chain
    ├── contact.html       # Contact form, direct WhatsApp CTA, corporate office details & map
    ├── videos.html        # Video gallery showing sourcing, processing, and packaging
    ├── privacy-policy.html# Privacy policy compliance for global trade partners
    └── terms-of-service.html # International export trade terms (FOB/CIF), payment & sample policies
```

---

## 3. Page Inventory & Functionalities

### 3.1 Homepage ([`index.html`](file:///d:/mearn/Growviax/index.html))
* **Hero Split Section:** High-impact value proposition with dynamic call-to-action buttons.
* **Hero Swiper Carousel:** Card-effect auto-advancing carousel showcasing featured export categories.
* **Category Previews:** Direct links to core export divisions (Spices, Dehydrated Products, Dairy, Fresh Produce).
* **Corporate Trust & Quality Badges:** Highlights APEDA, FSSAI, IEC, and international testing compliance.
* **Process & Supply Chain Flow:** 4-step farm sourcing, lab testing, grading, and global freight dispatch.
* **Testimonials / Global Reach Counter:** Corporate statistics and international partner network.

### 3.2 Product Catalog ([`products.html`](file:///d:/mearn/Growviax/products.html))
* **Category Filtering System:** Instant, client-side filtering without page reload:
  * `All Products`
  * `Spices` (Turmeric, Cumin, Chilli, Coriander, Black Pepper, Cardamom, Fennel)
  * `Dehydrated Powder` (Onion Powder, Garlic Powder, Beetroot Powder, Ginger Powder)
  * `Dehydrated Flakes` (Onion Flakes, Garlic Flakes)
  * `Dairy Products` (Pure Cow Ghee, Skimmed Milk Powder)
  * `Honey & Fresh Produce` (Raw Pure Honey, Fresh Red Onions, Grapes, Pomegranates)
* **Interactive Product Cards:** Displays category badge, high-res image, product name, and quick-view button.
* **AOS Animation Sync:** Re-triggers scroll animations automatically when filters change.

### 3.3 Product Quick-View Offcanvas & Image Modal
* **Offcanvas Preview:** Clicking "Quick View" extracts product title and photo from the card dynamically and presents specifications in a slide-out drawer.
* **Full-Screen Image Modal:** Clicking the image inside the quick-view drawer opens the high-resolution photo in an expanded modal dialog for detailed inspection.

### 3.4 About Us ([`about.html`](file:///d:/mearn/Growviax/about.html))
* **Company Profile:** Details Growviax Global’s founding, mission, and sustainable farming network.
* **Export Certifications:** Displays verified credentials:
  * Import-Export Code (IEC: `ALXPL1671J`)
  * FSSAI License (`21526072001794`)
  * GSTIN (`27ALXPL1671J1ZG`)
* **Supply Chain Infrastructure:** Details farm-level aggregation, sorting, lab validation, vacuum/export packaging, and port handling.

### 3.5 Contact Page ([`contact.html`](file:///d:/mearn/Growviax/contact.html))
* **Direct Inquiry Form:** Allows buyers to specify product interests, quantity, and target port.
* **Direct Communication Channels:** Instant links for WhatsApp chat, direct phone dialers, and corporate email.
* **Headquarters Location:** Nashik, Maharashtra, India (Agricultural trade hub).

### 3.6 Media & Videos ([`videos.html`](file:///d:/mearn/Growviax/videos.html))
* **GLightbox Integration:** Video gallery with responsive lightbox popups showcasing farm sourcing, dehydrated processing plants, and cold-chain packaging.

### 3.7 Legal & Compliance Pages
* **[`privacy-policy.html`](file:///d:/mearn/Growviax/privacy-policy.html):** Covers cookie handling, buyer data retention, and international compliance.
* **[`terms-of-service.html`](file:///d:/mearn/Growviax/terms-of-service.html):** Standard export contracts, Incoterms (FOB/CIF/CFR), sample shipment terms, and inspection protocols.

---

## 4. Interactive JavaScript Features ([`js/main.js`](file:///d:/mearn/Growviax/js/main.js))

| Feature | Implementation | Description |
| :--- | :--- | :--- |
| **Page Preloader** | `#preloader` fade-out | Displays animated logo preloader until DOM and assets are fully loaded. |
| **Frosted Glass Navbar** | `.navbar-custom.scrolled` | Automatically adds backdrop blur and solid background when scrolled past 50px. |
| **Active Nav Highlighter** | `location.pathname` | Automatically highlights the current page link in the header navigation. |
| **Back-to-Top Button** | `#back-to-top` | Fades in after 300px scroll; triggers smooth scroll back to window top. |
| **Hero Card Swiper** | `new Swiper('.hero-swiper')` | 3D card transition effect with 3.5s autoplay and pagination dots. |
| **Product Filter** | `.filter-btn` event listener | Toggles `.product-item` visibility based on `data-filter` and refreshes AOS offsets. |
| **Quick-View Drawer** | Event delegation on card | Extracts title and image to populate `#productQuickView` offcanvas. |
| **Full-Size Image Modal** | `#qv-img` click event | Seamlessly transitions from offcanvas drawer to full `#imageModal` popup. |

---

## 5. SEO, Search Engine Indexing & Favicon Configuration

### 5.1 Google Verification & Meta Stack
Every HTML page contains standardized header meta tags:
* **Google Site Verification:** `<meta name="google-site-verification" content="cA3f37711IE6q2VHefm2i210F4O66GIMHW2HYy77rdI" />`
* **Open Graph (Social):** Standardized `og:type`, `og:title`, `og:description`, `og:image`, and `og:url`.
* **Twitter Cards:** `twitter:card`, `twitter:image`, and title/description metadata.
* **Robots Directives:** `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1`

### 5.2 Favicon Stack (Google Search Requirement)
To ensure Google Search displays the Growviax logo instead of the fallback globe, the site strictly enforces:
```html
<!-- Favicon & Search Engine Icons -->
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon.png">
<link rel="apple-touch-icon" href="/favicon.png">
```
* **[`favicon.ico`](file:///d:/mearn/Growviax/favicon.ico):** Root file containing 16×16, 32×32, and 48×48 multi-resolution layers (required by Google's S2 cache and legacy crawlers).
* **[`favicon.png`](file:///d:/mearn/Growviax/favicon.png):** High-resolution 192×192 PNG (multiple of 48px, adhering to Google Search Central guidelines).
* **URL Stability Rule:** **Never change the file names or paths of `favicon.ico` or `favicon.png`**. Frequent renaming resets Google's stability timer.

---

## 6. Deployment & Maintenance SOP

### 6.1 Making & Pushing Changes
Whenever you update code, content, or images, run the following commands:
```bash
# 1. Check changed files
git status

# 2. Stage changes
git add .

# 3. Commit with a descriptive message
git commit -m "Your update description"

# 4. Deploy to live server
git push origin main
```

### 6.2 Cache-Busting for Images
If you replace an existing image file (e.g. updating product photo) without changing its filename, browsers and CDNs may serve the old version from cache. Always add a version query parameter in HTML:
```html
<!-- Example: adding ?v=2 to force refresh -->
<img src="images/products/turmeric.jpeg?v=2" alt="Turmeric">
```

### 6.3 Prompting Google to Update Search Results
Whenever you update SEO meta tags or after favicon deployment:
1. Open [Google Search Console](https://search.google.com/search-console).
2. Select property **`growviaxglobal.com`**.
3. In the top inspection bar, enter: `https://growviaxglobal.com/`
4. Click **Request Indexing**.
5. Wait for Googlebot to recrawl (typically 2–7 business days).

---

## 7. Troubleshooting Quick Reference

| Issue | Root Cause | Solution |
| :--- | :--- | :--- |
| **Favicon not showing in Google Search** | Google S2 cache hasn't crawled `/favicon.ico` yet | Ensure `/favicon.ico` returns 200 OK; submit homepage in Google Search Console URL Inspection. |
| **Favicon showing in tab but not Google** | Browser reads local DOM; Google reads its own independent cache | Do not rename files. Request indexing in Google Search Console and allow crawler schedule time. |
| **GitHub Pages deploy delayed** | GitHub Actions runners experiencing incident or queue backlog | Check `https://www.githubstatus.com` under "Actions" and "Pages". No manual action needed. |
| **Updated image not visible on live site** | Browser/CDN caching previous image file | Hard refresh (`Ctrl + Shift + R`) or append `?v=2` query parameter to the `src` attribute. |
