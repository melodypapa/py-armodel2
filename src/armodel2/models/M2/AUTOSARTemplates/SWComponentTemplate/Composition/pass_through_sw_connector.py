"""PassThroughSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 83)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2043)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import SwConnectorBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PassThroughSwConnector(SwConnector):
    """AUTOSAR PassThroughSwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PASS-THROUGH-SW-CONNECTOR"


    provided_outer_ref: Optional[ARRef]
    required_outer_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PROVIDED-OUTER-REF": ("_POLYMORPHIC", "provided_outer_ref", ["PPortPrototype", "PRPortPrototype"]),
        "REQUIRED-OUTER-REF": ("_POLYMORPHIC", "required_outer_ref", ["PRPortPrototype", "RPortPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize PassThroughSwConnector."""
        super().__init__()
        self.provided_outer_ref: Optional[ARRef] = None
        self.required_outer_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PassThroughSwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PassThroughSwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided_outer_ref
        if self.provided_outer_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provided_outer_ref, "AbstractProvidedPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-OUTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required_outer_ref
        if self.required_outer_ref is not None:
            serialized = SerializationHelper.serialize_item(self.required_outer_ref, "AbstractRequiredPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-OUTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PassThroughSwConnector":
        """Deserialize XML element to PassThroughSwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PassThroughSwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PassThroughSwConnector, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROVIDED-OUTER-REF":
                setattr(obj, "provided_outer_ref", ARRef.deserialize(child))
            elif tag == "REQUIRED-OUTER-REF":
                setattr(obj, "required_outer_ref", ARRef.deserialize(child))

        return obj



class PassThroughSwConnectorBuilder(SwConnectorBuilder):
    """Builder for PassThroughSwConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PassThroughSwConnector = PassThroughSwConnector()


    def with_provided_outer(self, value: Optional[AbstractProvidedPortPrototype]) -> "PassThroughSwConnectorBuilder":
        """Set provided_outer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'provided_outer' is required and cannot be None")
        self._obj.provided_outer = value
        return self

    def with_required_outer(self, value: Optional[AbstractRequiredPortPrototype]) -> "PassThroughSwConnectorBuilder":
        """Set required_outer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'required_outer' is required and cannot be None")
        self._obj.required_outer = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "providedOuter",
        "requiredOuter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PassThroughSwConnector:
        """Build and return the PassThroughSwConnector instance with validation."""
        self._validate_instance()
        return self._obj