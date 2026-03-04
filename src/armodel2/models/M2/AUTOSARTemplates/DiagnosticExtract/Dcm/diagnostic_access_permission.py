"""DiagnosticAccessPermission AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_security_level import (
    DiagnosticSecurityLevel,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_session import (
    DiagnosticSession,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticAccessPermission(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAccessPermission."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-ACCESS-PERMISSION"


    authentication: Optional[DiagnosticAuthRole]
    diagnostic_session_refs: list[ARRef]
    environmental_ref: Optional[Any]
    security_level_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "AUTHENTICATION": lambda obj, elem: setattr(obj, "authentication", SerializationHelper.deserialize_by_tag(elem, "DiagnosticAuthRole")),
        "DIAGNOSTIC-SESSION-REFS": lambda obj, elem: [obj.diagnostic_session_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "ENVIRONMENTAL-REF": lambda obj, elem: setattr(obj, "environmental_ref", ARRef.deserialize(elem)),
        "SECURITY-LEVEL-REFS": lambda obj, elem: [obj.security_level_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DiagnosticAccessPermission."""
        super().__init__()
        self.authentication: Optional[DiagnosticAuthRole] = None
        self.diagnostic_session_refs: list[ARRef] = []
        self.environmental_ref: Optional[Any] = None
        self.security_level_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAccessPermission to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAccessPermission, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication
        if self.authentication is not None:
            serialized = SerializationHelper.serialize_item(self.authentication, "DiagnosticAuthRole")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_session_refs (list to container "DIAGNOSTIC-SESSION-REFS")
        if self.diagnostic_session_refs:
            wrapper = ET.Element("DIAGNOSTIC-SESSION-REFS")
            for item in self.diagnostic_session_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticSession")
                if serialized is not None:
                    child_elem = ET.Element("DIAGNOSTIC-SESSION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize environmental_ref
        if self.environmental_ref is not None:
            serialized = SerializationHelper.serialize_item(self.environmental_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENVIRONMENTAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_level_refs (list to container "SECURITY-LEVEL-REFS")
        if self.security_level_refs:
            wrapper = ET.Element("SECURITY-LEVEL-REFS")
            for item in self.security_level_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticSecurityLevel")
                if serialized is not None:
                    child_elem = ET.Element("SECURITY-LEVEL-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticAccessPermission":
        """Deserialize XML element to DiagnosticAccessPermission object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAccessPermission object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAccessPermission, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUTHENTICATION":
                setattr(obj, "authentication", SerializationHelper.deserialize_by_tag(child, "DiagnosticAuthRole"))
            elif tag == "DIAGNOSTIC-SESSION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.diagnostic_session_refs.append(ARRef.deserialize(item_elem))
            elif tag == "ENVIRONMENTAL-REF":
                setattr(obj, "environmental_ref", ARRef.deserialize(child))
            elif tag == "SECURITY-LEVEL-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.security_level_refs.append(ARRef.deserialize(item_elem))

        return obj



class DiagnosticAccessPermissionBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticAccessPermission with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticAccessPermission = DiagnosticAccessPermission()


    def with_authentication(self, value: Optional[DiagnosticAuthRole]) -> "DiagnosticAccessPermissionBuilder":
        """Set authentication attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.authentication = value
        return self

    def with_diagnostic_sessions(self, items: list[DiagnosticSession]) -> "DiagnosticAccessPermissionBuilder":
        """Set diagnostic_sessions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.diagnostic_sessions = list(items) if items else []
        return self

    def with_environmental(self, value: Optional[any (Diagnostic)]) -> "DiagnosticAccessPermissionBuilder":
        """Set environmental attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.environmental = value
        return self

    def with_security_levels(self, items: list[DiagnosticSecurityLevel]) -> "DiagnosticAccessPermissionBuilder":
        """Set security_levels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.security_levels = list(items) if items else []
        return self


    def add_diagnostic_session(self, item: DiagnosticSession) -> "DiagnosticAccessPermissionBuilder":
        """Add a single item to diagnostic_sessions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.diagnostic_sessions.append(item)
        return self

    def clear_diagnostic_sessions(self) -> "DiagnosticAccessPermissionBuilder":
        """Clear all items from diagnostic_sessions list.

        Returns:
            self for method chaining
        """
        self._obj.diagnostic_sessions = []
        return self

    def add_security_level(self, item: DiagnosticSecurityLevel) -> "DiagnosticAccessPermissionBuilder":
        """Add a single item to security_levels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.security_levels.append(item)
        return self

    def clear_security_levels(self) -> "DiagnosticAccessPermissionBuilder":
        """Clear all items from security_levels list.

        Returns:
            self for method chaining
        """
        self._obj.security_levels = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "authentication",
        "diagnosticSession",
        "environmental",
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


    def build(self) -> DiagnosticAccessPermission:
        """Build and return the DiagnosticAccessPermission instance with validation."""
        self._validate_instance()
        return self._obj