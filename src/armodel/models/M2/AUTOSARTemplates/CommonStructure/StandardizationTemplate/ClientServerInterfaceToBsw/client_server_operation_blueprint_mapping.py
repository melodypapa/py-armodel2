"""ClientServerOperationBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 68)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_ClientServerInterfaceToBsw.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class ClientServerOperationBlueprintMapping(ARObject):
    """AUTOSAR ClientServerOperationBlueprintMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    blueprint: Optional[DocumentationBlock]
    bsw_module_entry_ref: ARRef
    client_server_ref: ARRef
    def __init__(self) -> None:
        """Initialize ClientServerOperationBlueprintMapping."""
        super().__init__()
        self.blueprint: Optional[DocumentationBlock] = None
        self.bsw_module_entry_ref: ARRef = None
        self.client_server_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerOperationBlueprintMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerOperationBlueprintMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize blueprint
        if self.blueprint is not None:
            serialized = SerializationHelper.serialize_item(self.blueprint, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bsw_module_entry_ref
        if self.bsw_module_entry_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_module_entry_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize client_server_ref
        if self.client_server_ref is not None:
            serialized = SerializationHelper.serialize_item(self.client_server_ref, "ClientServerOperation")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperationBlueprintMapping":
        """Deserialize XML element to ClientServerOperationBlueprintMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerOperationBlueprintMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerOperationBlueprintMapping, cls).deserialize(element)

        # Parse blueprint
        child = SerializationHelper.find_child_element(element, "BLUEPRINT")
        if child is not None:
            blueprint_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.blueprint = blueprint_value

        # Parse bsw_module_entry_ref
        child = SerializationHelper.find_child_element(element, "BSW-MODULE-ENTRY-REF")
        if child is not None:
            bsw_module_entry_ref_value = ARRef.deserialize(child)
            obj.bsw_module_entry_ref = bsw_module_entry_ref_value

        # Parse client_server_ref
        child = SerializationHelper.find_child_element(element, "CLIENT-SERVER-REF")
        if child is not None:
            client_server_ref_value = ARRef.deserialize(child)
            obj.client_server_ref = client_server_ref_value

        return obj



class ClientServerOperationBlueprintMappingBuilder:
    """Builder for ClientServerOperationBlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperationBlueprintMapping = ClientServerOperationBlueprintMapping()

    def build(self) -> ClientServerOperationBlueprintMapping:
        """Build and return ClientServerOperationBlueprintMapping object.

        Returns:
            ClientServerOperationBlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
