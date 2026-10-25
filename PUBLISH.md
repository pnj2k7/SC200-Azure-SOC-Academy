# Publish to pnj2k7 on GitHub

Target repository: pnj2k7/SC200-Azure-SOC-Academy. This target name is a proposal until creation is confirmed; no published URL is claimed by these files.

## Publish the reviewed files

1. Sign into GitHub as pnj2k7 and create a new public repository named SC200-Azure-SOC-Academy without an initial README/license. Confirm that you intend the original training content to be public.
2. Upload the contents of this folder, including .github/workflows/pages.yml and .nojekyll. Do not upload the parent Cloud Computing folder; it contains unrelated private learning material. Check that no evidence, tokens, keys or onboarding packages are included.
3. Alternatively use an authenticated Git CLI from this directory:

```bash
git init
git branch -M main
git add .
git commit -m "Add Wardlight SC-200 scenario learning programme"
git remote add origin https://github.com/pnj2k7/SC200-Azure-SOC-Academy.git
git push -u origin main
```

4. In repository Settings > Pages choose GitHub Actions as the source. The included workflow validates the content, creates a clean site artifact and deploys it with GitHub’s Pages actions. No Azure hosting is needed for these static learning pages.
5. Inspect the Pages workflow and open the deployment URL it returns. If using this account/name, the expected address is https://pnj2k7.github.io/SC200-Azure-SOC-Academy/ after successful publication; this is not a live-link claim.
6. Test the landing page, a lab, quiz, coverage page and practical downloads from the deployed URL. Publish the URL only after those checks pass.

## Offline use

Use GitHub Code > Download ZIP, extract and open index.html. Downloadable practical files remain under infra, queries, scripts, notebooks and data. handbook.html is a single-file reading edition; it does not embed the practical source files. No service worker, external font or CDN is required.
