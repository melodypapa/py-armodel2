"""InstantiationDataDefProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 588)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_InstantiationDataDefProps.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
        AutosarParameterRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
        AutosarVariableRef,
    )
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class InstantiationDataDefProps(ARObject):
    """AUTOSAR InstantiationDataDefProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INSTANTIATION-DATA-DEF-PROPS"


    parameter_ref: Optional[ARRef]
    sw_data_def: Optional[SwDataDefProps]
    variable_instance_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PARAMETER-REF": lambda obj, elem: setattr(obj, "parameter_ref", ARRef.deserialize(elem)),
        "SW-DATA-DEF": lambda obj, elem: setattr(obj, "sw_data_def", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
        "VARIABLE-INSTANCE-REF": lambda obj, elem: setattr(obj, "variable_instance_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize InstantiationDataDefProps."""
        super().__init__()
        self.parameter_ref: Optional[ARRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.variable_instance_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize InstantiationDataDefProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InstantiationDataDefProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize parameter_ref
        if self.parameter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.parameter_ref, "AutosarParameterRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_data_def
        if self.sw_data_def is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_instance_ref
        if self.variable_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.variable_instance_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstantiationDataDefProps":
        """Deserialize XML element to InstantiationDataDefProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InstantiationDataDefProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InstantiationDataDefProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PARAMETER-REF":
                setattr(obj, "parameter_ref", ARRef.deserialize(child))
            elif tag == "SW-DATA-DEF":
                setattr(obj, "sw_data_def", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))
            elif tag == "VARIABLE-INSTANCE-REF":
                setattr(obj, "variable_instance_ref", ARRef.deserialize(child))

        return obj



class InstantiationDataDefPropsBuilder(BuilderBase):
    """Builder for InstantiationDataDefProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InstantiationDataDefProps = InstantiationDataDefProps()


    def with_parameter(self, value: Optional[AutosarParameterRef]) -> "InstantiationDataDefPropsBuilder":
        """Set parameter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.parameter = value
        return self

    def with_sw_data_def(self, value: Optional[SwDataDefProps]) -> "InstantiationDataDefPropsBuilder":
        """Set sw_data_def attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_data_def = value
        return self

    def with_variable_instance(self, value: Optional[AutosarVariableRef]) -> "InstantiationDataDefPropsBuilder":
        """Set variable_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.variable_instance = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "parameter",
        "swDataDef",
        "variableInstance",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> InstantiationDataDefProps:
        """Build and return the InstantiationDataDefProps instance with validation."""
        self._validate_instance()
        return self._obj