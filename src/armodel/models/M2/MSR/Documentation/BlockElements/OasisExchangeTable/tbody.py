"""Tbody AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 335)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    ValignEnum,
)


class Tbody(ARObject):
    """AUTOSAR Tbody."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    valign: Optional[ValignEnum]
    def __init__(self) -> None:
        """Initialize Tbody."""
        super().__init__()
        self.valign: Optional[ValignEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Tbody":
        """Deserialize XML element to Tbody object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Tbody object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse valign
        child = ARObject._find_child_element(element, "VALIGN")
        if child is not None:
            valign_value = ValignEnum.deserialize(child)
            obj.valign = valign_value

        return obj



class TbodyBuilder:
    """Builder for Tbody."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Tbody = Tbody()

    def build(self) -> Tbody:
        """Build and return Tbody object.

        Returns:
            Tbody instance
        """
        # TODO: Add validation
        return self._obj
