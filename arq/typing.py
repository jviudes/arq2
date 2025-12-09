from collections.abc import Sequence
from datetime import timedelta
from typing import TYPE_CHECKING, Any, Literal, Protocol

__all__ = (
    'OptionType',
    'WeekdayOptionType',
    'WEEKDAYS',
    'SecondsTimedelta',
    'WorkerCoroutine',
    'StartupShutdown',
    'WorkerSettingsType',
)


if TYPE_CHECKING:
    from .cron import CronJob
    from .worker import Function

OptionType = None | set[int] | int
WEEKDAYS = 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun'
WeekdayOptionType = OptionType | Literal['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
SecondsTimedelta = int | float | timedelta


class WorkerCoroutine(Protocol):
    __qualname__: str

    async def __call__(self, ctx: dict[Any, Any], *args: Any, **kwargs: Any) -> Any:  # pragma: no cover
        pass


class StartupShutdown(Protocol):
    __qualname__: str

    async def __call__(self, ctx: dict[Any, Any]) -> Any:  # pragma: no cover
        pass


class WorkerSettingsBase(Protocol):
    functions: Sequence[WorkerCoroutine | 'Function']
    cron_jobs: Sequence['CronJob'] | None = None
    on_startup: StartupShutdown | None = None
    on_shutdown: StartupShutdown | None = None
    # and many more...


WorkerSettingsType = dict[str, Any] | type[WorkerSettingsBase]
