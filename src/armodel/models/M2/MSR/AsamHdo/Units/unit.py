"""Unit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 333)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 64)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 400)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 479)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_unit_names import (
    SingleLanguageUnitNames,
)


class Unit(ARElement):
    """AUTOSAR Unit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    display_name: Optional[SingleLanguageUnitNames]
    factor_si_to_unit: Optional[Float]
    offset_si_to_unit: Optional[Float]
    physical_dimension_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize Unit."""
        super().__init__()
        self.display_name: Optional[SingleLanguageUnitNames] = None
        self.factor_si_to_unit: Optional[Float] = None
        self.offset_si_to_unit: Optional[Float] = None
        self.physical_dimension_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize Unit to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Unit, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize display_name
        if self.display_name is not None:
            serialized = SerializationHelper.serialize_item(self.display_name, "SingleLanguageUnitNames")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DISPLAY-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize factor_si_to_unit
        if self.factor_si_to_unit is not None:
            serialized = SerializationHelper.serialize_item(self.factor_si_to_unit, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FACTOR-SI-TO-UNIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset_si_to_unit
        if self.offset_si_to_unit is not None:
            serialized = SerializationHelper.serialize_item(self.offset_si_to_unit, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET-SI-TO-UNIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize physical_dimension_ref
        if self.physical_dimension_ref is not None:
            serialized = SerializationHelper.serialize_item(self.physical_dimension_ref, "physicalDimension")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-DIMENSION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Unit":
        """Deserialize XML element to Unit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Unit object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Unit, cls).deserialize(element)

        # Parse display_name
        child = SerializationHelper.find_child_element(element, "DISPLAY-NAME")
        if child is not None:
            display_name_value = SerializationHelper.deserialize_by_tag(child, "SingleLanguageUnitNames")
            obj.display_name = display_name_value

        # Parse factor_si_to_unit
        child = SerializationHelper.find_child_element(element, "FACTOR-SI-TO-UNIT")
        if child is not None:
            factor_si_to_unit_value = child.text
            obj.factor_si_to_unit = factor_si_to_unit_value

        # Parse offset_si_to_unit
        child = SerializationHelper.find_child_element(element, "OFFSET-SI-TO-UNIT")
        if child is not None:
            offset_si_to_unit_value = child.text
            obj.offset_si_to_unit = offset_si_to_unit_value

        # Parse physical_dimension_ref
        child = SerializationHelper.find_child_element(element, "PHYSICAL-DIMENSION-REF")
        if child is not None:
            physical_dimension_ref_value = ARRef.deserialize(child)
            obj.physical_dimension_ref = physical_dimension_ref_value

        return obj



class UnitBuilder(ARElementBuilder):
    """Builder for Unit with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Unit = Unit()


    def with_display_name(self, value: Optional[SingleLanguageUnitNames]) -> "UnitBuilder":
        """Set display_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.display_name = value
        return self

    def with_factor_si_to_unit(self, value: Optional[Float]) -> "UnitBuilder":
        """Set factor_si_to_unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.factor_si_to_unit = value
        return self

    def with_offset_si_to_unit(self, value: Optional[Float]) -> "UnitBuilder":
        """Set offset_si_to_unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.offset_si_to_unit = value
        return self

    def with_physical_dimension(self, value: Optional[physicalDimension]) -> "UnitBuilder":
        """Set physical_dimension attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.physical_dimension = value
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


    def build(self) -> Unit:
        """Build and return the Unit instance with validation."""
        self._validate_instance()
        pass
        return self._obj