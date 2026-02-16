"""IdsDesign AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)


class IdsDesign(ARElement):
    """AUTOSAR IdsDesign."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("elements", None, False, True, IdsCommonElement),  # elements
    ]

    def __init__(self) -> None:
        """Initialize IdsDesign."""
        super().__init__()
        self.elements: list[IdsCommonElement] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IdsDesign to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsDesign":
        """Create IdsDesign from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IdsDesign instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IdsDesign since parent returns ARObject
        return cast("IdsDesign", obj)


class IdsDesignBuilder:
    """Builder for IdsDesign."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsDesign = IdsDesign()

    def build(self) -> IdsDesign:
        """Build and return IdsDesign object.

        Returns:
            IdsDesign instance
        """
        # TODO: Add validation
        return self._obj
