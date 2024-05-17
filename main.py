import scraper
import bot


def main() -> None:
    price = scraper.get_price()
    bot.send_message(price)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped!")
