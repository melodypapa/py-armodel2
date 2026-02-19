"""MetaDataItem AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 98)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2037)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.text_value_specification import (
    TextValueSpecification,
)


class MetaDataItem(ARObject):
    """AUTOSAR MetaDataItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    length: Optional[PositiveInteger]
    meta_data_item: Optional[TextValueSpecification]
    def __init__(self) -> None:
        """Initialize MetaDataItem."""
        super().__init__()
        self.length: Optional[PositiveInteger] = None
        self.meta_data_item: Optional[TextValueSpecification] = None
    def serialize(self) -> ET.Element:
        """Serialize MetaDataItem to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize length
        if self.length is not None:
            serialized = ARObject._serialize_item(self.length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize meta_data_item
        if self.meta_data_item is not None:
            serialized = ARObject._serialize_item(self.meta_data_item, "TextValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("META-DATA-ITEM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MetaDataItem":
        """Deserialize XML element to MetaDataItem object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MetaDataItem object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse length
        child = ARObject._find_child_element(element, "LENGTH")
        if child is not None:
            length_value = child.text
            obj.length = length_value

        # Parse meta_data_item
        child = ARObject._find_child_element(element, "META-DATA-ITEM")
        if child is not None:
            meta_data_item_value = ARObject._deserialize_by_tag(child, "TextValueSpecification")
            obj.meta_data_item = meta_data_item_value

        return obj



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
