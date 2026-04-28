# Deploy Guide — quotes.rendimension.com

## Hosting
- **Provider:** HostGator Mexico
- **cPanel URL:** https://mx98.hostgator.mx:2083
- **Account:** rendimen (Hugo's account)
- **Document root:** /home2/rendimen/quotes.rendimension.com/

## How to Deploy

### Option 1: cPanel File Manager (Manual)
1. Log into cPanel at https://mx98.hostgator.mx:2083
2. Open File Manager
3. Navigate to `/home2/rendimen/quotes.rendimension.com/`
4. Select `index.html` → Click Edit
5. Select all content (Ctrl+A) → Delete
6. Paste the contents of `src/index.html`
7. Click "Save Changes"
8. Visit https://quotes.rendimension.com to verify

### Option 2: cPanel File Manager (Upload)
1. Log into cPanel File Manager
2. Navigate to `/home2/rendimen/quotes.rendimension.com/`
3. Delete the existing `index.html`
4. Click "Upload" in toolbar
5. Upload `src/index.html` (make sure it's named `index.html`)
6. Verify at https://quotes.rendimension.com

### Option 3: FTP (if configured)
```bash
# Using scp or ftp client
scp src/index.html rendimen@mx98.hostgator.mx:/home2/rendimen/quotes.rendimension.com/index.html
```

## SSL Certificate
- The subdomain `quotes.rendimension.com` should have SSL auto-provisioned by HostGator
- If SSL is not active, go to cPanel → SSL/TLS Status → Run AutoSSL
- Force HTTPS redirect is handled by the server (.htaccess or cPanel setting)

## DNS
- Subdomain `quotes` is configured in cPanel → Domains
- Points to `/home2/rendimen/quotes.rendimension.com/`
- No external DNS changes needed (managed by HostGator)

## Post-Deploy Checklist
- [ ] Site loads at https://quotes.rendimension.com
- [ ] SSL certificate is valid (green lock)
- [ ] Hero screen renders correctly
- [ ] Both paths (homeowner/professional) work
- [ ] Services configurator calculates correctly
- [ ] Contact form validates
- [ ] Estimate screen shows correct totals
- [ ] Mobile layout works (test on phone)
- [ ] "View Our Work" link goes to rendimension.com
- [ ] Bottom nav links work (Portfolio → rendimension.com, Contact → rendimension.com/contact)

## Other Subdomains on This Account
- rendimension.com (main site, public_html)
- quotes.rendimension.com (this project)
- sales.rendimension.com
- test.rendimension.com
- virtual.rendimension.com
