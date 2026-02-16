"""LinTpNode AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class LinTpNode(Identifiable):
    """AUTOSAR LinTpNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("connector", None, False, False, any (Communication)),  # connector
        ("drop_not", None, True, False, None),  # dropNot
        ("max_number_of", None, True, False, None),  # maxNumberOf
        ("p2_max", None, True, False, None),  # p2Max
        ("p2_timing", None, True, False, None),  # p2Timing
        ("tp_address", None, False, False, TpAddress),  # tpAddress
    ]

    def __init__(self) -> None:
        """Initialize LinTpNode."""
        super().__init__()
        self.connector: Optional[Any] = None
        self.drop_not: Optional[Boolean] = None
        self.max_number_of: Optional[Integer] = None
        self.p2_max: Optional[TimeValue] = None
        self.p2_timing: Optional[TimeValue] = None
        self.tp_address: Optional[TpAddress] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinTpNode to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpNode":
        """Create LinTpNode from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinTpNode instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinTpNode since parent returns ARObject
        return cast("LinTpNode", obj)


class LinTpNodeBuilder:
    """Builder for LinTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinTpNode = LinTpNode()

    def build(self) -> LinTpNode:
        """Build and return LinTpNode object.

        Returns:
            LinTpNode instance
        """
        # TODO: Add validation
        return self._obj
