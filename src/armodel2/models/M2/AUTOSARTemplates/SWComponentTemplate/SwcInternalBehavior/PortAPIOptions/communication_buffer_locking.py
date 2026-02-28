"""CommunicationBufferLocking AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 595)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import SwcSupportedFeatureBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    SupportBufferLockingEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CommunicationBufferLocking(SwcSupportedFeature):
    """AUTOSAR CommunicationBufferLocking."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COMMUNICATION-BUFFER-LOCKING"


    support_buffer_locking: Optional[SupportBufferLockingEnum]
    _DESERIALIZE_DISPATCH = {
        "SUPPORT-BUFFER-LOCKING": lambda obj, elem: setattr(obj, "support_buffer_locking", SupportBufferLockingEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CommunicationBufferLocking."""
        super().__init__()
        self.support_buffer_locking: Optional[SupportBufferLockingEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationBufferLocking to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationBufferLocking, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize support_buffer_locking
        if self.support_buffer_locking is not None:
            serialized = SerializationHelper.serialize_item(self.support_buffer_locking, "SupportBufferLockingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-BUFFER-LOCKING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationBufferLocking":
        """Deserialize XML element to CommunicationBufferLocking object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationBufferLocking object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationBufferLocking, cls).deserialize(element)

        # Parse support_buffer_locking
        child = SerializationHelper.find_child_element(element, "SUPPORT-BUFFER-LOCKING")
        if child is not None:
            support_buffer_locking_value = SupportBufferLockingEnum.deserialize(child)
            obj.support_buffer_locking = support_buffer_locking_value

        return obj



class CommunicationBufferLockingBuilder(SwcSupportedFeatureBuilder):
    """Builder for CommunicationBufferLocking with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CommunicationBufferLocking = CommunicationBufferLocking()


    def with_support_buffer_locking(self, value: Optional[SupportBufferLockingEnum]) -> "CommunicationBufferLockingBuilder":
        """Set support_buffer_locking attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.support_buffer_locking = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> CommunicationBufferLocking:
        """Build and return the CommunicationBufferLocking instance with validation."""
        self._validate_instance()
        pass
        return self._obj