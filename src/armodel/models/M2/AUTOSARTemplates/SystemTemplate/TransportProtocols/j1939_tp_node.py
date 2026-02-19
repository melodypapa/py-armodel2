"""J1939TpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 626)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class J1939TpNode(Identifiable):
    """AUTOSAR J1939TpNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connector: Optional[Any]
    tp_address: Optional[TpAddress]
    def __init__(self) -> None:
        """Initialize J1939TpNode."""
        super().__init__()
        self.connector: Optional[Any] = None
        self.tp_address: Optional[TpAddress] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpNode":
        """Deserialize XML element to J1939TpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpNode object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse connector
        child = ARObject._find_child_element(element, "CONNECTOR")
        if child is not None:
            connector_value = child.text
            obj.connector = connector_value

        # Parse tp_address
        child = ARObject._find_child_element(element, "TP-ADDRESS")
        if child is not None:
            tp_address_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.tp_address = tp_address_value

        return obj



class J1939TpNodeBuilder:
    """Builder for J1939TpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpNode = J1939TpNode()

    def build(self) -> J1939TpNode:
        """Build and return J1939TpNode object.

        Returns:
            J1939TpNode instance
        """
        # TODO: Add validation
        return self._obj
