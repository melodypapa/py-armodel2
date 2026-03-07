"""VariableDataPrototypeInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1003)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class VariableDataPrototypeInSystemInstanceRef(ARObject):
    """AUTOSAR VariableDataPrototypeInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VARIABLE-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF"


    base_ref: Optional[ARRef]
    context_component_ref: Optional[ARRef]
    context_composition_ref: Optional[ARRef]
    context_port_ref: ARRef
    target_data_prototype_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": lambda obj, elem: setattr(obj, "base_ref", ARRef.deserialize(elem)),
        "CONTEXT-COMPONENT-REF": lambda obj, elem: setattr(obj, "context_component_ref", ARRef.deserialize(elem)),
        "CONTEXT-COMPOSITION-REF": lambda obj, elem: setattr(obj, "context_composition_ref", ARRef.deserialize(elem)),
        "CONTEXT-PORT-REF": ("_POLYMORPHIC", "context_port_ref", ["AbstractProvidedPortPrototype", "AbstractRequiredPortPrototype", "PPortPrototype", "PRPortPrototype", "RPortPrototype"]),
        "TARGET-DATA-PROTOTYPE-REF": lambda obj, elem: setattr(obj, "target_data_prototype_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize VariableDataPrototypeInSystemInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_component_ref: Optional[ARRef] = None
        self.context_composition_ref: Optional[ARRef] = None
        self.context_port_ref: ARRef = None
        self.target_data_prototype_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize VariableDataPrototypeInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariableDataPrototypeInSystemInstanceRef, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.base_ref, "System")
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

        # Serialize context_component_ref
        if self.context_component_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_component_ref, "SwComponentPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-COMPONENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_composition_ref
        if self.context_composition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_composition_ref, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-COMPOSITION-REF")
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

        # Serialize target_data_prototype_ref
        if self.target_data_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_data_prototype_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableDataPrototypeInSystemInstanceRef":
        """Deserialize XML element to VariableDataPrototypeInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableDataPrototypeInSystemInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariableDataPrototypeInSystemInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-COMPONENT-REF":
                setattr(obj, "context_component_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-COMPOSITION-REF":
                setattr(obj, "context_composition_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-PORT-REF":
                setattr(obj, "context_port_ref", ARRef.deserialize(child))
            elif tag == "TARGET-DATA-PROTOTYPE-REF":
                setattr(obj, "target_data_prototype_ref", ARRef.deserialize(child))

        return obj



class VariableDataPrototypeInSystemInstanceRefBuilder(BuilderBase):
    """Builder for VariableDataPrototypeInSystemInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: VariableDataPrototypeInSystemInstanceRef = VariableDataPrototypeInSystemInstanceRef()


    def with_base(self, value: Optional[System]) -> "VariableDataPrototypeInSystemInstanceRefBuilder":
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

    def with_context_component(self, value: Optional[SwComponentPrototype]) -> "VariableDataPrototypeInSystemInstanceRefBuilder":
        """Set context_component attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'context_component' is required and cannot be None")
        self._obj.context_component = value
        return self

    def with_context_composition(self, value: Optional[RootSwCompositionPrototype]) -> "VariableDataPrototypeInSystemInstanceRefBuilder":
        """Set context_composition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'context_composition' is required and cannot be None")
        self._obj.context_composition = value
        return self

    def with_context_port(self, value: PortPrototype) -> "VariableDataPrototypeInSystemInstanceRefBuilder":
        """Set context_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'context_port' is required and cannot be None")
        self._obj.context_port = value
        return self

    def with_target_data_prototype(self, value: Optional[VariableDataPrototype]) -> "VariableDataPrototypeInSystemInstanceRefBuilder":
        """Set target_data_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_data_prototype' is required and cannot be None")
        self._obj.target_data_prototype = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "contextPort",
    }
    _OPTIONAL_ATTRIBUTES = {
        "base",
        "contextComponent",
        "contextComposition",
        "targetDataPrototype",
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
        if getattr(self._obj, "contextPort", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'contextPort' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'contextPort' is None", UserWarning)


    def build(self) -> VariableDataPrototypeInSystemInstanceRef:
        """Build and return the VariableDataPrototypeInSystemInstanceRef instance with validation."""
        self._validate_instance()
        return self._obj