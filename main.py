from flask import Flask, jsonify
import requests

app = Flask(__name__)


def get_site_content(url):
    data = {"url": url}
    headers = {
        "authority": "www.siteexplainer.com",
        "origin": "www.siteexplainer.com",
        "referer": "www.siteexplainer.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
    }

    response = requests.post(
        "https://www.siteexplainer.com/api/fetchWebsiteContent",
        headers=headers,
        json=data,
        stream=False,
    ).text
    return response[:8000]


def get_summary(content):
    data = {"prompt": content}
    headers = {
        "authority": "wtfdoesthiscompanydo.vercel.app",
        "origin": "wtfdoesthiscompanydo.vercel.app",
        "referer": "wtfdoesthiscompanydo.vercel.app",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
    }

    response = requests.post(
        "https://wtfdoesthiscompanydo.vercel.app/api/e2uhqiueq932yh",
        headers=headers,
        json=data,
        stream=False,
    )
    return response.text


@app.route("/")
def home():
    return "Hello human"


@app.route("/fmhy_desc_from_url/<path:url>")
def get_desc_from_url(url):
    site_content = get_site_content(url)
    if site_content == "Bad Response":
        return jsonify(
            {"ok": False, "url": url, "description": "", "site_content": site_content}
        )
    summary = get_summary(site_content)
    return jsonify(
        {"ok": True, "url": url, "description": summary, "site_content": site_content}
    )


@app.route("/fmhy_desc_from_url/")
def get_desc_from_url_edgecase():
    return jsonify({"ok": False, "error": "no url provided"})


if __name__ == "__main__":
    app.run(port=5300, debug=True)

