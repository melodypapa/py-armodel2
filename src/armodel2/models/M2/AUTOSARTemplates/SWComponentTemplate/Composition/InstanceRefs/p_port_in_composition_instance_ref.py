"""PPortInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 951)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import PortInCompositionTypeInstanceRefBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR PPortInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "P-PORT-IN-COMPOSITION-INSTANCE-REF"


    context_component_ref: Optional[ARRef]
    target_p_port_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONTEXT-COMPONENT-REF": lambda obj, elem: setattr(obj, "context_component_ref", ARRef.deserialize(elem)),
        "TARGET-P-PORT-REF": ("_POLYMORPHIC", "target_p_port_ref", ["PPortPrototype", "PRPortPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize PPortInCompositionInstanceRef."""
        super().__init__()
        self.context_component_ref: Optional[ARRef] = None
        self.target_p_port_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PPortInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PPortInCompositionInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize target_p_port_ref
        if self.target_p_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_p_port_ref, "AbstractProvidedPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-P-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PPortInCompositionInstanceRef":
        """Deserialize XML element to PPortInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PPortInCompositionInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PPortInCompositionInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTEXT-COMPONENT-REF":
                setattr(obj, "context_component_ref", ARRef.deserialize(child))
            elif tag == "TARGET-P-PORT-REF":
                setattr(obj, "target_p_port_ref", ARRef.deserialize(child))

        return obj



class PPortInCompositionInstanceRefBuilder(PortInCompositionTypeInstanceRefBuilder):
    """Builder for PPortInCompositionInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PPortInCompositionInstanceRef = PPortInCompositionInstanceRef()


    def with_context_component(self, value: Optional[SwComponentPrototype]) -> "PPortInCompositionInstanceRefBuilder":
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

    def with_target_p_port(self, value: Optional[AbstractProvidedPortPrototype]) -> "PPortInCompositionInstanceRefBuilder":
        """Set target_p_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_p_port' is required and cannot be None")
        self._obj.target_p_port = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "contextComponent",
        "targetPPort",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PPortInCompositionInstanceRef:
        """Build and return the PPortInCompositionInstanceRef instance with validation."""
        self._validate_instance()
        return self._obj