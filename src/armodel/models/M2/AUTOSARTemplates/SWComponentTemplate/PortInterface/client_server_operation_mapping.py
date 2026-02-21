"""ClientServerOperationMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
    DataPrototypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)


class ClientServerOperationMapping(ARObject):
    """AUTOSAR ClientServerOperationMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    argument_refs: list[ARRef]
    first_operation_ref: Optional[ARRef]
    first_to_second_ref: Optional[ARRef]
    second_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ClientServerOperationMapping."""
        super().__init__()
        self.argument_refs: list[ARRef] = []
        self.first_operation_ref: Optional[ARRef] = None
        self.first_to_second_ref: Optional[ARRef] = None
        self.second_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerOperationMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerOperationMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize argument_refs (list to container "ARGUMENT-REFS")
        if self.argument_refs:
            wrapper = ET.Element("ARGUMENT-REFS")
            for item in self.argument_refs:
                serialized = SerializationHelper.serialize_item(item, "DataPrototypeMapping")
                if serialized is not None:
                    child_elem = ET.Element("ARGUMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize first_operation_ref
        if self.first_operation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_operation_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-OPERATION-REF")
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

        # Serialize second_ref
        if self.second_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperationMapping":
        """Deserialize XML element to ClientServerOperationMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerOperationMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerOperationMapping, cls).deserialize(element)

        # Parse argument_refs (list from container "ARGUMENT-REFS")
        obj.argument_refs = []
        container = SerializationHelper.find_child_element(element, "ARGUMENT-REFS")
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
                    obj.argument_refs.append(child_value)

        # Parse first_operation_ref
        child = SerializationHelper.find_child_element(element, "FIRST-OPERATION-REF")
        if child is not None:
            first_operation_ref_value = ARRef.deserialize(child)
            obj.first_operation_ref = first_operation_ref_value

        # Parse first_to_second_ref
        child = SerializationHelper.find_child_element(element, "FIRST-TO-SECOND-REF")
        if child is not None:
            first_to_second_ref_value = ARRef.deserialize(child)
            obj.first_to_second_ref = first_to_second_ref_value

        # Parse second_ref
        child = SerializationHelper.find_child_element(element, "SECOND-REF")
        if child is not None:
            second_ref_value = ARRef.deserialize(child)
            obj.second_ref = second_ref_value

        return obj



class ClientServerOperationMappingBuilder:
    """Builder for ClientServerOperationMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperationMapping = ClientServerOperationMapping()

    def build(self) -> ClientServerOperationMapping:
        """Build and return ClientServerOperationMapping object.

        Returns:
            ClientServerOperationMapping instance
        """
        # TODO: Add validation
        return self._obj
