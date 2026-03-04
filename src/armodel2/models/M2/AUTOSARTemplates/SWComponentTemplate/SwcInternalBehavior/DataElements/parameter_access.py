"""ParameterAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 586)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import AbstractAccessPointBuilder

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
        AutosarParameterRef,
    )
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ParameterAccess(AbstractAccessPoint):
    """AUTOSAR ParameterAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PARAMETER-ACCESS"


    accessed_parameter: Optional[AutosarParameterRef]
    sw_data_def_props: Optional[SwDataDefProps]
    _DESERIALIZE_DISPATCH = {
        "ACCESSED-PARAMETER": lambda obj, elem: setattr(obj, "accessed_parameter", SerializationHelper.deserialize_by_tag(elem, "AutosarParameterRef")),
        "SW-DATA-DEF-PROPS": lambda obj, elem: setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
    }


    def __init__(self) -> None:
        """Initialize ParameterAccess."""
        super().__init__()
        self.accessed_parameter: Optional[AutosarParameterRef] = None
        self.sw_data_def_props: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize ParameterAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ParameterAccess, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accessed_parameter
        if self.accessed_parameter is not None:
            serialized = SerializationHelper.serialize_item(self.accessed_parameter, "AutosarParameterRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESSED-PARAMETER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_data_def_props
        if self.sw_data_def_props is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def_props, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterAccess":
        """Deserialize XML element to ParameterAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterAccess object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterAccess, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCESSED-PARAMETER":
                setattr(obj, "accessed_parameter", SerializationHelper.deserialize_by_tag(child, "AutosarParameterRef"))
            elif tag == "SW-DATA-DEF-PROPS":
                setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))

        return obj



class ParameterAccessBuilder(AbstractAccessPointBuilder):
    """Builder for ParameterAccess with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ParameterAccess = ParameterAccess()


    def with_accessed_parameter(self, value: Optional[AutosarParameterRef]) -> "ParameterAccessBuilder":
        """Set accessed_parameter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.accessed_parameter = value
        return self

    def with_sw_data_def_props(self, value: Optional[SwDataDefProps]) -> "ParameterAccessBuilder":
        """Set sw_data_def_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_data_def_props = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "accessedParameter",
        "swDataDefProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ParameterAccess:
        """Build and return the ParameterAccess instance with validation."""
        self._validate_instance()
        return self._obj