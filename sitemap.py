
from flask import Blueprint, Response
from datetime import datetime

sitemap_bp = Blueprint('sitemap', __name__)

@sitemap_bp.route('/sitemap.xml', methods=['GET'])
def sitemap():
    pages = [
        {'loc': '/', 'lastmod': datetime.now().date()},
        {'loc': '/about', 'lastmod': datetime.now().date()},
        {'loc': '/portfolio', 'lastmod': datetime.now().date()},
        {'loc': '/blog', 'lastmod': datetime.now().date()},
        {'loc': '/depoimentos', 'lastmod': datetime.now().date()},
        {'loc': '/contacts', 'lastmod': datetime.now().date()},
    ]

    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for page in pages:
        sitemap_xml += '  <url>\n'
        sitemap_xml += f'    <loc>https://twonz-technology.onrender.com{page["loc"]}</loc>\n'
        sitemap_xml += f'    <lastmod>{page["lastmod"]}</lastmod>\n'
        sitemap_xml += '    <changefreq>monthly</changefreq>\n'
        sitemap_xml += '    <priority>0.8</priority>\n'
        sitemap_xml += '  </url>\n'

    sitemap_xml += '</urlset>'

    return Response(sitemap_xml, mimetype='application/xml')
