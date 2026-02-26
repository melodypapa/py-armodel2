"""DiagnosticSession AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import (
    DiagnosticJumpToBootLoaderEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticSession(DiagnosticCommonElement):
    """AUTOSAR DiagnosticSession."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    jump_to_boot: Optional[DiagnosticJumpToBootLoaderEnum]
    p2_server_max: Optional[TimeValue]
    p2_star_server: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize DiagnosticSession."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.jump_to_boot: Optional[DiagnosticJumpToBootLoaderEnum] = None
        self.p2_server_max: Optional[TimeValue] = None
        self.p2_star_server: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSession to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSession, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize jump_to_boot
        if self.jump_to_boot is not None:
            serialized = SerializationHelper.serialize_item(self.jump_to_boot, "DiagnosticJumpToBootLoaderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("JUMP-TO-BOOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p2_server_max
        if self.p2_server_max is not None:
            serialized = SerializationHelper.serialize_item(self.p2_server_max, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("P2-SERVER-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p2_star_server
        if self.p2_star_server is not None:
            serialized = SerializationHelper.serialize_item(self.p2_star_server, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("P2-STAR-SERVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSession":
        """Deserialize XML element to DiagnosticSession object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSession object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSession, cls).deserialize(element)

        # Parse id
        child = SerializationHelper.find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse jump_to_boot
        child = SerializationHelper.find_child_element(element, "JUMP-TO-BOOT")
        if child is not None:
            jump_to_boot_value = DiagnosticJumpToBootLoaderEnum.deserialize(child)
            obj.jump_to_boot = jump_to_boot_value

        # Parse p2_server_max
        child = SerializationHelper.find_child_element(element, "P2-SERVER-MAX")
        if child is not None:
            p2_server_max_value = child.text
            obj.p2_server_max = p2_server_max_value

        # Parse p2_star_server
        child = SerializationHelper.find_child_element(element, "P2-STAR-SERVER")
        if child is not None:
            p2_star_server_value = child.text
            obj.p2_star_server = p2_star_server_value

        return obj



class DiagnosticSessionBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticSession with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticSession = DiagnosticSession()


    def with_id(self, value: Optional[PositiveInteger]) -> "DiagnosticSessionBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.id = value
        return self

    def with_jump_to_boot(self, value: Optional[DiagnosticJumpToBootLoaderEnum]) -> "DiagnosticSessionBuilder":
        """Set jump_to_boot attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.jump_to_boot = value
        return self

    def with_p2_server_max(self, value: Optional[TimeValue]) -> "DiagnosticSessionBuilder":
        """Set p2_server_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.p2_server_max = value
        return self

    def with_p2_star_server(self, value: Optional[TimeValue]) -> "DiagnosticSessionBuilder":
        """Set p2_star_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.p2_star_server = value
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


    def build(self) -> DiagnosticSession:
        """Build and return the DiagnosticSession instance with validation."""
        self._validate_instance()
        pass
        return self._obj