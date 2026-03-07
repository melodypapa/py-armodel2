"""SecureCommunicationFreshnessProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecureCommunicationFreshnessProps(Identifiable):
    """AUTOSAR SecureCommunicationFreshnessProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURE-COMMUNICATION-FRESHNESS-PROPS"


    freshness: Optional[PositiveInteger]
    freshness_value: Optional[PositiveInteger]
    use_freshness: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "FRESHNESS": lambda obj, elem: setattr(obj, "freshness", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "FRESHNESS-VALUE": lambda obj, elem: setattr(obj, "freshness_value", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "USE-FRESHNESS": lambda obj, elem: setattr(obj, "use_freshness", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize SecureCommunicationFreshnessProps."""
        super().__init__()
        self.freshness: Optional[PositiveInteger] = None
        self.freshness_value: Optional[PositiveInteger] = None
        self.use_freshness: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize SecureCommunicationFreshnessProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecureCommunicationFreshnessProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize freshness
        if self.freshness is not None:
            serialized = SerializationHelper.serialize_item(self.freshness, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRESHNESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize freshness_value
        if self.freshness_value is not None:
            serialized = SerializationHelper.serialize_item(self.freshness_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRESHNESS-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_freshness
        if self.use_freshness is not None:
            serialized = SerializationHelper.serialize_item(self.use_freshness, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-FRESHNESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationFreshnessProps":
        """Deserialize XML element to SecureCommunicationFreshnessProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationFreshnessProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecureCommunicationFreshnessProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FRESHNESS":
                setattr(obj, "freshness", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "FRESHNESS-VALUE":
                setattr(obj, "freshness_value", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "USE-FRESHNESS":
                setattr(obj, "use_freshness", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class SecureCommunicationFreshnessPropsBuilder(IdentifiableBuilder):
    """Builder for SecureCommunicationFreshnessProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecureCommunicationFreshnessProps = SecureCommunicationFreshnessProps()


    def with_freshness(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessPropsBuilder":
        """Set freshness attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'freshness' is required and cannot be None")
        self._obj.freshness = value
        return self

    def with_freshness_value(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessPropsBuilder":
        """Set freshness_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'freshness_value' is required and cannot be None")
        self._obj.freshness_value = value
        return self

    def with_use_freshness(self, value: Optional[Boolean]) -> "SecureCommunicationFreshnessPropsBuilder":
        """Set use_freshness attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'use_freshness' is required and cannot be None")
        self._obj.use_freshness = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "freshness",
        "freshnessValue",
        "useFreshness",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SecureCommunicationFreshnessProps:
        """Build and return the SecureCommunicationFreshnessProps instance with validation."""
        self._validate_instance()
        return self._obj