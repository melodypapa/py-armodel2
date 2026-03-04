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
        "COMM-CONNECTOR-REFS": ("_POLYMORPHIC_LIST", "comm_connector_refs", ["AbstractCanCommunicationConnector", "CanCommunicationConnector", "EthernetCommunicationConnector", "FlexrayCommunicationConnector", "LinCommunicationConnector", "TtcanCommunicationConnector", "UserDefinedCommunicationConnector"]),
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
            if tag == "COMM-CONNECTOR-REFS":
                for item_elem in child:
                    obj.comm_connector_refs.append(ARRef.deserialize(item_elem))

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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "commConnector",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SecurityEventContextMappingCommConnector:
        """Build and return the SecurityEventContextMappingCommConnector instance with validation."""
        self._validate_instance()
        return self._obj