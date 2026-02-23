"""DiagnosticSecurityAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 96)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SecurityAccess.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_security_level import (
    DiagnosticSecurityLevel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticSecurityAccess(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSecurityAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_seed_id: Optional[PositiveInteger]
    security_access_ref: Optional[Any]
    security_delay: Optional[TimeValue]
    security_level_ref: Optional[ARRef]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse request_seed_id
        child = SerializationHelper.find_child_element(element, "REQUEST-SEED-ID")
        if child is not None:
            request_seed_id_value = child.text
            obj.request_seed_id = request_seed_id_value

        # Parse security_access_ref
        child = SerializationHelper.find_child_element(element, "SECURITY-ACCESS-REF")
        if child is not None:
            security_access_ref_value = ARRef.deserialize(child)
            obj.security_access_ref = security_access_ref_value

        # Parse security_delay
        child = SerializationHelper.find_child_element(element, "SECURITY-DELAY")
        if child is not None:
            security_delay_value = child.text
            obj.security_delay = security_delay_value

        # Parse security_level_ref
        child = SerializationHelper.find_child_element(element, "SECURITY-LEVEL-REF")
        if child is not None:
            security_level_ref_value = ARRef.deserialize(child)
            obj.security_level_ref = security_level_ref_value

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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.request_seed_id = value
        return self

    def with_security_access(self, value: Optional[any (DiagnosticSecurity)]) -> "DiagnosticSecurityAccessBuilder":
        """Set security_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.security_level = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> DiagnosticSecurityAccess:
        """Build and return the DiagnosticSecurityAccess instance with validation."""
        self._validate_instance()
        pass
        return self._obj