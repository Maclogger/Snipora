import asyncio
import os
from pyppeteer import launch

async def html_to_png(input_html, output_png):
    # Preveď relatívnu cestu na absolútnu
    input_html = os.path.abspath(input_html)

    # Spustenie prehliadača v režime headless
    browser = await launch(headless=True)
    page = await browser.newPage()

    # Načítanie HTML súboru
    await page.goto(f'file://{input_html}')

    # Získanie rozmerov elementu
    element = await page.querySelector('body > div')  # Uprav podľa svojho selektora
    bounding_box = await element.boundingBox()

    # Nastavenie viewportu na veľkosť elementu
    await page.setViewport({
        'width': int(bounding_box['width']),
        'height': int(bounding_box['height']),
        'deviceScaleFactor': 4
    })

    # Uloženie screenshotu len daného elementu
    await element.screenshot({'path': output_png})

    # Zavretie prehliadača
    await browser.close()


# Spustenie funkcie
if __name__ == "__main__":
    input_html = "HTML/output.html"  # Relatívna cesta k súboru
    output_png = "output.png"

    # Spustenie async funkcie
    asyncio.get_event_loop().run_until_complete(html_to_png(input_html, output_png))

    print(f"PNG obrázok bol úspešne vygenerovaný: {output_png}")
