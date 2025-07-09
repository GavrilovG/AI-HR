import functools
import itertools
from collections.abc import Iterable
from typing import Any

import aioinject
from pydantic_settings import BaseSettings

from settings import (
    DatabaseSettings,
    get_settings,
)

from .modules import (
    db,
)

PROVIDERS: Iterable[Iterable[aioinject.Provider[Any]]] = [
    db.providers,
]
SETTINGS = (DatabaseSettings)


def _register_settings(
    container: aioinject.Container,
    settings_classes: Iterable[type[BaseSettings]],
) -> None:
    for settings_cls in settings_classes:
        factory = functools.partial(get_settings, settings_cls)
        container.register(aioinject.Singleton(factory, type_=settings_cls))


@functools.cache
def get_container() -> aioinject.Container:
    container = aioinject.Container()

    _register_settings(container, settings_classes=SETTINGS)

    for provider in itertools.chain.from_iterable(PROVIDERS):
        container.register(provider)

    return container
