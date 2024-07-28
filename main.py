from flet import *

def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    _c = Container(
        width=200,
        height=500,
        bgcolor='black'
    )

    page.add(_c)

if __name__ == '__main__':
    app(target=main, assets_dir='assets')