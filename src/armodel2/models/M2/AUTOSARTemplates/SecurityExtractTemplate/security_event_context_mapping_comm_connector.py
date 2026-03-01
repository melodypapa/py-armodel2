"""SecurityEventContextMappingCommConnector AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import SecurityEventContextMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecurityEventContextMappingCommConnector(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingCommConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURITY-EVENT-CONTEXT-MAPPING-COMM-CONNECTOR"


    comm_connector_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMM-CONNECTORS": ("_POLYMORPHIC_LIST", "comm_connector_refs", ["AbstractCanCommunicationConnector", "EthernetCommunicationConnector", "FlexrayCommunicationConnector", "LinCommunicationConnector", "UserDefinedCommunicationConnector"]),
    }


    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingCommConnector."""
        super().__init__()
        self.comm_connector_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventContextMappingCommConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventContextMappingCommConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize comm_connector_refs (list to container "COMM-CONNECTOR-REFS")
        if self.comm_connector_refs:
            wrapper = ET.Element("COMM-CONNECTOR-REFS")
            for item in self.comm_connector_refs:
                serialized = SerializationHelper.serialize_item(item, "CommunicationConnector")
                if serialized is not None:
                    child_elem = ET.Element("COMM-CONNECTOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMappingCommConnector":
        """Deserialize XML element to SecurityEventContextMappingCommConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextMappingCommConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventContextMappingCommConnector, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "COMM-CONNECTORS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-CAN-COMMUNICATION-CONNECTOR":
                        obj.comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractCanCommunicationConnector"))
                    elif concrete_tag == "ETHERNET-COMMUNICATION-CONNECTOR":
                        obj.comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetCommunicationConnector"))
                    elif concrete_tag == "FLEXRAY-COMMUNICATION-CONNECTOR":
                        obj.comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayCommunicationConnector"))
                    elif concrete_tag == "LIN-COMMUNICATION-CONNECTOR":
                        obj.comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinCommunicationConnector"))
                    elif concrete_tag == "USER-DEFINED-COMMUNICATION-CONNECTOR":
                        obj.comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "UserDefinedCommunicationConnector"))

        return obj



class SecurityEventContextMappingCommConnectorBuilder(SecurityEventContextMappingBuilder):
    """Builder for SecurityEventContextMappingCommConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecurityEventContextMappingCommConnector = SecurityEventContextMappingCommConnector()


    def with_comm_connectors(self, items: list[CommunicationConnector]) -> "SecurityEventContextMappingCommConnectorBuilder":
        """Set comm_connectors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.comm_connectors = list(items) if items else []
        return self


    def add_comm_connector(self, item: CommunicationConnector) -> "SecurityEventContextMappingCommConnectorBuilder":
        """Add a single item to comm_connectors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.comm_connectors.append(item)
        return self

    def clear_comm_connectors(self) -> "SecurityEventContextMappingCommConnectorBuilder":
        """Clear all items from comm_connectors list.

        Returns:
            self for method chaining
        """
        self._obj.comm_connectors = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SecurityEventContextMappingCommConnector:
        """Build and return the SecurityEventContextMappingCommConnector instance with validation."""
        self._validate_instance()
        pass
        return self._obj