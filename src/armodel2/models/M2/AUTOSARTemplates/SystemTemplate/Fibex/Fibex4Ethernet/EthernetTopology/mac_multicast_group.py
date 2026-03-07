"""MacMulticastGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MacMulticastGroup(Identifiable):
    """AUTOSAR MacMulticastGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MAC-MULTICAST-GROUP"


    mac_multicast: Optional[MacAddressString]
    _DESERIALIZE_DISPATCH = {
        "MAC-MULTICAST": lambda obj, elem: setattr(obj, "mac_multicast", SerializationHelper.deserialize_by_tag(elem, "MacAddressString")),
    }


    def __init__(self) -> None:
        """Initialize MacMulticastGroup."""
        super().__init__()
        self.mac_multicast: Optional[MacAddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize MacMulticastGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacMulticastGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mac_multicast
        if self.mac_multicast is not None:
            serialized = SerializationHelper.serialize_item(self.mac_multicast, "MacAddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-MULTICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacMulticastGroup":
        """Deserialize XML element to MacMulticastGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacMulticastGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacMulticastGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAC-MULTICAST":
                setattr(obj, "mac_multicast", SerializationHelper.deserialize_by_tag(child, "MacAddressString"))

        return obj



class MacMulticastGroupBuilder(IdentifiableBuilder):
    """Builder for MacMulticastGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MacMulticastGroup = MacMulticastGroup()


    def with_mac_multicast(self, value: Optional[MacAddressString]) -> "MacMulticastGroupBuilder":
        """Set mac_multicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'mac_multicast' is required and cannot be None")
        self._obj.mac_multicast = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "macMulticast",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MacMulticastGroup:
        """Build and return the MacMulticastGroup instance with validation."""
        self._validate_instance()
        return self._obj