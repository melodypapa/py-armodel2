"""PlcaProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class PlcaProps(ARObject):
    """AUTOSAR PlcaProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("plca_local_node", None, True, False, None),  # plcaLocalNode
        ("plca_max_burst", None, True, False, None),  # plcaMaxBurst
    ]

    def __init__(self) -> None:
        """Initialize PlcaProps."""
        super().__init__()
        self.plca_local_node: Optional[PositiveInteger] = None
        self.plca_max_burst: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PlcaProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PlcaProps":
        """Create PlcaProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PlcaProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PlcaProps since parent returns ARObject
        return cast("PlcaProps", obj)


class PlcaPropsBuilder:
    """Builder for PlcaProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PlcaProps = PlcaProps()

    def build(self) -> PlcaProps:
        """Build and return PlcaProps object.

        Returns:
            PlcaProps instance
        """
        # TODO: Add validation
        return self._obj
