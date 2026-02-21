"""ClientServerInterfaceToBswModuleEntryBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_ClientServerInterfaceToBsw.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface import (
    ClientServerInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
    PortDefinedArgumentValue,
)


class ClientServerInterfaceToBswModuleEntryBlueprintMapping(ARElement):
    """AUTOSAR ClientServerInterfaceToBswModuleEntryBlueprintMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_server_ref: ARRef
    operation: ClientServerOperation
    port_defined_arguments: list[PortDefinedArgumentValue]
    def __init__(self) -> None:
        """Initialize ClientServerInterfaceToBswModuleEntryBlueprintMapping."""
        super().__init__()
        self.client_server_ref: ARRef = None
        self.operation: ClientServerOperation = None
        self.port_defined_arguments: list[PortDefinedArgumentValue] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientServerInterfaceToBswModuleEntryBlueprintMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerInterfaceToBswModuleEntryBlueprintMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_server_ref
        if self.client_server_ref is not None:
            serialized = SerializationHelper.serialize_item(self.client_server_ref, "ClientServerInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-SERVER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize operation
        if self.operation is not None:
            serialized = SerializationHelper.serialize_item(self.operation, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_defined_arguments (list to container "PORT-DEFINED-ARGUMENTS")
        if self.port_defined_arguments:
            wrapper = ET.Element("PORT-DEFINED-ARGUMENTS")
            for item in self.port_defined_arguments:
                serialized = SerializationHelper.serialize_item(item, "PortDefinedArgumentValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterfaceToBswModuleEntryBlueprintMapping":
        """Deserialize XML element to ClientServerInterfaceToBswModuleEntryBlueprintMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerInterfaceToBswModuleEntryBlueprintMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerInterfaceToBswModuleEntryBlueprintMapping, cls).deserialize(element)

        # Parse client_server_ref
        child = SerializationHelper.find_child_element(element, "CLIENT-SERVER-REF")
        if child is not None:
            client_server_ref_value = ARRef.deserialize(child)
            obj.client_server_ref = client_server_ref_value

        # Parse operation
        child = SerializationHelper.find_child_element(element, "OPERATION")
        if child is not None:
            operation_value = SerializationHelper.deserialize_by_tag(child, "ClientServerOperation")
            obj.operation = operation_value

        # Parse port_defined_arguments (list from container "PORT-DEFINED-ARGUMENTS")
        obj.port_defined_arguments = []
        container = SerializationHelper.find_child_element(element, "PORT-DEFINED-ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_defined_arguments.append(child_value)

        return obj



class ClientServerInterfaceToBswModuleEntryBlueprintMappingBuilder:
    """Builder for ClientServerInterfaceToBswModuleEntryBlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerInterfaceToBswModuleEntryBlueprintMapping = ClientServerInterfaceToBswModuleEntryBlueprintMapping()

    def build(self) -> ClientServerInterfaceToBswModuleEntryBlueprintMapping:
        """Build and return ClientServerInterfaceToBswModuleEntryBlueprintMapping object.

        Returns:
            ClientServerInterfaceToBswModuleEntryBlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
