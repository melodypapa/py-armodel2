"""SwDataDependencyArgs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 374)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
        SwCalprmRefProxy,
    )
    from armodel2.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
        SwVariableRefProxy,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
@atp_mixed()

class SwDataDependencyArgs(ARObject):
    """AUTOSAR SwDataDependencyArgs."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-DATA-DEPENDENCY-ARGS"


    sw_calprm_ref: Optional[SwCalprmRefProxy]
    sw_variable: Optional[SwVariableRefProxy]
    _DESERIALIZE_DISPATCH = {
        "SW-CALPRM-REF": lambda obj, elem: setattr(obj, "sw_calprm_ref", SerializationHelper.deserialize_by_tag(elem, "SwCalprmRefProxy")),
        "SW-VARIABLE": lambda obj, elem: setattr(obj, "sw_variable", SerializationHelper.deserialize_by_tag(elem, "SwVariableRefProxy")),
    }


    def __init__(self) -> None:
        """Initialize SwDataDependencyArgs."""
        super().__init__()
        self.sw_calprm_ref: Optional[SwCalprmRefProxy] = None
        self.sw_variable: Optional[SwVariableRefProxy] = None

    def serialize(self) -> ET.Element:
        """Serialize SwDataDependencyArgs to XML element (atp_mixed - no wrapping).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwDataDependencyArgs, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_calprm_ref (complex type)
        if self.sw_calprm_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calprm_ref, "SwCalprmRefProxy")
            if serialized is not None:
                wrapped = ET.Element("SW-CALPRM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_variable (complex type)
        if self.sw_variable is not None:
            serialized = SerializationHelper.serialize_item(self.sw_variable, "SwVariableRefProxy")
            if serialized is not None:
                wrapped = ET.Element("SW-VARIABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDependencyArgs":
        """Deserialize XML element to SwDataDependencyArgs object (atp_mixed - no unwrapping).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwDataDependencyArgs object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwDataDependencyArgs, cls).deserialize(element)

        # Parse sw_calprm_ref
        child = SerializationHelper.find_child_element(element, "SW-CALPRM-REF")
        if child is not None:
            sw_calprm_ref_value = SerializationHelper.deserialize_by_tag(child, "SwCalprmRefProxy")
            obj.sw_calprm_ref = sw_calprm_ref_value

        # Parse sw_variable
        child = SerializationHelper.find_child_element(element, "SW-VARIABLE")
        if child is not None:
            sw_variable_value = SerializationHelper.deserialize_by_tag(child, "SwVariableRefProxy")
            obj.sw_variable = sw_variable_value

        return obj



class SwDataDependencyArgsBuilder(BuilderBase):
    """Builder for SwDataDependencyArgs with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwDataDependencyArgs = SwDataDependencyArgs()


    def with_sw_calprm_ref(self, value: Optional[SwCalprmRefProxy]) -> "SwDataDependencyArgsBuilder":
        """Set sw_calprm_ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_calprm_ref' is required and cannot be None")
        self._obj.sw_calprm_ref = value
        return self

    def with_sw_variable(self, value: Optional[SwVariableRefProxy]) -> "SwDataDependencyArgsBuilder":
        """Set sw_variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_variable' is required and cannot be None")
        self._obj.sw_variable = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "swCalprmRef",
        "swVariable",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwDataDependencyArgs:
        """Build and return the SwDataDependencyArgs instance with validation."""
        self._validate_instance()
        return self._obj