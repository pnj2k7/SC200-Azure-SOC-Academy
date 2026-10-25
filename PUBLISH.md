# Publication and GitHub Pages maintenance

Published repository: [pnj2k7/SC200-Azure-SOC-Academy](https://github.com/pnj2k7/SC200-Azure-SOC-Academy). Published guide: [Wardlight SOC Academy](https://pnj2k7.github.io/SC200-Azure-SOC-Academy/). The initial Pages workflow completed successfully and the course URL returned HTTP 200 on 25 October 2026.

## Update the existing repository

Clone the existing repository, edit the course source, regenerate with `python build_course.py`, run `python scripts/validate.py`, review the diff and push to main. The Pages workflow validates and publishes the site. Check its result and the deployed URL after each update. Keep objective evidence and private training exports outside Git.

## Publish your own independent copy

1. Sign into your own GitHub account and create a new public repository without an initial README/license. Confirm that you intend the original training content to be public. The pnj2k7 repository already exists; do not attempt to recreate it.
2. Upload the contents of this folder, including .github/workflows/pages.yml and .nojekyll. Do not upload the parent Cloud Computing folder; it contains unrelated private learning material. Check that no evidence, tokens, keys or onboarding packages are included.
3. Alternatively use an authenticated Git CLI from a new copy of the course directory. Replace YOUR_ACCOUNT and YOUR_REPOSITORY with your own target:

```bash
git init
git branch -M main
git add .
git commit -m "Add Wardlight SC-200 scenario learning programme"
git remote add origin https://github.com/YOUR_ACCOUNT/YOUR_REPOSITORY.git
git push -u origin main
```

4. In repository Settings > Pages choose GitHub Actions as the source. The included workflow validates the content, creates a clean site artifact and deploys it with GitHub’s Pages actions. No Azure hosting is needed for these static learning pages.
5. Inspect the Pages workflow and open the deployment URL it returns. Your independent copy uses its own account/repository path.
6. Test the landing page, a lab, quiz, coverage page and practical downloads from the deployed URL. Publish the URL only after those checks pass.

## Offline use

Use GitHub Code > Download ZIP, extract and open index.html. Downloadable practical files remain under infra, queries, scripts, notebooks and data. handbook.html is a single-file reading edition; it does not embed the practical source files. No service worker, external font or CDN is required.
