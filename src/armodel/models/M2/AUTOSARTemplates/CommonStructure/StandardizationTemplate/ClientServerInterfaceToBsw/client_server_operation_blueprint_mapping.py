"""ClientServerOperationBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 68)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_ClientServerInterfaceToBsw.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    bsw_module_entry: BswModuleEntry
    client_server: ClientServerOperation
    def __init__(self) -> None:
        """Initialize ClientServerOperationBlueprintMapping."""
        super().__init__()
        self.blueprint: Optional[DocumentationBlock] = None
        self.bsw_module_entry: BswModuleEntry = None
        self.client_server: ClientServerOperation = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerOperationBlueprintMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize blueprint
        if self.blueprint is not None:
            serialized = ARObject._serialize_item(self.blueprint, "DocumentationBlock")
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

        # Serialize bsw_module_entry
        if self.bsw_module_entry is not None:
            serialized = ARObject._serialize_item(self.bsw_module_entry, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize client_server
        if self.client_server is not None:
            serialized = ARObject._serialize_item(self.client_server, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-SERVER")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse blueprint
        child = ARObject._find_child_element(element, "BLUEPRINT")
        if child is not None:
            blueprint_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.blueprint = blueprint_value

        # Parse bsw_module_entry
        child = ARObject._find_child_element(element, "BSW-MODULE-ENTRY")
        if child is not None:
            bsw_module_entry_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.bsw_module_entry = bsw_module_entry_value

        # Parse client_server
        child = ARObject._find_child_element(element, "CLIENT-SERVER")
        if child is not None:
            client_server_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.client_server = client_server_value

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
