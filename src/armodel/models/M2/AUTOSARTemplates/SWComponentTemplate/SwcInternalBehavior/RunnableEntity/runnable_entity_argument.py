"""RunnableEntityArgument AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 536)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RunnableEntity.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)


class RunnableEntityArgument(ARObject):
    """AUTOSAR RunnableEntityArgument."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize RunnableEntityArgument."""
        super().__init__()
        self.symbol: Optional[CIdentifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntityArgument":
        """Deserialize XML element to RunnableEntityArgument object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RunnableEntityArgument object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = ARObject._deserialize_by_tag(child, "CIdentifier")
            obj.symbol = symbol_value

        return obj



class RunnableEntityArgumentBuilder:
    """Builder for RunnableEntityArgument."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntityArgument = RunnableEntityArgument()

    def build(self) -> RunnableEntityArgument:
        """Build and return RunnableEntityArgument object.

        Returns:
            RunnableEntityArgument instance
        """
        # TODO: Add validation
        return self._obj
