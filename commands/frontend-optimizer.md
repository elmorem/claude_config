# Frontend Performance Optimizer

Analyze the provided code and identify performance optimization opportunities across these key areas:

## 1. Assets & Resources
- **Images**: Compress, use modern formats (WebP/AVIF), implement lazy loading
- **CSS/JS**: Minify, remove unused code, implement code splitting
- **Fonts**: Subset fonts, use font-display, preload critical fonts

## 2. Network & Delivery  
- **Requests**: Bundle files, reduce dependencies, enable caching
- **Compression**: Implement GZIP/Brotli for text resources
- **CDN**: Use geographically distributed delivery
- **Protocol**: Leverage HTTP/2+ features

## 3. Rendering & Load
- **Critical Path**: Prioritize above-the-fold CSS/JS
- **Layout**: Minimize reflows/repaints, optimize animations
- **Loading**: Use async/defer for non-critical scripts
- **Rendering**: Consider SSR/SSG for faster initial loads

## 4. Monitoring & Caching
- **Tools**: Use Lighthouse, WebPageTest for analysis
- **Service Workers**: Implement intelligent caching strategies
- **Backend**: Optimize API response times and data efficiency