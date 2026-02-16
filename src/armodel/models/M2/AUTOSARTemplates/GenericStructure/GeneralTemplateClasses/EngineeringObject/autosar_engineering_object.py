"""AutosarEngineeringObject AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)


class AutosarEngineeringObject(EngineeringObject):
    """AUTOSAR AutosarEngineeringObject."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize AutosarEngineeringObject."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AutosarEngineeringObject to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarEngineeringObject":
        """Create AutosarEngineeringObject from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AutosarEngineeringObject instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AutosarEngineeringObject since parent returns ARObject
        return cast("AutosarEngineeringObject", obj)


class AutosarEngineeringObjectBuilder:
    """Builder for AutosarEngineeringObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarEngineeringObject = AutosarEngineeringObject()

    def build(self) -> AutosarEngineeringObject:
        """Build and return AutosarEngineeringObject object.

        Returns:
            AutosarEngineeringObject instance
        """
        # TODO: Add validation
        return self._obj
