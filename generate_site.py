#!/usr/bin/env python3
import os
import pathlib, shutil, datetime
import markdown, frontmatter
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = pathlib.Path(__file__).parent
SRC_POSTS = ROOT / "posts"
SRC_PAGES = ROOT / "pages"

DST_SITE  = ROOT / "docs"
TEMPLATES = ROOT / "templates"


env = Environment(
    loader=FileSystemLoader(TEMPLATES),
    autoescape=select_autoescape()
)
md = markdown.Markdown(extensions=["fenced_code", "codehilite", "tables", "mdx_math"],
                       extension_configs={
        "mdx_math": {
            "enable_dollar_delimiter": True,
        }
    })

def render_page(page_name: str):
    page = frontmatter.load(SRC_PAGES / f"{page_name}.md")
    html = md.convert(page.content)
    tpl = env.get_template("page.html")
    (DST_SITE / f"{page_name}.html").write_text(
        tpl.render(
            page={"title": page["title"], "html": html},
            title=page['title'], content=html)
    )

to_delete_from_slug = ['?', ':', ',', '.', '!', "'"]
def render_posts():
    post_tpl = env.get_template("post.html")
    index_items = []
    for md_path in sorted(SRC_POSTS.glob("*.md"), reverse=True):
        post = frontmatter.load(md_path)
        post_html = md.convert(post.content)
        post_date = post.get("date").strftime("%Y-%m-%d")
        subtitle = post.get("subtitle", "")
        title = post["title"]
        if len(subtitle):
            title += f": {subtitle}" 
        slug = post['title'].lower().replace(' ', '-')
        for c in to_delete_from_slug:
            slug = slug.replace(c, '')
        out_file = DST_SITE / f"{slug}.html"
        out_file.write_text(
            post_tpl.render(
                post={"title": post["title"], "date": post_date, "html": post_html, "subtitle": subtitle},
                description=post.get("description", None),
                title=title
            )
        )
        index_items.append({"title": post["title"], "slug": slug, "date": post_date,
                            "draft": post.get('draft', False), "subtitle": subtitle})
        md.reset()  # important when re-using the converter
    return index_items

def render_index(items):
    # newest first
    items = sorted(items, key=lambda x: x["date"], reverse=True)
    items = list(filter(lambda x: not x.get('draft', False), items))
    tpl   = env.get_template("base.html")

    # helper → "SEPTEMBER 2022"
    def pretty(d):  
        return datetime.datetime.strptime(d, "%Y-%m-%d").strftime("%B %Y").upper()

    about_link = '''
<div class="top-links">
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
</div>
    '''.strip()


    li_elements = []
    for i in items:
        title = i["title"]
        if i.get("subtitle", ""):
            title += f': {i["subtitle"]}'
        li_elements.append(
            f'  <li class="post-item">'
            f'    <div class="post-meta">{pretty(i["date"])}</div>'
            f'    <h2 class="post-title"><a href="{i["slug"]}.html">{title}</a></h2>'
            f'  </li>'
        )
    
    html_list = about_link + "\n<ul class=\"post-list\">\n" + "\n".join(li_elements)+ "\n</ul>"

    (DST_SITE / "index.html").write_text(
        tpl.render(title="abranti's website", content=html_list)
    )

def copy_static():
    dst_static = DST_SITE / "static"
    if dst_static.exists():
        shutil.rmtree(dst_static)
    shutil.copytree(ROOT / "static", dst_static, dirs_exist_ok=True)

if __name__ == "__main__":
    DST_SITE.mkdir(exist_ok=True)
    copy_static()
    render_page('about')
    render_page('contact')
    items = render_posts()
    render_index(items)
    (DST_SITE / '.nojekyll').write_text('')
    (DST_SITE / 'CNAME').write_text('abranti.com')
    print("Site rendered →", DST_SITE)