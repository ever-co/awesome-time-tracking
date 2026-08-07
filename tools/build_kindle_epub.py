#!/usr/bin/env python3
"""Build a Kindle-compatible EPUB from this Markdown wiki."""

from __future__ import annotations

import html
import mimetypes
import posixpath
import re
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
DETAILS = ROOT / "details"
OUT = ROOT / "dist" / "awesome-time-tracking.epub"
TITLE = "Awesome Time Tracking"
AUTHOR = "Ever Works"
REPO_URL = "https://github.com/ever-works/awesome-time-tracking"

CSS = """
body {
  font-family: serif;
  line-height: 1.45;
  margin: 0 5%;
}
h1, h2, h3, h4 {
  font-family: sans-serif;
  line-height: 1.2;
  page-break-after: avoid;
}
h1 {
  font-size: 1.7em;
}
a {
  color: inherit;
}
code, pre {
  font-family: monospace;
}
pre {
  white-space: pre-wrap;
  border-left: 0.2em solid #999;
  padding-left: 0.8em;
}
li {
  margin: 0.25em 0;
}
""".strip()

VOLUMES = [
    (
        "01-methods",
        "Awesome Time Tracking: Time Management Methods",
        ("method", "practice", "philosophy", "principle", "technique", "thought leader", "research", "statistic", "concept", "policy", "neuroscience", "time blocking", "student"),
    ),
    (
        "02-personal-productivity",
        "Awesome Time Tracking: Personal Productivity Tools",
        ("productivity", "personal", "pomodoro", "timer", "browser", "desktop", "mobile", "digital wellness", "health", "gtd", "accessibility", "virtual coworking", "work-life"),
    ),
    (
        "03-business-software",
        "Awesome Time Tracking: Business Time Tracking Software",
        ("software", "automatic", "automated", "analytics", "professional services", "project", "team", "business", "client", "commerce", "billing", "resource", "integration", "apis", "api", "cli", "open source", "developer", "web based", "work management", "work os"),
    ),
    (
        "04-workforce-compliance",
        "Awesome Time Tracking: Workforce, Payroll, and Compliance",
        ("attendance", "payroll", "workforce", "employee", "scheduling", "monitoring", "compliance", "overtime", "legal", "government", "hr", "privacy", "tax", "workplace", "global team", "remote work"),
    ),
    (
        "05-industry-specific",
        "Awesome Time Tracking: Industry-Specific Time Tracking",
        ("construction", "healthcare", "field", "equipment", "fleet", "industry", "creative agencies", "freelance", "freelancers", "nonprofit", "hardware", "physical time clocks", "mobile workforce"),
    ),
    (
        "06-utilities-templates",
        "Awesome Time Tracking: Calculators, Templates, and Utilities",
        ("utilities", "calculators", "calculator", "templates", "template", "time clock", "world clock", "meeting planner", "rate", "timesheet", "overview", "feature", "technology", "roi", "comparison", "criticism", "process", "tool", "others"),
    ),
]


def epub_filename(title: str) -> str:
    """Return a Kindle-friendly filename matching the book title."""
    safe = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-")
    return f"{safe}.epub"


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "section"


def page_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return path.stem.replace("-", " ").title()


def discover_detail_order(readme: str) -> tuple[list[Path], dict[Path, str]]:
    seen: set[Path] = set()
    ordered: list[Path] = []
    titles: dict[Path, str] = {}
    for line in readme.splitlines():
        match = re.search(r"\]\((?:/)?details/([^)#]+\.md)(?:#[^)]+)?\)", line)
        if not match:
            continue
        path = DETAILS / match.group(1)
        if path.exists() and path not in seen:
            seen.add(path)
            ordered.append(path)
            first_link = re.search(r"\[([^\]]+)\]\([^)]+\)", line)
            if first_link:
                titles[path] = re.sub(r"\s+", " ", first_link.group(1)).strip()

    for path in sorted(DETAILS.glob("*.md")):
        if path not in seen:
            ordered.append(path)
    return ordered, titles


def detail_path_from_link(line: str) -> Path | None:
    match = re.search(r"\]\((?:/)?details/([^)#]+\.md)(?:#[^)]+)?\)", line)
    if not match:
        return None
    path = DETAILS / match.group(1)
    return path if path.exists() else None


def parse_readme_sections(readme: str) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    current_title: str | None = None
    current_lines: list[str] = []

    for line in readme.splitlines():
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            if current_title is not None:
                sections.append((current_title, current_lines))
            current_title = heading.group(1)
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        sections.append((current_title, current_lines))
    return sections


def classify_section(title: str) -> str:
    normalized = title.lower()
    for slug, _book_title, keywords in VOLUMES:
        if any(keyword in normalized for keyword in keywords):
            return slug
    return "06-utilities-templates"


def split_details_by_volume(readme: str, all_details: list[Path]) -> dict[str, list[Path]]:
    return {
        slug: [path for _section, paths in section_list for path in paths]
        for slug, section_list in split_sections_by_volume(readme, all_details).items()
    }


def split_sections_by_volume(readme: str, all_details: list[Path]) -> dict[str, list[tuple[str, list[Path]]]]:
    by_volume: dict[str, list[tuple[str, list[Path]]]] = {slug: [] for slug, _title, _keywords in VOLUMES}
    assigned: set[Path] = set()

    for section_title, lines in parse_readme_sections(readme):
        if section_title.startswith(("🔥", "📑", "🍺", "⭐", "™", "🛡")):
            continue
        slug = classify_section(section_title)
        section_paths: list[Path] = []
        for line in lines:
            path = detail_path_from_link(line)
            if path and path not in assigned:
                section_paths.append(path)
                assigned.add(path)
        if section_paths:
            by_volume[slug].append((section_title, section_paths))

    unassigned = [path for path in all_details if path not in assigned]
    if unassigned:
        by_volume["06-utilities-templates"].append(("Other Detail Pages", unassigned))

    return by_volume


def inline_markdown(text: str) -> str:
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"HTMLPLACEHOLDER{len(placeholders) - 1}TOKEN"

    def link_repl(match: re.Match[str]) -> str:
        label = inline_markdown(match.group(1))
        target = match.group(2)
        href = rewrite_href(target)
        return stash(f'<a href="{html.escape(href, quote=True)}">{label}</a>')

    text = html.escape(text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", lambda m: m.group(1), text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, text)
    text = re.sub(r"`([^`]+)`", lambda m: stash(f"<code>{m.group(1)}</code>"), text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", text)
    text = re.sub(r"_([^_]+)_", r"<em>\1</em>", text)
    for idx, value in enumerate(placeholders):
        text = text.replace(f"HTMLPLACEHOLDER{idx}TOKEN", value)
    return text


def rewrite_href(target: str) -> str:
    if re.match(r"^[a-z][a-z0-9+.-]*:", target):
        return target
    if target.startswith("#"):
        return target

    target = target.lstrip("/")
    path, marker, fragment = target.partition("#")
    if path == "README.md":
        href = "readme.xhtml"
    elif path.startswith("details/") and path.endswith(".md"):
        href = f"details/{Path(path).stem}.xhtml"
    else:
        href = path
    if marker:
        href += f"#{fragment}"
    return href


def markdown_to_body(markdown: str, *, title: str | None = None) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    list_stack: list[int] = []
    paragraph: list[str] = []
    in_code = False
    code_lines: list[str] = []

    def close_paragraph() -> None:
        if paragraph:
            out.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_lists(to_level: int = 0) -> None:
        while len(list_stack) > to_level:
            out.append("</ul>")
            list_stack.pop()

    def heading_id(text: str) -> str:
        base = slugify(text)
        existing = {m.group(1) for m in re.finditer(r'id="([^"]+)"', "\n".join(out))}
        if base not in existing:
            return base
        i = 1
        while f"{base}-{i}" in existing:
            i += 1
        return f"{base}-{i}"

    if title:
        out.append(f"<h1 id=\"{slugify(title)}\">{html.escape(title)}</h1>")

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            close_paragraph()
            close_lists()
            if in_code:
                out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines.clear()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            close_paragraph()
            close_lists()
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            close_paragraph()
            close_lists()
            level = min(len(heading.group(1)), 6)
            text = heading.group(2).strip()
            out.append(f'<h{level} id="{heading_id(text)}">{inline_markdown(text)}</h{level}>')
            continue
        item = re.match(r"^(\s*)[-*]\s+(.+)$", line)
        if item:
            close_paragraph()
            level = len(item.group(1)) // 2 + 1
            while len(list_stack) < level:
                out.append("<ul>")
                list_stack.append(level)
            close_lists(level)
            out.append(f"<li>{inline_markdown(item.group(2))}</li>")
            continue
        paragraph.append(line.strip())

    close_paragraph()
    close_lists()
    if in_code:
        out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(out)


def xhtml_document(title: str, body: str) -> str:
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
{body}
</body>
</html>
'''


def nav_doc(items: list[tuple[str, str]]) -> str:
    entries = "\n".join(
        f'      <li><a href="{html.escape(href, quote=True)}">{html.escape(label)}</a></li>'
        for label, href in items
    )
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head>
  <title>Table of Contents</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Table of Contents</h1>
    <ol>
{entries}
    </ol>
  </nav>
</body>
</html>
'''


def content_opf(book_title: str, files: list[str], spine: list[str], identifier: str) -> str:
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="style.css" media-type="text/css"/>',
    ]
    for index, href in enumerate(files):
        manifest.append(f'<item id="item{index}" href="{href}" media-type="application/xhtml+xml"/>')
    spine_items = "\n".join(f'    <itemref idref="{item}"/>' for item in spine)
    manifest_xml = "\n    ".join(manifest)
    return f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:{identifier}</dc:identifier>
    <dc:title>{html.escape(book_title)}</dc:title>
    <dc:creator>{html.escape(AUTHOR)}</dc:creator>
    <dc:language>en</dc:language>
    <meta property="dcterms:modified">{modified}</meta>
  </metadata>
  <manifest>
    {manifest_xml}
  </manifest>
  <spine>
{spine_items}
  </spine>
</package>
'''


def assert_xml_documents_are_parseable(docs: dict[str, str], nav: str, opf: str) -> None:
    for name, content in {"nav.xhtml": nav, "content.opf": opf, **docs}.items():
        try:
            ElementTree.fromstring(content.encode("utf-8"))
        except ElementTree.ParseError as exc:
            raise SystemExit(f"{name}: invalid XML: {exc}") from exc


def write_epub(out: Path, book_title: str, details: list[Path], titles: dict[Path, str], readme_body: str) -> None:
    docs: dict[str, str] = {}
    toc: list[tuple[str, str]] = []
    docs["readme.xhtml"] = xhtml_document(book_title, readme_body)
    toc.append(("Overview and Index", "readme.xhtml"))

    for detail in details:
        title = titles.get(detail) or page_title(detail)
        href = f"details/{detail.stem}.xhtml"
        detail_body = markdown_to_body(detail.read_text(encoding="utf-8"), title=title)
        docs[href] = xhtml_document(title, detail_body)
        toc.append((title, href))

    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()

    file_order = list(docs)
    spine = [f"item{idx}" for idx in range(len(file_order))]
    identifier = str(uuid.uuid5(uuid.NAMESPACE_URL, f"file://{out}"))

    nav = nav_doc(toc)
    opf = content_opf(book_title, file_order, spine, identifier)
    assert_xml_documents_are_parseable(docs, nav, opf)

    with zipfile.ZipFile(out, "w") as epub:
        epub.writestr(zipfile.ZipInfo("mimetype", date_time=(1980, 1, 1, 0, 0, 0)), "application/epub+zip", zipfile.ZIP_STORED)
        epub.writestr("META-INF/container.xml", '''<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
''')
        epub.writestr("OEBPS/style.css", CSS)
        epub.writestr("OEBPS/nav.xhtml", nav)
        for href, content in docs.items():
            epub.writestr(f"OEBPS/{href}", content)
        epub.writestr("OEBPS/content.opf", opf)

    print(f"Wrote {out.relative_to(ROOT)} with {len(details)} detail pages.")


def volume_markdown(book_title: str, sections: list[tuple[str, list[Path]]], titles: dict[Path, str]) -> str:
    lines = [
        f"# {book_title}",
        "",
        f"Repository: [{REPO_URL}]({REPO_URL})",
        "",
        "Part of the Awesome Time Tracking Kindle edition.",
        "",
        "## Contents",
        "",
    ]
    for section_title, details in sections:
        lines.extend([f"## {section_title}", ""])
        for detail in details:
            title = titles.get(detail) or page_title(detail)
            lines.append(f"- [{title}](details/{detail.name})")
        lines.append("")
    return "\n".join(lines)


def readme_with_repo_link(readme: str) -> str:
    first_newline = readme.find("\n")
    if first_newline == -1:
        return f"{readme}\n\nRepository: [{REPO_URL}]({REPO_URL})\n"
    return f"{readme[:first_newline]}\n\nRepository: [{REPO_URL}]({REPO_URL})\n{readme[first_newline:]}"


def main() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    details, titles = discover_detail_order(readme)

    write_epub(OUT, TITLE, details, titles, markdown_to_body(readme_with_repo_link(readme)))

    sections_by_volume = split_sections_by_volume(readme, details)
    by_volume = {
        slug: [path for _section, paths in section_list for path in paths]
        for slug, section_list in sections_by_volume.items()
    }
    split_dir = ROOT / "dist" / "split"
    for slug, book_title, _keywords in VOLUMES:
        volume_details = by_volume[slug]
        write_epub(
            split_dir / epub_filename(book_title),
            book_title,
            volume_details,
            titles,
            markdown_to_body(volume_markdown(book_title, sections_by_volume[slug], titles)),
        )


if __name__ == "__main__":
    mimetypes.add_type("application/xhtml+xml", ".xhtml")
    main()
