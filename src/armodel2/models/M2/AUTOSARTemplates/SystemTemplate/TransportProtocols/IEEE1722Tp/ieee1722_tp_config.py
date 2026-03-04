"""IEEE1722TpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 636)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import TpConfigBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpConfig(TpConfig):
    """AUTOSAR IEEE1722TpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-E-E-E1722-TP-CONFIG"


    tp_connection_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "TP-CONNECTION-REFS": ("_POLYMORPHIC_LIST", "tp_connection_refs", ["IEEE1722TpAafConnection", "IEEE1722TpAcfConnection", "IEEE1722TpAvConnection", "IEEE1722TpCrfConnection", "IEEE1722TpIidcConnection"]),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpConfig."""
        super().__init__()
        self.tp_connection_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_connection_refs (list to container "TP-CONNECTION-REFS")
        if self.tp_connection_refs:
            wrapper = ET.Element("TP-CONNECTION-REFS")
            for item in self.tp_connection_refs:
                serialized = SerializationHelper.serialize_item(item, "IEEE1722TpConnection")
                if serialized is not None:
                    child_elem = ET.Element("TP-CONNECTION-REF")
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
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpConfig":
        """Deserialize XML element to IEEE1722TpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TP-CONNECTION-REFS":
                for item_elem in child:
                    obj.tp_connection_refs.append(ARRef.deserialize(item_elem))

        return obj



class IEEE1722TpConfigBuilder(TpConfigBuilder):
    """Builder for IEEE1722TpConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpConfig = IEEE1722TpConfig()


    def with_tp_connections(self, items: list[IEEE1722TpConnection]) -> "IEEE1722TpConfigBuilder":
        """Set tp_connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = list(items) if items else []
        return self


    def add_tp_connection(self, item: IEEE1722TpConnection) -> "IEEE1722TpConfigBuilder":
        """Add a single item to tp_connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_connections.append(item)
        return self

    def clear_tp_connections(self) -> "IEEE1722TpConfigBuilder":
        """Clear all items from tp_connections list.

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tpConnection",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IEEE1722TpConfig:
        """Build and return the IEEE1722TpConfig instance with validation."""
        self._validate_instance()
        return self._obj