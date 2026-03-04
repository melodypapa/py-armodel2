"""DoIpRoutingActivationConfirmationNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 807)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import DoIpServiceNeedsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DoIpRoutingActivationConfirmationNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpRoutingActivationConfirmationNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DO-IP-ROUTING-ACTIVATION-CONFIRMATION-NEEDS"


    data_length: Optional[PositiveInteger]
    routing: Optional[NameToken]
    _DESERIALIZE_DISPATCH = {
        "DATA-LENGTH": lambda obj, elem: setattr(obj, "data_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "ROUTING": lambda obj, elem: setattr(obj, "routing", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
    }


    def __init__(self) -> None:
        """Initialize DoIpRoutingActivationConfirmationNeeds."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.routing: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize DoIpRoutingActivationConfirmationNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpRoutingActivationConfirmationNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_length
        if self.data_length is not None:
            serialized = SerializationHelper.serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize routing
        if self.routing is not None:
            serialized = SerializationHelper.serialize_item(self.routing, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROUTING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpRoutingActivationConfirmationNeeds":
        """Deserialize XML element to DoIpRoutingActivationConfirmationNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpRoutingActivationConfirmationNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpRoutingActivationConfirmationNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-LENGTH":
                setattr(obj, "data_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "ROUTING":
                setattr(obj, "routing", SerializationHelper.deserialize_by_tag(child, "NameToken"))

        return obj



class DoIpRoutingActivationConfirmationNeedsBuilder(DoIpServiceNeedsBuilder):
    """Builder for DoIpRoutingActivationConfirmationNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DoIpRoutingActivationConfirmationNeeds = DoIpRoutingActivationConfirmationNeeds()


    def with_data_length(self, value: Optional[PositiveInteger]) -> "DoIpRoutingActivationConfirmationNeedsBuilder":
        """Set data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_length = value
        return self

    def with_routing(self, value: Optional[NameToken]) -> "DoIpRoutingActivationConfirmationNeedsBuilder":
        """Set routing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.routing = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataLength",
        "routing",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DoIpRoutingActivationConfirmationNeeds:
        """Build and return the DoIpRoutingActivationConfirmationNeeds instance with validation."""
        self._validate_instance()
        return self._obj