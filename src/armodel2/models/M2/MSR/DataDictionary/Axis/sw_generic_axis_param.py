"""SwGenericAxisParam AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 356)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwGenericAxisParam(ARObject):
    """AUTOSAR SwGenericAxisParam."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-GENERIC-AXIS-PARAM"


    sw_generic_axis_param_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SW-GENERIC-AXIS-PARAM-REF": lambda obj, elem: setattr(obj, "sw_generic_axis_param_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SwGenericAxisParam."""
        super().__init__()
        self.sw_generic_axis_param_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwGenericAxisParam to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwGenericAxisParam, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_generic_axis_param_ref
        if self.sw_generic_axis_param_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_generic_axis_param_ref, "SwGenericAxisParam")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-GENERIC-AXIS-PARAM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwGenericAxisParam":
        """Deserialize XML element to SwGenericAxisParam object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwGenericAxisParam object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwGenericAxisParam, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SW-GENERIC-AXIS-PARAM-REF":
                setattr(obj, "sw_generic_axis_param_ref", ARRef.deserialize(child))

        return obj



class SwGenericAxisParamBuilder(BuilderBase):
    """Builder for SwGenericAxisParam with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwGenericAxisParam = SwGenericAxisParam()


    def with_sw_generic_axis_param(self, value: Optional[SwGenericAxisParam]) -> "SwGenericAxisParamBuilder":
        """Set sw_generic_axis_param attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_generic_axis_param' is required and cannot be None")
        self._obj.sw_generic_axis_param = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "swGenericAxisParam",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwGenericAxisParam:
        """Build and return the SwGenericAxisParam instance with validation."""
        self._validate_instance()
        return self._obj