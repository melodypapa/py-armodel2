"""FMAttributeValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)


class FMAttributeValue(ARObject):
    """AUTOSAR FMAttributeValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("definition", None, False, False, FMAttributeDef),  # definition
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize FMAttributeValue."""
        super().__init__()
        self.definition: Optional[FMAttributeDef] = None
        self.value: Optional[Numerical] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMAttributeValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMAttributeValue":
        """Create FMAttributeValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMAttributeValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMAttributeValue since parent returns ARObject
        return cast("FMAttributeValue", obj)


class FMAttributeValueBuilder:
    """Builder for FMAttributeValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMAttributeValue = FMAttributeValue()

    def build(self) -> FMAttributeValue:
        """Build and return FMAttributeValue object.

        Returns:
            FMAttributeValue instance
        """
        # TODO: Add validation
        return self._obj
