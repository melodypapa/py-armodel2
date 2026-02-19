"""MetaDataItemSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 99)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2037)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize data_element_refs (list to container "DATA-ELEMENTS")
        if self.data_element_refs:
            wrapper = ET.Element("DATA-ELEMENTS")
            for item in self.data_element_refs:
                serialized = ARObject._serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize meta_data_items (list to container "META-DATA-ITEMS")
        if self.meta_data_items:
            wrapper = ET.Element("META-DATA-ITEMS")
            for item in self.meta_data_items:
                serialized = ARObject._serialize_item(item, "MetaDataItem")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_element_refs (list from container "DATA-ELEMENTS")
        obj.data_element_refs = []
        container = ARObject._find_child_element(element, "DATA-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_element_refs.append(child_value)

        # Parse meta_data_items (list from container "META-DATA-ITEMS")
        obj.meta_data_items = []
        container = ARObject._find_child_element(element, "META-DATA-ITEMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
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
