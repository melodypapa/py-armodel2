"""SwDataDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 373)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_generic_math import (
    CompuGenericMath,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
        SwCalprmRefProxy,
    )
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_dependency_args import (
        SwDataDependencyArgs,
    )
    from armodel2.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
        SwVariableRefProxy,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwDataDependency(ARObject):
    """AUTOSAR SwDataDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-DATA-DEPENDENCY"


    sw_data_dependency_args: Optional[SwDataDependencyArgs]
    sw_calprm_ref: Optional[SwCalprmRefProxy]
    sw_variable: Optional[SwVariableRefProxy]
    sw_data_dependency_formula: Optional[CompuGenericMath]
    _DESERIALIZE_DISPATCH = {
        "SW-DATA-DEPENDENCY-ARGS": lambda obj, elem: setattr(obj, "sw_data_dependency_args", SerializationHelper.deserialize_by_tag(elem, "SwDataDependencyArgs")),
        "SW-CALPRM-REF": lambda obj, elem: setattr(obj, "sw_calprm_ref", SerializationHelper.deserialize_by_tag(elem, "SwCalprmRefProxy")),
        "SW-VARIABLE": lambda obj, elem: setattr(obj, "sw_variable", SerializationHelper.deserialize_by_tag(elem, "SwVariableRefProxy")),
        "SW-DATA-DEPENDENCY-FORMULA": lambda obj, elem: setattr(obj, "sw_data_dependency_formula", SerializationHelper.deserialize_by_tag(elem, "CompuGenericMath")),
    }


    def __init__(self) -> None:
        """Initialize SwDataDependency."""
        super().__init__()
        self.sw_data_dependency_args: Optional[SwDataDependencyArgs] = None
        self.sw_calprm_ref: Optional[SwCalprmRefProxy] = None
        self.sw_variable: Optional[SwVariableRefProxy] = None
        self.sw_data_dependency_formula: Optional[CompuGenericMath] = None

    def serialize(self) -> ET.Element:
        """Serialize SwDataDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwDataDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_data_dependency_args (atp_mixed - append children directly)
        if self.sw_data_dependency_args is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_dependency_args, "SwDataDependencyArgs")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        # Serialize sw_calprm_ref
        if self.sw_calprm_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calprm_ref, "SwCalprmRefProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CALPRM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_variable
        if self.sw_variable is not None:
            serialized = SerializationHelper.serialize_item(self.sw_variable, "SwVariableRefProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-VARIABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_data_dependency_formula
        if self.sw_data_dependency_formula is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_dependency_formula, "CompuGenericMath")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEPENDENCY-FORMULA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDependency":
        """Deserialize XML element to SwDataDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwDataDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwDataDependency, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SW-DATA-DEPENDENCY-ARGS":
                setattr(obj, "sw_data_dependency_args", SerializationHelper.deserialize_by_tag(child, "SwDataDependencyArgs"))
            elif tag == "SW-CALPRM-REF":
                setattr(obj, "sw_calprm_ref", SerializationHelper.deserialize_by_tag(child, "SwCalprmRefProxy"))
            elif tag == "SW-VARIABLE":
                setattr(obj, "sw_variable", SerializationHelper.deserialize_by_tag(child, "SwVariableRefProxy"))
            elif tag == "SW-DATA-DEPENDENCY-FORMULA":
                setattr(obj, "sw_data_dependency_formula", SerializationHelper.deserialize_by_tag(child, "CompuGenericMath"))

        return obj



class SwDataDependencyBuilder(BuilderBase):
    """Builder for SwDataDependency with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwDataDependency = SwDataDependency()


    def with_sw_data_dependency_args(self, value: Optional[SwDataDependencyArgs]) -> "SwDataDependencyBuilder":
        """Set sw_data_dependency_args attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_data_dependency_args' is required and cannot be None")
        self._obj.sw_data_dependency_args = value
        return self

    def with_sw_calprm_ref(self, value: Optional[SwCalprmRefProxy]) -> "SwDataDependencyBuilder":
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

    def with_sw_variable(self, value: Optional[SwVariableRefProxy]) -> "SwDataDependencyBuilder":
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

    def with_sw_data_dependency_formula(self, value: Optional[CompuGenericMath]) -> "SwDataDependencyBuilder":
        """Set sw_data_dependency_formula attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_data_dependency_formula' is required and cannot be None")
        self._obj.sw_data_dependency_formula = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "swDataDependencyArgs",
        "swDataDependencyFormula",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwDataDependency:
        """Build and return the SwDataDependency instance with validation."""
        self._validate_instance()
        return self._obj