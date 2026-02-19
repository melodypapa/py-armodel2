"""TpAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 588)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class TpAddress(Identifiable):
    """AUTOSAR TpAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_address: Optional[Integer]
    def __init__(self) -> None:
        """Initialize TpAddress."""
        super().__init__()
        self.tp_address: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TpAddress":
        """Deserialize XML element to TpAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TpAddress object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tp_address
        child = ARObject._find_child_element(element, "TP-ADDRESS")
        if child is not None:
            tp_address_value = child.text
            obj.tp_address = tp_address_value

        return obj



class TpAddressBuilder:
    """Builder for TpAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpAddress = TpAddress()

    def build(self) -> TpAddress:
        """Build and return TpAddress object.

        Returns:
            TpAddress instance
        """
        # TODO: Add validation
        return self._obj
