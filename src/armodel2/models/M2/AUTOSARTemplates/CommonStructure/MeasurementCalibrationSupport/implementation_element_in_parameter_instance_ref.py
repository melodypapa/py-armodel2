"""ImplementationElementInParameterInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
        ParameterDataPrototype,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ImplementationElementInParameterInstanceRef(ARObject):
    """AUTOSAR ImplementationElementInParameterInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IMPLEMENTATION-ELEMENT-IN-PARAMETER-INSTANCE-REF"


    context_ref: Optional[ARRef]
    target_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "CONTEXT-REF": lambda obj, elem: setattr(obj, "context_ref", ARRef.deserialize(elem)),
        "TARGET-REF": lambda obj, elem: setattr(obj, "target_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ImplementationElementInParameterInstanceRef."""
        super().__init__()
        self.context_ref: Optional[ARRef] = None
        self.target_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ImplementationElementInParameterInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationElementInParameterInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_ref
        if self.context_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_ref, "ParameterDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_ref
        if self.target_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationElementInParameterInstanceRef":
        """Deserialize XML element to ImplementationElementInParameterInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationElementInParameterInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationElementInParameterInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTEXT-REF":
                setattr(obj, "context_ref", ARRef.deserialize(child))
            elif tag == "TARGET-REF":
                setattr(obj, "target_ref", ARRef.deserialize(child))

        return obj



class ImplementationElementInParameterInstanceRefBuilder(BuilderBase):
    """Builder for ImplementationElementInParameterInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ImplementationElementInParameterInstanceRef = ImplementationElementInParameterInstanceRef()


    def with_context(self, value: Optional[ParameterDataPrototype]) -> "ImplementationElementInParameterInstanceRefBuilder":
        """Set context attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context = value
        return self

    def with_target(self, value: Optional[any (AbstractImplementation)]) -> "ImplementationElementInParameterInstanceRefBuilder":
        """Set target attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "context",
        "target",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ImplementationElementInParameterInstanceRef:
        """Build and return the ImplementationElementInParameterInstanceRef instance with validation."""
        self._validate_instance()
        return self._obj