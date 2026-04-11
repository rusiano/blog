from pathlib import Path

def on_post_build(config):
    output_dir = Path(config["site_dir"])
    (output_dir / "CNAME").write_text("blog.rusiano.xyz", encoding="utf-8")