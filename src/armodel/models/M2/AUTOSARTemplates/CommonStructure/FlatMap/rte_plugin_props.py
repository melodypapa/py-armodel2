"""RtePluginProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)


class RtePluginProps(ARObject):
    """AUTOSAR RtePluginProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("associated", None, False, False, EcucContainerValue),  # associated
        ("associated_rte", None, False, False, EcucContainerValue),  # associatedRte
    ]

    def __init__(self) -> None:
        """Initialize RtePluginProps."""
        super().__init__()
        self.associated: Optional[EcucContainerValue] = None
        self.associated_rte: Optional[EcucContainerValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RtePluginProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RtePluginProps":
        """Create RtePluginProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RtePluginProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RtePluginProps since parent returns ARObject
        return cast("RtePluginProps", obj)


class RtePluginPropsBuilder:
    """Builder for RtePluginProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RtePluginProps = RtePluginProps()

    def build(self) -> RtePluginProps:
        """Build and return RtePluginProps object.

        Returns:
            RtePluginProps instance
        """
        # TODO: Add validation
        return self._obj
