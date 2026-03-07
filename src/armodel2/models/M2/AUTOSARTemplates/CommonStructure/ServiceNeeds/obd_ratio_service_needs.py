"""ObdRatioServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 795)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import DiagnosticCapabilityElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ObdRatioConnectionKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdRatioServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "OBD-RATIO-SERVICE-NEEDS"


    connection_type: Optional[ObdRatioConnectionKindEnum]
    rate_based_monitored_event_ref: Optional[ARRef]
    used_fid_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONNECTION-TYPE": lambda obj, elem: setattr(obj, "connection_type", ObdRatioConnectionKindEnum.deserialize(elem)),
        "RATE-BASED-MONITORED-EVENT-REF": lambda obj, elem: setattr(obj, "rate_based_monitored_event_ref", ARRef.deserialize(elem)),
        "USED-FID-REF": lambda obj, elem: setattr(obj, "used_fid_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ObdRatioServiceNeeds."""
        super().__init__()
        self.connection_type: Optional[ObdRatioConnectionKindEnum] = None
        self.rate_based_monitored_event_ref: Optional[ARRef] = None
        self.used_fid_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ObdRatioServiceNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ObdRatioServiceNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connection_type
        if self.connection_type is not None:
            serialized = SerializationHelper.serialize_item(self.connection_type, "ObdRatioConnectionKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTION-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_based_monitored_event_ref
        if self.rate_based_monitored_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.rate_based_monitored_event_ref, "DiagnosticEventNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-BASED-MONITORED-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize used_fid_ref
        if self.used_fid_ref is not None:
            serialized = SerializationHelper.serialize_item(self.used_fid_ref, "FunctionInhibitionNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-FID-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdRatioServiceNeeds":
        """Deserialize XML element to ObdRatioServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdRatioServiceNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ObdRatioServiceNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONNECTION-TYPE":
                setattr(obj, "connection_type", ObdRatioConnectionKindEnum.deserialize(child))
            elif tag == "RATE-BASED-MONITORED-EVENT-REF":
                setattr(obj, "rate_based_monitored_event_ref", ARRef.deserialize(child))
            elif tag == "USED-FID-REF":
                setattr(obj, "used_fid_ref", ARRef.deserialize(child))

        return obj



class ObdRatioServiceNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for ObdRatioServiceNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ObdRatioServiceNeeds = ObdRatioServiceNeeds()


    def with_connection_type(self, value: Optional[ObdRatioConnectionKindEnum]) -> "ObdRatioServiceNeedsBuilder":
        """Set connection_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'connection_type' is required and cannot be None")
        self._obj.connection_type = value
        return self

    def with_rate_based_monitored_event(self, value: Optional[DiagnosticEventNeeds]) -> "ObdRatioServiceNeedsBuilder":
        """Set rate_based_monitored_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rate_based_monitored_event' is required and cannot be None")
        self._obj.rate_based_monitored_event = value
        return self

    def with_used_fid(self, value: Optional[FunctionInhibitionNeeds]) -> "ObdRatioServiceNeedsBuilder":
        """Set used_fid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'used_fid' is required and cannot be None")
        self._obj.used_fid = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "connectionType",
        "rateBasedMonitoredEvent",
        "usedFid",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ObdRatioServiceNeeds:
        """Build and return the ObdRatioServiceNeeds instance with validation."""
        self._validate_instance()
        return self._obj