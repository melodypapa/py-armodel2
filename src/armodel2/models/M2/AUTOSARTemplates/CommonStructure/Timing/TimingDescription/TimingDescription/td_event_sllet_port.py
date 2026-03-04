"""TDEventSLLETPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_sllet import (
    TDEventSLLET,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_sllet import TDEventSLLETBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventSLLETPort(TDEventSLLET):
    """AUTOSAR TDEventSLLETPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-S-L-L-E-T-PORT"


    port_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PORT-REF": ("_POLYMORPHIC", "port_ref", ["AbstractProvidedPortPrototype", "AbstractRequiredPortPrototype", "PPortPrototype", "PRPortPrototype", "RPortPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize TDEventSLLETPort."""
        super().__init__()
        self.port_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventSLLETPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventSLLETPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize port_ref
        if self.port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSLLETPort":
        """Deserialize XML element to TDEventSLLETPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventSLLETPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventSLLETPort, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PORT-REF":
                setattr(obj, "port_ref", ARRef.deserialize(child))

        return obj



class TDEventSLLETPortBuilder(TDEventSLLETBuilder):
    """Builder for TDEventSLLETPort with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventSLLETPort = TDEventSLLETPort()


    def with_port(self, value: Optional[PortPrototype]) -> "TDEventSLLETPortBuilder":
        """Set port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.port = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "port",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDEventSLLETPort:
        """Build and return the TDEventSLLETPort instance with validation."""
        self._validate_instance()
        return self._obj