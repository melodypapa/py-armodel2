"""ClientServerOperationMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    first_operation: Optional[ClientServerOperation]
    first_to_second: Optional[DataTransformation]
    second: Optional[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize ClientServerOperationMapping."""
        super().__init__()
        self.argument_refs: list[ARRef] = []
        self.first_operation: Optional[ClientServerOperation] = None
        self.first_to_second: Optional[DataTransformation] = None
        self.second: Optional[ClientServerOperation] = None
    def serialize(self) -> ET.Element:
        """Serialize ClientServerOperationMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize argument_refs (list to container "ARGUMENTS")
        if self.argument_refs:
            wrapper = ET.Element("ARGUMENTS")
            for item in self.argument_refs:
                serialized = ARObject._serialize_item(item, "DataPrototypeMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize first_operation
        if self.first_operation is not None:
            serialized = ARObject._serialize_item(self.first_operation, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-OPERATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize first_to_second
        if self.first_to_second is not None:
            serialized = ARObject._serialize_item(self.first_to_second, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-TO-SECOND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second
        if self.second is not None:
            serialized = ARObject._serialize_item(self.second, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse argument_refs (list from container "ARGUMENTS")
        obj.argument_refs = []
        container = ARObject._find_child_element(element, "ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.argument_refs.append(child_value)

        # Parse first_operation
        child = ARObject._find_child_element(element, "FIRST-OPERATION")
        if child is not None:
            first_operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.first_operation = first_operation_value

        # Parse first_to_second
        child = ARObject._find_child_element(element, "FIRST-TO-SECOND")
        if child is not None:
            first_to_second_value = ARObject._deserialize_by_tag(child, "DataTransformation")
            obj.first_to_second = first_to_second_value

        # Parse second
        child = ARObject._find_child_element(element, "SECOND")
        if child is not None:
            second_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.second = second_value

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
