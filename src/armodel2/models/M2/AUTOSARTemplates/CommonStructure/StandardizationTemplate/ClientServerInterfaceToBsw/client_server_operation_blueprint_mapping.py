"""ClientServerOperationBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 68)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_ClientServerInterfaceToBsw.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientServerOperationBlueprintMapping(ARObject):
    """AUTOSAR ClientServerOperationBlueprintMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-SERVER-OPERATION-BLUEPRINT-MAPPING"


    blueprint: Optional[DocumentationBlock]
    bsw_module_entry_ref: ARRef
    client_server_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "BLUEPRINT": lambda obj, elem: setattr(obj, "blueprint", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "BSW-MODULE-ENTRY-REF": lambda obj, elem: setattr(obj, "bsw_module_entry_ref", ARRef.deserialize(elem)),
        "CLIENT-SERVER-REF": lambda obj, elem: setattr(obj, "client_server_ref", ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BLUEPRINT":
                setattr(obj, "blueprint", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "BSW-MODULE-ENTRY-REF":
                setattr(obj, "bsw_module_entry_ref", ARRef.deserialize(child))
            elif tag == "CLIENT-SERVER-REF":
                setattr(obj, "client_server_ref", ARRef.deserialize(child))

        return obj



class ClientServerOperationBlueprintMappingBuilder(BuilderBase):
    """Builder for ClientServerOperationBlueprintMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerOperationBlueprintMapping = ClientServerOperationBlueprintMapping()


    def with_blueprint(self, value: Optional[DocumentationBlock]) -> "ClientServerOperationBlueprintMappingBuilder":
        """Set blueprint attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.blueprint = value
        return self

    def with_bsw_module_entry(self, value: BswModuleEntry) -> "ClientServerOperationBlueprintMappingBuilder":
        """Set bsw_module_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_module_entry = value
        return self

    def with_client_server(self, value: ClientServerOperation) -> "ClientServerOperationBlueprintMappingBuilder":
        """Set client_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.client_server = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "bswModuleEntry",
        "clientServer",
    }
    _OPTIONAL_ATTRIBUTES = {
        "blueprint",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "bswModuleEntry", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'bswModuleEntry' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'bswModuleEntry' is None", UserWarning)
        if getattr(self._obj, "clientServer", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'clientServer' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'clientServer' is None", UserWarning)


    def build(self) -> ClientServerOperationBlueprintMapping:
        """Build and return the ClientServerOperationBlueprintMapping instance with validation."""
        self._validate_instance()
        return self._obj