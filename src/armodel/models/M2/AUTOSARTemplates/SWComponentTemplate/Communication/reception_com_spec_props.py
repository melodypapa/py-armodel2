"""ReceptionComSpecProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class ReceptionComSpecProps(ARObject):
    """AUTOSAR ReceptionComSpecProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_update", None, True, False, None),  # dataUpdate
        ("timeout", None, True, False, None),  # timeout
    ]

    def __init__(self) -> None:
        """Initialize ReceptionComSpecProps."""
        super().__init__()
        self.data_update: Optional[TimeValue] = None
        self.timeout: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ReceptionComSpecProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReceptionComSpecProps":
        """Create ReceptionComSpecProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ReceptionComSpecProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ReceptionComSpecProps since parent returns ARObject
        return cast("ReceptionComSpecProps", obj)


class ReceptionComSpecPropsBuilder:
    """Builder for ReceptionComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceptionComSpecProps = ReceptionComSpecProps()

    def build(self) -> ReceptionComSpecProps:
        """Build and return ReceptionComSpecProps object.

        Returns:
            ReceptionComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
