"""SingleLanguageUnitNames AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class SingleLanguageUnitNames(ARObject):
    """AUTOSAR SingleLanguageUnitNames."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SingleLanguageUnitNames."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SingleLanguageUnitNames to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SingleLanguageUnitNames":
        """Create SingleLanguageUnitNames from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SingleLanguageUnitNames instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SingleLanguageUnitNames since parent returns ARObject
        return cast("SingleLanguageUnitNames", obj)


class SingleLanguageUnitNamesBuilder:
    """Builder for SingleLanguageUnitNames."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SingleLanguageUnitNames = SingleLanguageUnitNames()

    def build(self) -> SingleLanguageUnitNames:
        """Build and return SingleLanguageUnitNames object.

        Returns:
            SingleLanguageUnitNames instance
        """
        # TODO: Add validation
        return self._obj
