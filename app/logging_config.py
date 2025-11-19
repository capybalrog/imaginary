import logging
import sys

from loguru import logger


class InterceptHandler(logging.Handler):
    """
    Перехватывает логирование и передает их в loguru.
    """

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logging():
    """
    Настраивает логгер для всего приложения.
    """
    logger.remove()

    logger.add(
        sys.stderr,
        level="DEBUG",
        format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        colorize=True,
    )

    logger.add(
        "logs/app.log",
        level="INFO",
        rotation="10 MB",
        retention="1 month",
        compression="zip",
        serialize=False,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    )

    logger.info("Конфигурация логирования завершена.")
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
    logger.info("Стандартный logging перехвачен.")
