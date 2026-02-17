"""DataPrototypeReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DataPrototypeReference(ARObject):
    """AUTOSAR DataPrototypeReference."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DataPrototypeReference."""
        super().__init__()
        self.tag_id: Optional[PositiveInteger] = None


class DataPrototypeReferenceBuilder:
    """Builder for DataPrototypeReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeReference = DataPrototypeReference()

    def build(self) -> DataPrototypeReference:
        """Build and return DataPrototypeReference object.

        Returns:
            DataPrototypeReference instance
        """
        # TODO: Add validation
        return self._obj
