"""SwValues AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 458)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.numerical_or_text import (
    NumericalOrText,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.value_group import (
        ValueGroup,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwValues(ARObject):
    """AUTOSAR SwValues."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    v: Optional[Numerical]
    vf: Optional[Numerical]
    vg_ref: Optional[ARRef]
    vt: Optional[VerbatimString]
    vtf: Optional[NumericalOrText]
    def __init__(self) -> None:
        """Initialize SwValues."""
        super().__init__()
        self.v: Optional[Numerical] = None
        self.vf: Optional[Numerical] = None
        self.vg_ref: Optional[ARRef] = None
        self.vt: Optional[VerbatimString] = None
        self.vtf: Optional[NumericalOrText] = None

    def serialize(self) -> ET.Element:
        """Serialize SwValues to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwValues, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize v
        if self.v is not None:
            serialized = SerializationHelper.serialize_item(self.v, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vf
        if self.vf is not None:
            serialized = SerializationHelper.serialize_item(self.vf, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vg_ref
        if self.vg_ref is not None:
            serialized = SerializationHelper.serialize_item(self.vg_ref, "ValueGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VG-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vt
        if self.vt is not None:
            serialized = SerializationHelper.serialize_item(self.vt, "VerbatimString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vtf
        if self.vtf is not None:
            serialized = SerializationHelper.serialize_item(self.vtf, "NumericalOrText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VTF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwValues":
        """Deserialize XML element to SwValues object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwValues object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwValues, cls).deserialize(element)

        # Parse v
        child = SerializationHelper.find_child_element(element, "V")
        if child is not None:
            v_value = child.text
            obj.v = v_value

        # Parse vf
        child = SerializationHelper.find_child_element(element, "VF")
        if child is not None:
            vf_value = child.text
            obj.vf = vf_value

        # Parse vg_ref
        child = SerializationHelper.find_child_element(element, "VG-REF")
        if child is not None:
            vg_ref_value = ARRef.deserialize(child)
            obj.vg_ref = vg_ref_value

        # Parse vt
        child = SerializationHelper.find_child_element(element, "VT")
        if child is not None:
            vt_value = SerializationHelper.deserialize_by_tag(child, "VerbatimString")
            obj.vt = vt_value

        # Parse vtf
        child = SerializationHelper.find_child_element(element, "VTF")
        if child is not None:
            vtf_value = SerializationHelper.deserialize_by_tag(child, "NumericalOrText")
            obj.vtf = vtf_value

        return obj



class SwValuesBuilder(BuilderBase):
    """Builder for SwValues with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwValues = SwValues()


    def with_v(self, value: Optional[Numerical]) -> "SwValuesBuilder":
        """Set v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.v = value
        return self

    def with_vf(self, value: Optional[Numerical]) -> "SwValuesBuilder":
        """Set vf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vf = value
        return self

    def with_vg(self, value: Optional[ValueGroup]) -> "SwValuesBuilder":
        """Set vg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vg = value
        return self

    def with_vt(self, value: Optional[VerbatimString]) -> "SwValuesBuilder":
        """Set vt attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vt = value
        return self

    def with_vtf(self, value: Optional[NumericalOrText]) -> "SwValuesBuilder":
        """Set vtf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vtf = value
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


    def build(self) -> SwValues:
        """Build and return the SwValues instance with validation."""
        self._validate_instance()
        pass
        return self._obj