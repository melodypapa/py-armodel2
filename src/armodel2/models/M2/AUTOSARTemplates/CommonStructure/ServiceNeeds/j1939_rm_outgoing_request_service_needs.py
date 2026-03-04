"""J1939RmOutgoingRequestServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 829)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import ServiceNeedsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class J1939RmOutgoingRequestServiceNeeds(ServiceNeeds):
    """AUTOSAR J1939RmOutgoingRequestServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "J1939-RM-OUTGOING-REQUEST-SERVICE-NEEDS"


    def __init__(self) -> None:
        """Initialize J1939RmOutgoingRequestServiceNeeds."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize J1939RmOutgoingRequestServiceNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939RmOutgoingRequestServiceNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939RmOutgoingRequestServiceNeeds":
        """Deserialize XML element to J1939RmOutgoingRequestServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939RmOutgoingRequestServiceNeeds object
        """
        # Delegate to parent class to handle inherited attributes
        return super(J1939RmOutgoingRequestServiceNeeds, cls).deserialize(element)



class J1939RmOutgoingRequestServiceNeedsBuilder(ServiceNeedsBuilder):
    """Builder for J1939RmOutgoingRequestServiceNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939RmOutgoingRequestServiceNeeds = J1939RmOutgoingRequestServiceNeeds()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> J1939RmOutgoingRequestServiceNeeds:
        """Build and return the J1939RmOutgoingRequestServiceNeeds instance with validation."""
        self._validate_instance()
        return self._obj