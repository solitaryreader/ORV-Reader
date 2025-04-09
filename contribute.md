# Contribution Guide

This guide provides detailed instructions on how to contribute to the ORV-Reader project. Whether you're fixing typos, adding images, or improving the front end, your contributions are welcome!

---

## Index
1. [How to Contribute](#how-to-contribute-browser---quick-guide)
2. [Editing Text Files](#editing-text-files)
3. [Adding Images](#adding-images)
4. [Improving the Front End](#improving-the-front-end)
5. [Important Notes](#important-notes)

---

## How to Contribute (Browser - Quick Guide)

1.  **Fork:** Go to [https://github.com/Bittu5134/ORV-Reader](https://github.com/Bittu5134/ORV-Reader) and click "Fork" (top-right).
2.  **Edit:** In your fork, browse to the file, click the pencil icon ("Edit this file"). Make changes.
3.  **Commit:** Scroll down, add a commit message, and click "Commit changes" (or "Propose changes").
4.  **Pull Request:** Go to your fork, click "Compare & pull request". Add title/description, and click "Create pull request".
5.  **Review:** Wait for maintainer feedback. Update your fork if needed.

> [!Note]
> Most chapters on the [ORV-Reader](http://orv.pages.dev) have a pencil icon which can be used for directly going to the file which you will nead to edit.

---

## Editing Text Files

The following directories contain the text files for different parts of the ORV-Reader project:
- `chapters/orv`: Contains the main story of ORV.
- `chapters/cont`: Contains the sequel (Chapters 553+).
- `chapters/side`: Contains side stories.

### What You Can Edit
- Fix typos or grammatical errors.
- Correct system message types, constellation speech, or outer god dialogues.
- Add missing tags or improve formatting.

Refer to the [Formatting Guide](./formatting.md) for detailed instructions on using tags and formatting styles.

---

## Adding Images

You can contribute by adding illustrations and cover images to the chapters.

### Steps to Add Images
1. Upload the image to the `website/assets/images` folder with a unique name (e.g., `CH512-01.jpg`).
2. Edit the corresponding chapter file to include the image using the `<img>` tag. Refer to the [Formatting Guide](./formatting.md) for the correct syntax.

Example:
```
<img>[CH512-01.jpg][Illustration for Chapter 512]
```

---

## Improving the Front End

If you're up for a challenge, you can contribute to improving the front end of the website.

### Front-End Files
- All front-end files are located in the `/website` directory.
- The files for individual chapters are dynamically generated using GitHub Actions. To edit these, modify the corresponding `template.html` files:
  - `website/stories/orv/read/template.html`
  - `website/stories/cont/read/template.html`
  - `website/stories/side/read/template.html`

### Important Notes
- Do not copy-paste content between template files. Each template contains unique data tags that must remain intact.
- Test your changes locally before submitting a pull request.

---

## Important Notes

- Always follow the [Formatting Guide](./formatting.md) to ensure consistency.
- Avoid making unnecessary changes to dynamically generated files.
- If you're unsure about anything, feel free to open an issue on GitHub for clarification.
- Be respectful and patient during the review process.

Thank you for contributing to the ORV-Reader project!
