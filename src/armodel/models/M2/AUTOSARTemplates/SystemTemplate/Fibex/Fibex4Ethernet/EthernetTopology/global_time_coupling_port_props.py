"""GlobalTimeCouplingPortProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class GlobalTimeCouplingPortProps(ARObject):
    """AUTOSAR GlobalTimeCouplingPortProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("propagation", None, True, False, None),  # propagation
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeCouplingPortProps."""
        super().__init__()
        self.propagation: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeCouplingPortProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCouplingPortProps":
        """Create GlobalTimeCouplingPortProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeCouplingPortProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeCouplingPortProps since parent returns ARObject
        return cast("GlobalTimeCouplingPortProps", obj)


class GlobalTimeCouplingPortPropsBuilder:
    """Builder for GlobalTimeCouplingPortProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCouplingPortProps = GlobalTimeCouplingPortProps()

    def build(self) -> GlobalTimeCouplingPortProps:
        """Build and return GlobalTimeCouplingPortProps object.

        Returns:
            GlobalTimeCouplingPortProps instance
        """
        # TODO: Add validation
        return self._obj
