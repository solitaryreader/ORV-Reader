# Contribution Guide

This guide provides detailed instructions on how to contribute to the ORV-Reader project. Whether you're fixing typos, adding images, or improving the front end, your contributions are welcome!

---

## Index
1. [How to Contribute](#how-to-contribute)
   - [Forking the Repository](#forking-the-repository)
   - [Cloning the Repository](#cloning-the-repository)
   - [Making Changes](#making-changes)
   - [Submitting a Pull Request](#submitting-a-pull-request)
2. [Editing Text Files](#editing-text-files)
3. [Adding Images](#adding-images)
4. [Improving the Front End](#improving-the-front-end)
5. [Important Notes](#important-notes)

---

## How to Contribute

### Forking the Repository
1. Go to the [GitHub repository](https://github.com/Bittu5134/ORV-Reader).
2. Click the "Fork" button in the top-right corner to create a copy of the repository in your GitHub account.

### Cloning the Repository
1. Clone your forked repository to your local machine:
   ```
   git clone https://github.com/<your-username>/ORV-Reader.git
   ```
   Replace `<your-username>` with your GitHub username.

2. Navigate to the project directory:
   ```
   cd ORV-Reader
   ```

### Making Changes
1. Identify the files you want to edit. Refer to the sections below for specific instructions on editing text files, adding images, or improving the front end.
2. Make your changes following the guidelines provided in this document and the [Formatting Guide](./formatting.md).

### Submitting a Pull Request
1. Commit your changes with a meaningful message:
   ```
   git add .
   git commit -m "Describe your changes"
   ```
2. Push your changes to your forked repository:
   ```
   git push origin main
   ```
3. Go to your forked repository on GitHub and click the "Pull Request" button.
4. Provide a clear description of the changes you made and submit the PR.
5. Wait for the maintainers to review your PR. If changes are requested, update your branch and push the changes.

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