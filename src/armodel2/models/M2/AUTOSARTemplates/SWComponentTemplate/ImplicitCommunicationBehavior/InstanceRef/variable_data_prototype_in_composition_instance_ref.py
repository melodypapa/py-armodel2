"""VariableDataPrototypeInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 959)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class VariableDataPrototypeInCompositionInstanceRef(ARObject):
    """AUTOSAR VariableDataPrototypeInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VARIABLE-DATA-PROTOTYPE-IN-COMPOSITION-INSTANCE-REF"


    base_ref: Optional[ARRef]
    context_port_ref: Optional[ARRef]
    context_sw_refs: list[Any]
    target_variable_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": lambda obj, elem: setattr(obj, "base_ref", ARRef.deserialize(elem)),
        "CONTEXT-PORT-REF": ("_POLYMORPHIC", "context_port_ref", ["AbstractProvidedPortPrototype", "AbstractRequiredPortPrototype", "PPortPrototype", "PRPortPrototype", "RPortPrototype"]),
        "CONTEXT-SW-REFS": lambda obj, elem: [obj.context_sw_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "TARGET-VARIABLE-REF": lambda obj, elem: setattr(obj, "target_variable_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize VariableDataPrototypeInCompositionInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_port_ref: Optional[ARRef] = None
        self.context_sw_refs: list[Any] = []
        self.target_variable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize VariableDataPrototypeInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariableDataPrototypeInCompositionInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "CompositionSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_port_ref
        if self.context_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_sw_refs (list to container "CONTEXT-SW-REFS")
        if self.context_sw_refs:
            wrapper = ET.Element("CONTEXT-SW-REFS")
            for item in self.context_sw_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-SW-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_variable_ref
        if self.target_variable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_variable_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableDataPrototypeInCompositionInstanceRef":
        """Deserialize XML element to VariableDataPrototypeInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableDataPrototypeInCompositionInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariableDataPrototypeInCompositionInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-PORT-REF":
                setattr(obj, "context_port_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-SW-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_sw_refs.append(ARRef.deserialize(item_elem))
            elif tag == "TARGET-VARIABLE-REF":
                setattr(obj, "target_variable_ref", ARRef.deserialize(child))

        return obj



class VariableDataPrototypeInCompositionInstanceRefBuilder(BuilderBase):
    """Builder for VariableDataPrototypeInCompositionInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: VariableDataPrototypeInCompositionInstanceRef = VariableDataPrototypeInCompositionInstanceRef()


    def with_base(self, value: Optional[CompositionSwComponentType]) -> "VariableDataPrototypeInCompositionInstanceRefBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'base' is required and cannot be None")
        self._obj.base = value
        return self

    def with_context_port(self, value: Optional[PortPrototype]) -> "VariableDataPrototypeInCompositionInstanceRefBuilder":
        """Set context_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'context_port' is required and cannot be None")
        self._obj.context_port = value
        return self

    def with_context_sws(self, items: list[Any]) -> "VariableDataPrototypeInCompositionInstanceRefBuilder":
        """Set context_sws list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_sws = list(items) if items else []
        return self

    def with_target_variable(self, value: Optional[VariableDataPrototype]) -> "VariableDataPrototypeInCompositionInstanceRefBuilder":
        """Set target_variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_variable' is required and cannot be None")
        self._obj.target_variable = value
        return self


    def add_context_sw(self, item: Any) -> "VariableDataPrototypeInCompositionInstanceRefBuilder":
        """Add a single item to context_sws list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_sws.append(item)
        return self

    def clear_context_sws(self) -> "VariableDataPrototypeInCompositionInstanceRefBuilder":
        """Clear all items from context_sws list.

        Returns:
            self for method chaining
        """
        self._obj.context_sws = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "base",
        "contextPort",
        "contextSw",
        "targetVariable",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> VariableDataPrototypeInCompositionInstanceRef:
        """Build and return the VariableDataPrototypeInCompositionInstanceRef instance with validation."""
        self._validate_instance()
        return self._obj