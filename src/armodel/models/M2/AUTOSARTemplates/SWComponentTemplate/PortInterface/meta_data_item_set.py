"""MetaDataItemSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 99)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2037)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.meta_data_item import (
    MetaDataItem,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class MetaDataItemSet(ARObject):
    """AUTOSAR MetaDataItemSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element_refs: list[ARRef]
    meta_data_items: list[MetaDataItem]
    def __init__(self) -> None:
        """Initialize MetaDataItemSet."""
        super().__init__()
        self.data_element_refs: list[ARRef] = []
        self.meta_data_items: list[MetaDataItem] = []

    def serialize(self) -> ET.Element:
        """Serialize MetaDataItemSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MetaDataItemSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_element_refs (list to container "DATA-ELEMENT-REFS")
        if self.data_element_refs:
            wrapper = ET.Element("DATA-ELEMENT-REFS")
            for item in self.data_element_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("DATA-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize meta_data_items (list to container "META-DATA-ITEMS")
        if self.meta_data_items:
            wrapper = ET.Element("META-DATA-ITEMS")
            for item in self.meta_data_items:
                serialized = SerializationHelper.serialize_item(item, "MetaDataItem")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MetaDataItemSet":
        """Deserialize XML element to MetaDataItemSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MetaDataItemSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MetaDataItemSet, cls).deserialize(element)

        # Parse data_element_refs (list from container "DATA-ELEMENT-REFS")
        obj.data_element_refs = []
        container = SerializationHelper.find_child_element(element, "DATA-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_element_refs.append(child_value)

        # Parse meta_data_items (list from container "META-DATA-ITEMS")
        obj.meta_data_items = []
        container = SerializationHelper.find_child_element(element, "META-DATA-ITEMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.meta_data_items.append(child_value)

        return obj



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
