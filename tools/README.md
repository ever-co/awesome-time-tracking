# Tools

This directory contains local build tooling for repository artifacts.

## Kindle EPUB Builder

`build_kindle_epub.py` converts the Markdown wiki into Kindle-compatible EPUB files.

Run it from the repository root:

```bash
python3 tools/build_kindle_epub.py
```

The script writes:

- `dist/awesome-time-tracking.epub` - one all-in-one EPUB containing the README and every `details/*.md` page.
- `dist/split/Awesome-Time-Tracking-Time-Management-Methods.epub`
- `dist/split/Awesome-Time-Tracking-Personal-Productivity-Tools.epub`
- `dist/split/Awesome-Time-Tracking-Business-Time-Tracking-Software.epub`
- `dist/split/Awesome-Time-Tracking-Workforce-Payroll-and-Compliance.epub`
- `dist/split/Awesome-Time-Tracking-Industry-Specific-Time-Tracking.epub`
- `dist/split/Awesome-Time-Tracking-Calculators-Templates-and-Utilities.epub`

Each generated book starts with a landing page that includes the repository URL:

```text
https://github.com/ever-works/awesome-time-tracking
```

## Split Logic

The split volumes are assigned from `README.md` section headings. For each `##` section, the builder classifies the heading using keyword groups defined in `VOLUMES` inside `build_kindle_epub.py`.

Each linked `details/*.md` page is assigned to the first matching volume where it appears. This avoids duplicate chapters across the split books. Any detail page not linked from the README falls back to the utilities/templates volume.

The beginning-of-book contents page for each split EPUB is grouped by the README sections that contributed articles to that volume. It only links to articles included in that EPUB.

## Markdown Support

The builder intentionally implements a small Markdown subset that matches this wiki:

- headings
- unordered lists
- paragraphs
- fenced code blocks
- links
- inline code
- bold and italic text

Images are converted to their alt text. Internal links to `details/*.md` are rewritten to the generated XHTML files inside the EPUB.

## Validation

Before writing each EPUB, the builder parses every generated XML/XHTML document with Python's XML parser. This catches invalid XML, mismatched tags, and disallowed characters such as null bytes.

After generation, you can also check the EPUB container:

```bash
unzip -t dist/awesome-time-tracking.epub
unzip -t dist/split/Awesome-Time-Tracking-Time-Management-Methods.epub
```

EPUB files can be sent to Kindle using Amazon's Send to Kindle flow.
