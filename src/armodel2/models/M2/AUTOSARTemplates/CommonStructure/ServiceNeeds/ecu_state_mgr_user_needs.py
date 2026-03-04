"""EcuStateMgrUserNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 714)

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


class EcuStateMgrUserNeeds(ServiceNeeds):
    """AUTOSAR EcuStateMgrUserNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECU-STATE-MGR-USER-NEEDS"


    def __init__(self) -> None:
        """Initialize EcuStateMgrUserNeeds."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize EcuStateMgrUserNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcuStateMgrUserNeeds, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "EcuStateMgrUserNeeds":
        """Deserialize XML element to EcuStateMgrUserNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuStateMgrUserNeeds object
        """
        # Delegate to parent class to handle inherited attributes
        return super(EcuStateMgrUserNeeds, cls).deserialize(element)



class EcuStateMgrUserNeedsBuilder(ServiceNeedsBuilder):
    """Builder for EcuStateMgrUserNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcuStateMgrUserNeeds = EcuStateMgrUserNeeds()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcuStateMgrUserNeeds:
        """Build and return the EcuStateMgrUserNeeds instance with validation."""
        self._validate_instance()
        return self._obj