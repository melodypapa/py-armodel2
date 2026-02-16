"""MetaDataItemSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.meta_data_item import (
    MetaDataItem,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class MetaDataItemSet(ARObject):
    """AUTOSAR MetaDataItemSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_elements", None, False, True, VariableDataPrototype),  # dataElements
        ("meta_data_items", None, False, True, MetaDataItem),  # metaDataItems
    ]

    def __init__(self) -> None:
        """Initialize MetaDataItemSet."""
        super().__init__()
        self.data_elements: list[VariableDataPrototype] = []
        self.meta_data_items: list[MetaDataItem] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MetaDataItemSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MetaDataItemSet":
        """Create MetaDataItemSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MetaDataItemSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MetaDataItemSet since parent returns ARObject
        return cast("MetaDataItemSet", obj)


class MetaDataItemSetBuilder:
    """Builder for MetaDataItemSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MetaDataItemSet = MetaDataItemSet()

    def build(self) -> MetaDataItemSet:
        """Build and return MetaDataItemSet object.

        Returns:
            MetaDataItemSet instance
        """
        # TODO: Add validation
        return self._obj
