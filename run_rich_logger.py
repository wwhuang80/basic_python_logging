import sys
import logging
import argparse
from rich.logging import RichHandler


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="CLI logging example")
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="outputs debug level log messages to stdout",
    )
    args = parser.parse_args()
    return args


def set_logger(debug=False) -> logging.Logger:
    FORMAT = "%(module)s %(asctime)s: %(message)s"
    lvl = logging.DEBUG if debug else logging.INFO
    # --- set the handlers --- #
    rich_stdout_handler = RichHandler(level=logging.INFO, console=sys.stdout)
    rich_stdout_handler.addFilter(lambda record: record.levelname == logging.INFO)

    debug_handler = logging.StreamHandler(sys.stderr)
    debug_handler.addFilter(lambda record: record.levelname == logging.DEBUG)

    # using the root logger
    logging.basicConfig(
        level=lvl, format=FORMAT, handlers=[RichHandler(), rich_stdout_handler]
    )
    if debug:
        logging.getLogger().addHandler(debug_handler)


def main():
    args = get_args()
    set_logger(args.debug)
    logger = logging.getLogger()
    logger.info("this is an info log record")
    logger.debug("this is a debug message")


if __name__ == "__main__":
    sys.exit(main())
