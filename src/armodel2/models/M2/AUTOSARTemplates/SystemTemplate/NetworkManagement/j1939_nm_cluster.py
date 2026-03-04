"""J1939NmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 691)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import NmClusterBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class J1939NmCluster(NmCluster):
    """AUTOSAR J1939NmCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "J1939-NM-CLUSTER"


    address_claim: Optional[Boolean]
    uses_dynamic: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ADDRESS-CLAIM": lambda obj, elem: setattr(obj, "address_claim", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "USES-DYNAMIC": lambda obj, elem: setattr(obj, "uses_dynamic", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize J1939NmCluster."""
        super().__init__()
        self.address_claim: Optional[Boolean] = None
        self.uses_dynamic: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize J1939NmCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939NmCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize address_claim
        if self.address_claim is not None:
            serialized = SerializationHelper.serialize_item(self.address_claim, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDRESS-CLAIM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uses_dynamic
        if self.uses_dynamic is not None:
            serialized = SerializationHelper.serialize_item(self.uses_dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USES-DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939NmCluster":
        """Deserialize XML element to J1939NmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939NmCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939NmCluster, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ADDRESS-CLAIM":
                setattr(obj, "address_claim", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "USES-DYNAMIC":
                setattr(obj, "uses_dynamic", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class J1939NmClusterBuilder(NmClusterBuilder):
    """Builder for J1939NmCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939NmCluster = J1939NmCluster()


    def with_address_claim(self, value: Optional[Boolean]) -> "J1939NmClusterBuilder":
        """Set address_claim attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.address_claim = value
        return self

    def with_uses_dynamic(self, value: Optional[Boolean]) -> "J1939NmClusterBuilder":
        """Set uses_dynamic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uses_dynamic = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "addressClaim",
        "usesDynamic",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> J1939NmCluster:
        """Build and return the J1939NmCluster instance with validation."""
        self._validate_instance()
        return self._obj