"""DataFormatElementReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)


class DataFormatElementReference(SpecElementReference):
    """AUTOSAR DataFormatElementReference."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DataFormatElementReference."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataFormatElementReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFormatElementReference":
        """Create DataFormatElementReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataFormatElementReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataFormatElementReference since parent returns ARObject
        return cast("DataFormatElementReference", obj)


class DataFormatElementReferenceBuilder:
    """Builder for DataFormatElementReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataFormatElementReference = DataFormatElementReference()

    def build(self) -> DataFormatElementReference:
        """Build and return DataFormatElementReference object.

        Returns:
            DataFormatElementReference instance
        """
        # TODO: Add validation
        return self._obj
