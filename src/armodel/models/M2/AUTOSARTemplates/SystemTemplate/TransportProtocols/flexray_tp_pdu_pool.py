"""FlexrayTpPduPool AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class FlexrayTpPduPool(Identifiable):
    """AUTOSAR FlexrayTpPduPool."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("n_pdus", None, False, True, NPdu),  # nPdus
    ]

    def __init__(self) -> None:
        """Initialize FlexrayTpPduPool."""
        super().__init__()
        self.n_pdus: list[NPdu] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayTpPduPool to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpPduPool":
        """Create FlexrayTpPduPool from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayTpPduPool instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayTpPduPool since parent returns ARObject
        return cast("FlexrayTpPduPool", obj)


class FlexrayTpPduPoolBuilder:
    """Builder for FlexrayTpPduPool."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpPduPool = FlexrayTpPduPool()

    def build(self) -> FlexrayTpPduPool:
        """Build and return FlexrayTpPduPool object.

        Returns:
            FlexrayTpPduPool instance
        """
        # TODO: Add validation
        return self._obj
