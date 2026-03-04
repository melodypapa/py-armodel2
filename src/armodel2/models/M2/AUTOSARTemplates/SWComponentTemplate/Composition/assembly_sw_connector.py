"""AssemblySwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 289)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

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
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.p_port_in_composition_instance_ref import (
    PPortInCompositionInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.r_port_in_composition_instance_ref import (
    RPortInCompositionInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AssemblySwConnector(SwConnector):
    """AUTOSAR AssemblySwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ASSEMBLY-SW-CONNECTOR"


    _provider_iref: Optional[PPortInCompositionInstanceRef]
    _requester_iref: Optional[RPortInCompositionInstanceRef]
    _DESERIALIZE_DISPATCH = {
        "PROVIDER-IREF": lambda obj, elem: setattr(obj, "_provider_iref", SerializationHelper.deserialize_by_tag(elem, "PPortInCompositionInstanceRef")),
        "REQUESTER-IREF": lambda obj, elem: setattr(obj, "_requester_iref", SerializationHelper.deserialize_by_tag(elem, "RPortInCompositionInstanceRef")),
    }


    def __init__(self) -> None:
        """Initialize AssemblySwConnector."""
        super().__init__()
        self._provider_iref: Optional[PPortInCompositionInstanceRef] = None
        self._requester_iref: Optional[RPortInCompositionInstanceRef] = None
    @property
    @instance_ref(flatten=True)
    def provider_iref(self) -> Optional[PPortInCompositionInstanceRef]:
        """Get provider_iref instance reference."""
        return self._provider_iref

    @provider_iref.setter
    def provider_iref(self, value: Optional[PPortInCompositionInstanceRef]) -> None:
        """Set provider_iref instance reference."""
        self._provider_iref = value

    @property
    @instance_ref(flatten=True)
    def requester_iref(self) -> Optional[RPortInCompositionInstanceRef]:
        """Get requester_iref instance reference."""
        return self._requester_iref

    @requester_iref.setter
    def requester_iref(self, value: Optional[RPortInCompositionInstanceRef]) -> None:
        """Set requester_iref instance reference."""
        self._requester_iref = value


    def serialize(self) -> ET.Element:
        """Serialize AssemblySwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AssemblySwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provider_iref (instance reference with wrapper "PROVIDER-IREF")
        if self.provider_iref is not None:
            serialized = SerializationHelper.serialize_item(self.provider_iref, "PPortInCompositionInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("PROVIDER-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        # Serialize requester_iref (instance reference with wrapper "REQUESTER-IREF")
        if self.requester_iref is not None:
            serialized = SerializationHelper.serialize_item(self.requester_iref, "RPortInCompositionInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("REQUESTER-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssemblySwConnector":
        """Deserialize XML element to AssemblySwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AssemblySwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AssemblySwConnector, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROVIDER-IREF":
                setattr(obj, "_provider_iref", SerializationHelper.deserialize_by_tag(child, "PPortInCompositionInstanceRef"))
            elif tag == "REQUESTER-IREF":
                setattr(obj, "_requester_iref", SerializationHelper.deserialize_by_tag(child, "RPortInCompositionInstanceRef"))

        return obj



class AssemblySwConnectorBuilder(SwConnectorBuilder):
    """Builder for AssemblySwConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AssemblySwConnector = AssemblySwConnector()


    def with_provider(self, value: Optional[PPortInCompositionInstanceRef]) -> "AssemblySwConnectorBuilder":
        """Set provider attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.provider = value
        return self

    def with_requester(self, value: Optional[RPortInCompositionInstanceRef]) -> "AssemblySwConnectorBuilder":
        """Set requester attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.requester = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "provider",
        "requester",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AssemblySwConnector:
        """Build and return the AssemblySwConnector instance with validation."""
        self._validate_instance()
        return self._obj