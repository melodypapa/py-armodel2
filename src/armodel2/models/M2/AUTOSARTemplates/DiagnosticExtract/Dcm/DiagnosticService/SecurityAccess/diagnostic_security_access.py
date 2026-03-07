"""DiagnosticSecurityAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 96)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SecurityAccess.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_security_level import (
    DiagnosticSecurityLevel,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticSecurityAccess(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSecurityAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-SECURITY-ACCESS"


    request_seed_id: Optional[PositiveInteger]
    security_access_ref: Optional[Any]
    security_delay: Optional[TimeValue]
    security_level_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "REQUEST-SEED-ID": lambda obj, elem: setattr(obj, "request_seed_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SECURITY-ACCESS-REF": lambda obj, elem: setattr(obj, "security_access_ref", ARRef.deserialize(elem)),
        "SECURITY-DELAY": lambda obj, elem: setattr(obj, "security_delay", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "SECURITY-LEVEL-REF": lambda obj, elem: setattr(obj, "security_level_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticSecurityAccess."""
        super().__init__()
        self.request_seed_id: Optional[PositiveInteger] = None
        self.security_access_ref: Optional[Any] = None
        self.security_delay: Optional[TimeValue] = None
        self.security_level_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSecurityAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSecurityAccess, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize request_seed_id
        if self.request_seed_id is not None:
            serialized = SerializationHelper.serialize_item(self.request_seed_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-SEED-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_access_ref
        if self.security_access_ref is not None:
            serialized = SerializationHelper.serialize_item(self.security_access_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-ACCESS-REF")
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

        # Serialize security_level_ref
        if self.security_level_ref is not None:
            serialized = SerializationHelper.serialize_item(self.security_level_ref, "DiagnosticSecurityLevel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-LEVEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityAccess":
        """Deserialize XML element to DiagnosticSecurityAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSecurityAccess object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSecurityAccess, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "REQUEST-SEED-ID":
                setattr(obj, "request_seed_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SECURITY-ACCESS-REF":
                setattr(obj, "security_access_ref", ARRef.deserialize(child))
            elif tag == "SECURITY-DELAY":
                setattr(obj, "security_delay", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "SECURITY-LEVEL-REF":
                setattr(obj, "security_level_ref", ARRef.deserialize(child))

        return obj



class DiagnosticSecurityAccessBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticSecurityAccess with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticSecurityAccess = DiagnosticSecurityAccess()


    def with_request_seed_id(self, value: Optional[PositiveInteger]) -> "DiagnosticSecurityAccessBuilder":
        """Set request_seed_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'request_seed_id' is required and cannot be None")
        self._obj.request_seed_id = value
        return self

    def with_security_access(self, value: Optional[Any]) -> "DiagnosticSecurityAccessBuilder":
        """Set security_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'security_access' is required and cannot be None")
        self._obj.security_access = value
        return self

    def with_security_delay(self, value: Optional[TimeValue]) -> "DiagnosticSecurityAccessBuilder":
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

    def with_security_level(self, value: Optional[DiagnosticSecurityLevel]) -> "DiagnosticSecurityAccessBuilder":
        """Set security_level attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'security_level' is required and cannot be None")
        self._obj.security_level = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "requestSeedId",
        "securityAccess",
        "securityDelay",
        "securityLevel",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticSecurityAccess:
        """Build and return the DiagnosticSecurityAccess instance with validation."""
        self._validate_instance()
        return self._obj