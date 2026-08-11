# 📦 High Desert Eclipse - Assets Directory

**Directory:** `projects/high-desert-eclipse/assets/`

---

## 🎬 Local Media & 360 Video Assets
This directory stores local static media assets (360° panorama images, video teasers, and optimized WebXR clips).

### 📹 Video Asset Storage Guidelines:
* **File Size Limit:** GitHub allows standard git commits for files up to **100 MB** (warning at 50 MB).
* **10.5 MB `.mp4` Status:** A 10.5 MB `.mp4` video fits well under GitHub's 50MB warning threshold and **does NOT require Git LFS** (Git Large File Storage).
* **Native WebXR Streaming:** Storing the 10.5 MB `.mp4` here allows `<video>` and A-Frame (`<a-videosphere>`) in `index.html` to stream native 360° drag panning directly in the browser without YouTube iframe restrictions!

---

## 📂 Expected File Layout
* `assets/Total-Solar-Eclipse_360-4k-Time-lapse_from_High-Desert-Eclipse.mp4` (Optimized 10.5 MB 360 video clip)
* `assets/poster.jpg` (High-resolution preview thumbnail)
