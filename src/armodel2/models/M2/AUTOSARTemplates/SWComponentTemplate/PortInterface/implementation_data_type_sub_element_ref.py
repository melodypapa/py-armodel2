"""ImplementationDataTypeSubElementRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import SubElementRefBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.ar_parameter_in_implementation_data_instance_ref import (
    ArParameterInImplementationDataInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ImplementationDataTypeSubElementRef(SubElementRef):
    """AUTOSAR ImplementationDataTypeSubElementRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF"


    implementation: Optional[Any]
    parameter: Optional[ArParameterInImplementationDataInstanceRef]
    _DESERIALIZE_DISPATCH = {
        "IMPLEMENTATION": lambda obj, elem: setattr(obj, "implementation", SerializationHelper.deserialize_by_tag(elem, "any (ArVariableIn)")),
        "PARAMETER": lambda obj, elem: setattr(obj, "parameter", SerializationHelper.deserialize_by_tag(elem, "ArParameterInImplementationDataInstanceRef")),
    }


    def __init__(self) -> None:
        """Initialize ImplementationDataTypeSubElementRef."""
        super().__init__()
        self.implementation: Optional[Any] = None
        self.parameter: Optional[ArParameterInImplementationDataInstanceRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ImplementationDataTypeSubElementRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationDataTypeSubElementRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize implementation
        if self.implementation is not None:
            serialized = SerializationHelper.serialize_item(self.implementation, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter
        if self.parameter is not None:
            serialized = SerializationHelper.serialize_item(self.parameter, "ArParameterInImplementationDataInstanceRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeSubElementRef":
        """Deserialize XML element to ImplementationDataTypeSubElementRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataTypeSubElementRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationDataTypeSubElementRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IMPLEMENTATION":
                setattr(obj, "implementation", SerializationHelper.deserialize_by_tag(child, "any (ArVariableIn)"))
            elif tag == "PARAMETER":
                setattr(obj, "parameter", SerializationHelper.deserialize_by_tag(child, "ArParameterInImplementationDataInstanceRef"))

        return obj



class ImplementationDataTypeSubElementRefBuilder(SubElementRefBuilder):
    """Builder for ImplementationDataTypeSubElementRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ImplementationDataTypeSubElementRef = ImplementationDataTypeSubElementRef()


    def with_implementation(self, value: Optional[Any]) -> "ImplementationDataTypeSubElementRefBuilder":
        """Set implementation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'implementation' is required and cannot be None")
        self._obj.implementation = value
        return self

    def with_parameter(self, value: Optional[ArParameterInImplementationDataInstanceRef]) -> "ImplementationDataTypeSubElementRefBuilder":
        """Set parameter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'parameter' is required and cannot be None")
        self._obj.parameter = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "implementation",
        "parameter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ImplementationDataTypeSubElementRef:
        """Build and return the ImplementationDataTypeSubElementRef instance with validation."""
        self._validate_instance()
        return self._obj