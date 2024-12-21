import asyncio
import os
from playwright.async_api import async_playwright

async def html_to_png(input_html, output_png):
    input_html = os.path.abspath(input_html)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(f'file://{input_html}')

        # Nájde element podľa selektora a získa jeho rozmery
        element = await page.query_selector('body > div')  # Uprav podľa svojho selektora
        bounding_box = await element.bounding_box()

        # Nastaví viewport podľa rozmerov elementu
        await page.set_viewport_size({
            'width': int(bounding_box['width'] * 3),
            'height': int(bounding_box['height'] * 3)
        })

        # Uloží screenshot elementu
        await element.screenshot(path=output_png, scale="device")

        await browser.close()

def generate_image_from_html():
    input_html = "HTML/output.html"  # Relatívna cesta k súboru
    output_png = "output.png"

    asyncio.run(html_to_png(input_html, output_png))

    print(f"PNG obrázok bol úspešne vygenerovaný: {output_png}")

