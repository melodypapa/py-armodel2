"""CanTpNode AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)


class CanTpNode(Identifiable):
    """AUTOSAR CanTpNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("connector", None, False, False, any (Communication)),  # connector
        ("max_fc_wait", None, True, False, None),  # maxFcWait
        ("st_min", None, True, False, None),  # stMin
        ("timeout_ar", None, True, False, None),  # timeoutAr
        ("timeout_as", None, True, False, None),  # timeoutAs
        ("tp_address", None, False, False, CanTpAddress),  # tpAddress
    ]

    def __init__(self) -> None:
        """Initialize CanTpNode."""
        super().__init__()
        self.connector: Optional[Any] = None
        self.max_fc_wait: Optional[Integer] = None
        self.st_min: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.tp_address: Optional[CanTpAddress] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanTpNode to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpNode":
        """Create CanTpNode from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanTpNode instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanTpNode since parent returns ARObject
        return cast("CanTpNode", obj)


class CanTpNodeBuilder:
    """Builder for CanTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpNode = CanTpNode()

    def build(self) -> CanTpNode:
        """Build and return CanTpNode object.

        Returns:
            CanTpNode instance
        """
        # TODO: Add validation
        return self._obj
