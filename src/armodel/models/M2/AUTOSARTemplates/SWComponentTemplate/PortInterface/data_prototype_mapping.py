"""DataPrototypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 125)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2014)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_mapping import (
    SubElementMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class DataPrototypeMapping(ARObject):
    """AUTOSAR DataPrototypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_data_ref: Optional[ARRef]
    first_to_second_ref: Optional[ARRef]
    second_data_ref: Optional[ARRef]
    second_to_first_ref: Optional[ARRef]
    sub_element_refs: list[ARRef]
    text_table_ref: ARRef
    def __init__(self) -> None:
        """Initialize DataPrototypeMapping."""
        super().__init__()
        self.first_data_ref: Optional[ARRef] = None
        self.first_to_second_ref: Optional[ARRef] = None
        self.second_data_ref: Optional[ARRef] = None
        self.second_to_first_ref: Optional[ARRef] = None
        self.sub_element_refs: list[ARRef] = []
        self.text_table_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_data_ref
        if self.first_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_data_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize first_to_second_ref
        if self.first_to_second_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_to_second_ref, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-TO-SECOND-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_data_ref
        if self.second_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_data_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_to_first_ref
        if self.second_to_first_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_to_first_ref, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-TO-FIRST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_element_refs (list to container "SUB-ELEMENT-REFS")
        if self.sub_element_refs:
            wrapper = ET.Element("SUB-ELEMENT-REFS")
            for item in self.sub_element_refs:
                serialized = SerializationHelper.serialize_item(item, "SubElementMapping")
                if serialized is not None:
                    child_elem = ET.Element("SUB-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize text_table_ref
        if self.text_table_ref is not None:
            serialized = SerializationHelper.serialize_item(self.text_table_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEXT-TABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeMapping":
        """Deserialize XML element to DataPrototypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeMapping, cls).deserialize(element)

        # Parse first_data_ref
        child = SerializationHelper.find_child_element(element, "FIRST-DATA-REF")
        if child is not None:
            first_data_ref_value = ARRef.deserialize(child)
            obj.first_data_ref = first_data_ref_value

        # Parse first_to_second_ref
        child = SerializationHelper.find_child_element(element, "FIRST-TO-SECOND-REF")
        if child is not None:
            first_to_second_ref_value = ARRef.deserialize(child)
            obj.first_to_second_ref = first_to_second_ref_value

        # Parse second_data_ref
        child = SerializationHelper.find_child_element(element, "SECOND-DATA-REF")
        if child is not None:
            second_data_ref_value = ARRef.deserialize(child)
            obj.second_data_ref = second_data_ref_value

        # Parse second_to_first_ref
        child = SerializationHelper.find_child_element(element, "SECOND-TO-FIRST-REF")
        if child is not None:
            second_to_first_ref_value = ARRef.deserialize(child)
            obj.second_to_first_ref = second_to_first_ref_value

        # Parse sub_element_refs (list from container "SUB-ELEMENT-REFS")
        obj.sub_element_refs = []
        container = SerializationHelper.find_child_element(element, "SUB-ELEMENT-REFS")
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
                    obj.sub_element_refs.append(child_value)

        # Parse text_table_ref
        child = SerializationHelper.find_child_element(element, "TEXT-TABLE-REF")
        if child is not None:
            text_table_ref_value = ARRef.deserialize(child)
            obj.text_table_ref = text_table_ref_value

        return obj



class DataPrototypeMappingBuilder:
    """Builder for DataPrototypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeMapping = DataPrototypeMapping()

    def build(self) -> DataPrototypeMapping:
        """Build and return DataPrototypeMapping object.

        Returns:
            DataPrototypeMapping instance
        """
        # TODO: Add validation
        return self._obj
