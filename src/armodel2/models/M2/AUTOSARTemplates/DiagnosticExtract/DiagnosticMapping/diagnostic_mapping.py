"""DiagnosticMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 223)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticMapping(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    provider_ref: Optional[ARRef]
    requester_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PROVIDER-REF": lambda obj, elem: setattr(obj, "provider_ref", ARRef.deserialize(elem)),
        "REQUESTER-REF": lambda obj, elem: setattr(obj, "requester_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticMapping."""
        super().__init__()
        self.provider_ref: Optional[ARRef] = None
        self.requester_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provider_ref
        if self.provider_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provider_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requester_ref
        if self.requester_ref is not None:
            serialized = SerializationHelper.serialize_item(self.requester_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUESTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMapping":
        """Deserialize XML element to DiagnosticMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROVIDER-REF":
                setattr(obj, "provider_ref", ARRef.deserialize(child))
            elif tag == "REQUESTER-REF":
                setattr(obj, "requester_ref", ARRef.deserialize(child))

        return obj



class DiagnosticMappingBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticMapping = DiagnosticMapping()


    def with_provider(self, value: Optional[CpSoftwareCluster]) -> "DiagnosticMappingBuilder":
        """Set provider attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'provider' is required and cannot be None")
        self._obj.provider = value
        return self

    def with_requester(self, value: Optional[CpSoftwareCluster]) -> "DiagnosticMappingBuilder":
        """Set requester attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'requester' is required and cannot be None")
        self._obj.requester = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "provider",
        "requester",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> DiagnosticMapping:
        """Build and return the DiagnosticMapping instance (abstract)."""
        raise NotImplementedError