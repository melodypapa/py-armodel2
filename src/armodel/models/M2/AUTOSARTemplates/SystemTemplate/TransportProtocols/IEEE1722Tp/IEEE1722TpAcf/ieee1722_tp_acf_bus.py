"""IEEE1722TpAcfBus AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)


class IEEE1722TpAcfBus(Identifiable):
    """AUTOSAR IEEE1722TpAcfBus."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("acf_parts", None, False, True, IEEE1722TpAcfBusPart),  # acfParts
        ("bus_id", None, True, False, None),  # busId
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfBus."""
        super().__init__()
        self.acf_parts: list[IEEE1722TpAcfBusPart] = []
        self.bus_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpAcfBus to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfBus":
        """Create IEEE1722TpAcfBus from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpAcfBus instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpAcfBus since parent returns ARObject
        return cast("IEEE1722TpAcfBus", obj)


class IEEE1722TpAcfBusBuilder:
    """Builder for IEEE1722TpAcfBus."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfBus = IEEE1722TpAcfBus()

    def build(self) -> IEEE1722TpAcfBus:
        """Build and return IEEE1722TpAcfBus object.

        Returns:
            IEEE1722TpAcfBus instance
        """
        # TODO: Add validation
        return self._obj
