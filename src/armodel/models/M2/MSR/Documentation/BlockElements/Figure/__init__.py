"""Figure module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.Figure.area import (
        Area,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.Figure.graphic import (
        Graphic,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.Figure.map import (
        Map,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.Figure.ml_figure import (
        MlFigure,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.Figure.l_graphic import (
        LGraphic,
    )

from armodel.models.M2.MSR.Documentation.BlockElements.Figure.area_enum_nohref import (
    AreaEnumNohref,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.area_enum_shape import (
    AreaEnumShape,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.graphic_fit_enum import (
    GraphicFitEnum,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.graphic_notation_enum import (
    GraphicNotationEnum,
)

__all__ = [
    "Area",
    "AreaEnumNohref",
    "AreaEnumShape",
    "Graphic",
    "GraphicFitEnum",
    "GraphicNotationEnum",
    "LGraphic",
    "Map",
    "MlFigure",
]
