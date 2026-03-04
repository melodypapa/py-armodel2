"""SwAxisGrouped AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 357)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import SwCalprmAxisTypePropsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel2.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwAxisGrouped(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisGrouped."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-AXIS-GROUPED"


    shared_axis_type_ref: Optional[ARRef]
    sw_axis_index: Optional[AxisIndexType]
    sw_calprm_ref_proxy_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "SHARED-AXIS-TYPE-REF": lambda obj, elem: setattr(obj, "shared_axis_type_ref", ARRef.deserialize(elem)),
        "SW-AXIS-INDEX": lambda obj, elem: setattr(obj, "sw_axis_index", SerializationHelper.deserialize_by_tag(elem, "AxisIndexType")),
        "SW-CALPRM-REF-PROXY-REF": lambda obj, elem: setattr(obj, "sw_calprm_ref_proxy_ref", ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SHARED-AXIS-TYPE-REF":
                setattr(obj, "shared_axis_type_ref", ARRef.deserialize(child))
            elif tag == "SW-AXIS-INDEX":
                setattr(obj, "sw_axis_index", SerializationHelper.deserialize_by_tag(child, "AxisIndexType"))
            elif tag == "SW-CALPRM-REF-PROXY-REF":
                setattr(obj, "sw_calprm_ref_proxy_ref", ARRef.deserialize(child))

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



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "swCalprmRefProxy",
    }
    _OPTIONAL_ATTRIBUTES = {
        "sharedAxisType",
        "swAxisIndex",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "swCalprmRefProxy", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'swCalprmRefProxy' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'swCalprmRefProxy' is None", UserWarning)


    def build(self) -> SwAxisGrouped:
        """Build and return the SwAxisGrouped instance with validation."""
        self._validate_instance()
        return self._obj