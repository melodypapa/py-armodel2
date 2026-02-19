"""HwAttributeLiteralDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class HwAttributeLiteralDef(Identifiable):
    """AUTOSAR HwAttributeLiteralDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize HwAttributeLiteralDef."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwAttributeLiteralDef":
        """Deserialize XML element to HwAttributeLiteralDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwAttributeLiteralDef object
        """
        # Delegate to parent class to handle inherited attributes
        return super(HwAttributeLiteralDef, cls).deserialize(element)



class HwAttributeLiteralDefBuilder:
    """Builder for HwAttributeLiteralDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwAttributeLiteralDef = HwAttributeLiteralDef()

    def build(self) -> HwAttributeLiteralDef:
        """Build and return HwAttributeLiteralDef object.

        Returns:
            HwAttributeLiteralDef instance
        """
        # TODO: Add validation
        return self._obj
