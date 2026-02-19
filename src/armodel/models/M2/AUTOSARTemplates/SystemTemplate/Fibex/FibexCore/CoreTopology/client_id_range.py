"""ClientIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
)


class ClientIdRange(ARObject):
    """AUTOSAR ClientIdRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lower_limit: Optional[Limit]
    upper_limit: Optional[Limit]
    def __init__(self) -> None:
        """Initialize ClientIdRange."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.upper_limit: Optional[Limit] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientIdRange":
        """Deserialize XML element to ClientIdRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientIdRange object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lower_limit
        child = ARObject._find_child_element(element, "LOWER-LIMIT")
        if child is not None:
            lower_limit_value = child.text
            obj.lower_limit = lower_limit_value

        # Parse upper_limit
        child = ARObject._find_child_element(element, "UPPER-LIMIT")
        if child is not None:
            upper_limit_value = child.text
            obj.upper_limit = upper_limit_value

        return obj



class ClientIdRangeBuilder:
    """Builder for ClientIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientIdRange = ClientIdRange()

    def build(self) -> ClientIdRange:
        """Build and return ClientIdRange object.

        Returns:
            ClientIdRange instance
        """
        # TODO: Add validation
        return self._obj
