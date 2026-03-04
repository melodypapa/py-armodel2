"""SocketConnectionIpduIdentifierSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 490)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SocketConnectionIpduIdentifierSet(FibexElement):
    """AUTOSAR SocketConnectionIpduIdentifierSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SOCKET-CONNECTION-IPDU-IDENTIFIER-SET"


    i_pdu_identifiers: list[SoConIPduIdentifier]
    _DESERIALIZE_DISPATCH = {
        "I-PDU-IDENTIFIERS": lambda obj, elem: obj.i_pdu_identifiers.append(SerializationHelper.deserialize_by_tag(elem, "SoConIPduIdentifier")),
    }


    def __init__(self) -> None:
        """Initialize SocketConnectionIpduIdentifierSet."""
        super().__init__()
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []

    def serialize(self) -> ET.Element:
        """Serialize SocketConnectionIpduIdentifierSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SocketConnectionIpduIdentifierSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_identifiers (list to container "I-PDU-IDENTIFIERS")
        if self.i_pdu_identifiers:
            wrapper = ET.Element("I-PDU-IDENTIFIERS")
            for item in self.i_pdu_identifiers:
                serialized = SerializationHelper.serialize_item(item, "SoConIPduIdentifier")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketConnectionIpduIdentifierSet":
        """Deserialize XML element to SocketConnectionIpduIdentifierSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SocketConnectionIpduIdentifierSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SocketConnectionIpduIdentifierSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "I-PDU-IDENTIFIERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_pdu_identifiers.append(SerializationHelper.deserialize_by_tag(item_elem, "SoConIPduIdentifier"))

        return obj



class SocketConnectionIpduIdentifierSetBuilder(FibexElementBuilder):
    """Builder for SocketConnectionIpduIdentifierSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SocketConnectionIpduIdentifierSet = SocketConnectionIpduIdentifierSet()


    def with_i_pdu_identifiers(self, items: list[SoConIPduIdentifier]) -> "SocketConnectionIpduIdentifierSetBuilder":
        """Set i_pdu_identifiers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_identifiers = list(items) if items else []
        return self


    def add_i_pdu_identifier(self, item: SoConIPduIdentifier) -> "SocketConnectionIpduIdentifierSetBuilder":
        """Add a single item to i_pdu_identifiers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_identifiers.append(item)
        return self

    def clear_i_pdu_identifiers(self) -> "SocketConnectionIpduIdentifierSetBuilder":
        """Clear all items from i_pdu_identifiers list.

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_identifiers = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "iPduIdentifier",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SocketConnectionIpduIdentifierSet:
        """Build and return the SocketConnectionIpduIdentifierSet instance with validation."""
        self._validate_instance()
        return self._obj