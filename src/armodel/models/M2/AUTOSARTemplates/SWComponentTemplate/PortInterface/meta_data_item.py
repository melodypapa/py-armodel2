"""MetaDataItem AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.text_value_specification import (
    TextValueSpecification,
)


class MetaDataItem(ARObject):
    """AUTOSAR MetaDataItem."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("length", None, True, False, None),  # length
        ("meta_data_item", None, False, False, TextValueSpecification),  # metaDataItem
    ]

    def __init__(self) -> None:
        """Initialize MetaDataItem."""
        super().__init__()
        self.length: Optional[PositiveInteger] = None
        self.meta_data_item: Optional[TextValueSpecification] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MetaDataItem to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MetaDataItem":
        """Create MetaDataItem from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MetaDataItem instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MetaDataItem since parent returns ARObject
        return cast("MetaDataItem", obj)


class MetaDataItemBuilder:
    """Builder for MetaDataItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MetaDataItem = MetaDataItem()

    def build(self) -> MetaDataItem:
        """Build and return MetaDataItem object.

        Returns:
            MetaDataItem instance
        """
        # TODO: Add validation
        return self._obj
