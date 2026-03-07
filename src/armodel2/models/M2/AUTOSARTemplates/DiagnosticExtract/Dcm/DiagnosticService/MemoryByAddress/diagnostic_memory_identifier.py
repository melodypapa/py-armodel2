"""DiagnosticMemoryIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticMemoryIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMemoryIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-MEMORY-IDENTIFIER"


    access_ref: Optional[ARRef]
    id: Optional[PositiveInteger]
    memory_high: Optional[String]
    memory_low: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "ACCESS-REF": lambda obj, elem: setattr(obj, "access_ref", ARRef.deserialize(elem)),
        "ID": lambda obj, elem: setattr(obj, "id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MEMORY-HIGH": lambda obj, elem: setattr(obj, "memory_high", SerializationHelper.deserialize_by_tag(elem, "String")),
        "MEMORY-LOW": lambda obj, elem: setattr(obj, "memory_low", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticMemoryIdentifier."""
        super().__init__()
        self.access_ref: Optional[ARRef] = None
        self.id: Optional[PositiveInteger] = None
        self.memory_high: Optional[String] = None
        self.memory_low: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMemoryIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMemoryIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_ref
        if self.access_ref is not None:
            serialized = SerializationHelper.serialize_item(self.access_ref, "DiagnosticAccessPermission")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize memory_high
        if self.memory_high is not None:
            serialized = SerializationHelper.serialize_item(self.memory_high, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY-HIGH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize memory_low
        if self.memory_low is not None:
            serialized = SerializationHelper.serialize_item(self.memory_low, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY-LOW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryIdentifier":
        """Deserialize XML element to DiagnosticMemoryIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryIdentifier, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCESS-REF":
                setattr(obj, "access_ref", ARRef.deserialize(child))
            elif tag == "ID":
                setattr(obj, "id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MEMORY-HIGH":
                setattr(obj, "memory_high", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "MEMORY-LOW":
                setattr(obj, "memory_low", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class DiagnosticMemoryIdentifierBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticMemoryIdentifier with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticMemoryIdentifier = DiagnosticMemoryIdentifier()


    def with_access(self, value: Optional[DiagnosticAccessPermission]) -> "DiagnosticMemoryIdentifierBuilder":
        """Set access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'access' is required and cannot be None")
        self._obj.access = value
        return self

    def with_id(self, value: Optional[PositiveInteger]) -> "DiagnosticMemoryIdentifierBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'id' is required and cannot be None")
        self._obj.id = value
        return self

    def with_memory_high(self, value: Optional[String]) -> "DiagnosticMemoryIdentifierBuilder":
        """Set memory_high attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'memory_high' is required and cannot be None")
        self._obj.memory_high = value
        return self

    def with_memory_low(self, value: Optional[String]) -> "DiagnosticMemoryIdentifierBuilder":
        """Set memory_low attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'memory_low' is required and cannot be None")
        self._obj.memory_low = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "access",
        "id",
        "memoryHigh",
        "memoryLow",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticMemoryIdentifier:
        """Build and return the DiagnosticMemoryIdentifier instance with validation."""
        self._validate_instance()
        return self._obj