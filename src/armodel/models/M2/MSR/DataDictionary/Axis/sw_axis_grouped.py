"""SwAxisGrouped AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 357)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import SwCalprmAxisTypePropsBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class SwAxisGrouped(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisGrouped."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    shared_axis_type_ref: Optional[ARRef]
    sw_axis_index: Optional[AxisIndexType]
    sw_calprm_ref_proxy_ref: ARRef
    def __init__(self) -> None:
        """Initialize SwAxisGrouped."""
        super().__init__()
        self.shared_axis_type_ref: Optional[ARRef] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_calprm_ref_proxy_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize SwAxisGrouped to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAxisGrouped, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize shared_axis_type_ref
        if self.shared_axis_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.shared_axis_type_ref, "ApplicationPrimitiveDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHARED-AXIS-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_axis_index
        if self.sw_axis_index is not None:
            serialized = SerializationHelper.serialize_item(self.sw_axis_index, "AxisIndexType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-AXIS-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_calprm_ref_proxy_ref
        if self.sw_calprm_ref_proxy_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calprm_ref_proxy_ref, "SwCalprmRefProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CALPRM-REF-PROXY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisGrouped":
        """Deserialize XML element to SwAxisGrouped object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisGrouped object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAxisGrouped, cls).deserialize(element)

        # Parse shared_axis_type_ref
        child = SerializationHelper.find_child_element(element, "SHARED-AXIS-TYPE-REF")
        if child is not None:
            shared_axis_type_ref_value = ARRef.deserialize(child)
            obj.shared_axis_type_ref = shared_axis_type_ref_value

        # Parse sw_axis_index
        child = SerializationHelper.find_child_element(element, "SW-AXIS-INDEX")
        if child is not None:
            sw_axis_index_value = child.text
            obj.sw_axis_index = sw_axis_index_value

        # Parse sw_calprm_ref_proxy_ref
        child = SerializationHelper.find_child_element(element, "SW-CALPRM-REF-PROXY-REF")
        if child is not None:
            sw_calprm_ref_proxy_ref_value = ARRef.deserialize(child)
            obj.sw_calprm_ref_proxy_ref = sw_calprm_ref_proxy_ref_value

        return obj



class SwAxisGroupedBuilder(SwCalprmAxisTypePropsBuilder):
    """Builder for SwAxisGrouped with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwAxisGrouped = SwAxisGrouped()


    def with_shared_axis_type(self, value: Optional[ApplicationPrimitiveDataType]) -> "SwAxisGroupedBuilder":
        """Set shared_axis_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.shared_axis_type = value
        return self

    def with_sw_axis_index(self, value: Optional[AxisIndexType]) -> "SwAxisGroupedBuilder":
        """Set sw_axis_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_axis_index = value
        return self

    def with_sw_calprm_ref_proxy(self, value: SwCalprmRefProxy) -> "SwAxisGroupedBuilder":
        """Set sw_calprm_ref_proxy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_calprm_ref_proxy = value
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


    def build(self) -> SwAxisGrouped:
        """Build and return the SwAxisGrouped instance with validation."""
        self._validate_instance()
        pass
        return self._obj