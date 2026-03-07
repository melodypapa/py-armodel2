"""DiagnosticSecurityLevel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticSecurityLevel(DiagnosticCommonElement):
    """AUTOSAR DiagnosticSecurityLevel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-SECURITY-LEVEL"


    access_data: Optional[PositiveInteger]
    key_size: Optional[PositiveInteger]
    num_failed: Optional[PositiveInteger]
    security_delay: Optional[TimeValue]
    seed_size: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ACCESS-DATA": lambda obj, elem: setattr(obj, "access_data", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "KEY-SIZE": lambda obj, elem: setattr(obj, "key_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "NUM-FAILED": lambda obj, elem: setattr(obj, "num_failed", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SECURITY-DELAY": lambda obj, elem: setattr(obj, "security_delay", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "SEED-SIZE": lambda obj, elem: setattr(obj, "seed_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticSecurityLevel."""
        super().__init__()
        self.access_data: Optional[PositiveInteger] = None
        self.key_size: Optional[PositiveInteger] = None
        self.num_failed: Optional[PositiveInteger] = None
        self.security_delay: Optional[TimeValue] = None
        self.seed_size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSecurityLevel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSecurityLevel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_data
        if self.access_data is not None:
            serialized = SerializationHelper.serialize_item(self.access_data, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_size
        if self.key_size is not None:
            serialized = SerializationHelper.serialize_item(self.key_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize num_failed
        if self.num_failed is not None:
            serialized = SerializationHelper.serialize_item(self.num_failed, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUM-FAILED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_delay
        if self.security_delay is not None:
            serialized = SerializationHelper.serialize_item(self.security_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize seed_size
        if self.seed_size is not None:
            serialized = SerializationHelper.serialize_item(self.seed_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEED-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityLevel":
        """Deserialize XML element to DiagnosticSecurityLevel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSecurityLevel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSecurityLevel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCESS-DATA":
                setattr(obj, "access_data", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "KEY-SIZE":
                setattr(obj, "key_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "NUM-FAILED":
                setattr(obj, "num_failed", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SECURITY-DELAY":
                setattr(obj, "security_delay", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "SEED-SIZE":
                setattr(obj, "seed_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticSecurityLevelBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticSecurityLevel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticSecurityLevel = DiagnosticSecurityLevel()


    def with_access_data(self, value: Optional[PositiveInteger]) -> "DiagnosticSecurityLevelBuilder":
        """Set access_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'access_data' is required and cannot be None")
        self._obj.access_data = value
        return self

    def with_key_size(self, value: Optional[PositiveInteger]) -> "DiagnosticSecurityLevelBuilder":
        """Set key_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'key_size' is required and cannot be None")
        self._obj.key_size = value
        return self

    def with_num_failed(self, value: Optional[PositiveInteger]) -> "DiagnosticSecurityLevelBuilder":
        """Set num_failed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'num_failed' is required and cannot be None")
        self._obj.num_failed = value
        return self

    def with_security_delay(self, value: Optional[TimeValue]) -> "DiagnosticSecurityLevelBuilder":
        """Set security_delay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'security_delay' is required and cannot be None")
        self._obj.security_delay = value
        return self

    def with_seed_size(self, value: Optional[PositiveInteger]) -> "DiagnosticSecurityLevelBuilder":
        """Set seed_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'seed_size' is required and cannot be None")
        self._obj.seed_size = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "accessData",
        "keySize",
        "numFailed",
        "securityDelay",
        "seedSize",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticSecurityLevel:
        """Build and return the DiagnosticSecurityLevel instance with validation."""
        self._validate_instance()
        return self._obj