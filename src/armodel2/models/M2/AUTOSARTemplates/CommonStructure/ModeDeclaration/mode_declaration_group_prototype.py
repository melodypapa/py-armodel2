"""ModeDeclarationGroupPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 42)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 113)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2038)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 233)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwCalibrationAccessEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeDeclarationGroupPrototype(Identifiable):
    """AUTOSAR ModeDeclarationGroupPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-DECLARATION-GROUP-PROTOTYPE"


    sw_calibration_access: Optional[SwCalibrationAccessEnum]
    type_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SW-CALIBRATION-ACCESS": lambda obj, elem: setattr(obj, "sw_calibration_access", SwCalibrationAccessEnum.deserialize(elem)),
        "TYPE-TREF": lambda obj, elem: setattr(obj, "type_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ModeDeclarationGroupPrototype."""
        super().__init__()
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.type_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeDeclarationGroupPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeDeclarationGroupPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_calibration_access
        if self.sw_calibration_access is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calibration_access, "SwCalibrationAccessEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CALIBRATION-ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type_ref
        if self.type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.type_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroupPrototype":
        """Deserialize XML element to ModeDeclarationGroupPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationGroupPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeDeclarationGroupPrototype, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "SW-CALIBRATION-ACCESS":
                setattr(obj, "sw_calibration_access", SwCalibrationAccessEnum.deserialize(child))
            elif tag == "TYPE-TREF":
                setattr(obj, "type_ref", ARRef.deserialize(child))

        return obj



class ModeDeclarationGroupPrototypeBuilder(IdentifiableBuilder):
    """Builder for ModeDeclarationGroupPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeDeclarationGroupPrototype = ModeDeclarationGroupPrototype()


    def with_sw_calibration_access(self, value: Optional[SwCalibrationAccessEnum]) -> "ModeDeclarationGroupPrototypeBuilder":
        """Set sw_calibration_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_calibration_access = value
        return self

    def with_type(self, value: Optional[ModeDeclarationGroup]) -> "ModeDeclarationGroupPrototypeBuilder":
        """Set type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type = value
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


    def build(self) -> ModeDeclarationGroupPrototype:
        """Build and return the ModeDeclarationGroupPrototype instance with validation."""
        self._validate_instance()
        pass
        return self._obj