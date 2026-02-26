"""ElementCollection module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collection import (
        Collection,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collectable_element import (
        CollectableElement,
    )

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.auto_collect_enum import (
    AutoCollectEnum,
)

__all__ = [
    "AutoCollectEnum",
    "CollectableElement",
    "Collection",
]
