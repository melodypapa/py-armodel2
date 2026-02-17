"""AbstractStructure module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_instance_ref import (
        AtpInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_classifier import (
        AtpClassifier,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
        AtpFeature,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_prototype import (
        AtpPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_structure_element import (
        AtpStructureElement,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_type import (
        AtpType,
    )

__all__ = [
    "AtpClassifier",
    "AtpFeature",
    "AtpInstanceRef",
    "AtpPrototype",
    "AtpStructureElement",
    "AtpType",
]
