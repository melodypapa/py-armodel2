"""DataFormatElementScope AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_scope import (
    SpecElementScope,
)


class DataFormatElementScope(SpecElementScope):
    """AUTOSAR DataFormatElementScope."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DataFormatElementScope."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataFormatElementScope to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFormatElementScope":
        """Create DataFormatElementScope from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataFormatElementScope instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataFormatElementScope since parent returns ARObject
        return cast("DataFormatElementScope", obj)


class DataFormatElementScopeBuilder:
    """Builder for DataFormatElementScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataFormatElementScope = DataFormatElementScope()

    def build(self) -> DataFormatElementScope:
        """Build and return DataFormatElementScope object.

        Returns:
            DataFormatElementScope instance
        """
        # TODO: Add validation
        return self._obj
