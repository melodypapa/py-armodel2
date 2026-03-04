"""DelegationSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2016)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import instance_ref
from armodel2.serialization.decorators import ref_conditional

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import SwConnectorBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DelegationSwConnector(SwConnector):
    """AUTOSAR DelegationSwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DELEGATION-SW-CONNECTOR"


    _inner_port_iref: Optional[PortInCompositionTypeInstanceRef]
    outer_port_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "INNER-PORT-IREF": ("_POLYMORPHIC", "_inner_port_iref", ["PPortInCompositionInstanceRef", "RPortInCompositionInstanceRef"]),
        "OUTER-PORT-REF": ("_POLYMORPHIC", "outer_port_ref", ["AbstractProvidedPortPrototype", "AbstractRequiredPortPrototype", "PPortPrototype", "PRPortPrototype", "RPortPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize DelegationSwConnector."""
        super().__init__()
        self._inner_port_iref: Optional[PortInCompositionTypeInstanceRef] = None
        self.outer_port_ref: Optional[ARRef] = None
    @property
    @instance_ref(flatten=False)
    def inner_port_iref(self) -> Optional[PortInCompositionTypeInstanceRef]:
        """Get inner_port_iref instance reference."""
        return self._inner_port_iref

    @inner_port_iref.setter
    def inner_port_iref(self, value: Optional[PortInCompositionTypeInstanceRef]) -> None:
        """Set inner_port_iref instance reference."""
        self._inner_port_iref = value


    def serialize(self) -> ET.Element:
        """Serialize DelegationSwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DelegationSwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize inner_port_iref (instance reference with wrapper "INNER-PORT-IREF")
        if self.inner_port_iref is not None:
            serialized = SerializationHelper.serialize_item(self.inner_port_iref, "PortInCompositionTypeInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("INNER-PORT-IREF")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

        # Serialize outer_port_ref
        if self.outer_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.outer_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OUTER-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DelegationSwConnector":
        """Deserialize XML element to DelegationSwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DelegationSwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DelegationSwConnector, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INNER-PORT-IREF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "P-PORT-IN-COMPOSITION-INSTANCE-REF":
                        setattr(obj, "_inner_port_iref", SerializationHelper.deserialize_by_tag(child[0], "PPortInCompositionInstanceRef"))
                    elif concrete_tag == "R-PORT-IN-COMPOSITION-INSTANCE-REF":
                        setattr(obj, "_inner_port_iref", SerializationHelper.deserialize_by_tag(child[0], "RPortInCompositionInstanceRef"))
            elif tag == "OUTER-PORT-REF":
                setattr(obj, "outer_port_ref", ARRef.deserialize(child))

        return obj



class DelegationSwConnectorBuilder(SwConnectorBuilder):
    """Builder for DelegationSwConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DelegationSwConnector = DelegationSwConnector()


    def with_inner_port(self, value: Optional[PortInCompositionTypeInstanceRef]) -> "DelegationSwConnectorBuilder":
        """Set inner_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.inner_port = value
        return self

    def with_outer_port(self, value: Optional[PortPrototype]) -> "DelegationSwConnectorBuilder":
        """Set outer_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.outer_port = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "innerPort",
        "outerPort",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DelegationSwConnector:
        """Build and return the DelegationSwConnector instance with validation."""
        self._validate_instance()
        return self._obj