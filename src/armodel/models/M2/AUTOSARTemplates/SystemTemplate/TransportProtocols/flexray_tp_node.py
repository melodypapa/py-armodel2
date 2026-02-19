"""FlexrayTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 596)

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


class FlexrayTpNode(Identifiable):
    """AUTOSAR FlexrayTpNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connectors: list[Any]
    tp_address: Optional[TpAddress]
    def __init__(self) -> None:
        """Initialize FlexrayTpNode."""
        super().__init__()
        self.connectors: list[Any] = []
        self.tp_address: Optional[TpAddress] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpNode":
        """Deserialize XML element to FlexrayTpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpNode object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse connectors (list)
        obj.connectors = []
        for child in ARObject._find_all_child_elements(element, "CONNECTORS"):
            connectors_value = child.text
            obj.connectors.append(connectors_value)

        # Parse tp_address
        child = ARObject._find_child_element(element, "TP-ADDRESS")
        if child is not None:
            tp_address_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.tp_address = tp_address_value

        return obj



class FlexrayTpNodeBuilder:
    """Builder for FlexrayTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpNode = FlexrayTpNode()

    def build(self) -> FlexrayTpNode:
        """Build and return FlexrayTpNode object.

        Returns:
            FlexrayTpNode instance
        """
        # TODO: Add validation
        return self._obj
